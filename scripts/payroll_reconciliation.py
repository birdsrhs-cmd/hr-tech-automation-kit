"""
Payroll Reconciliation Tool
Author: Cataleya | HR Tech Specialist
Description: Cross-references payroll CSV against benefits/tax registries
to identify missing enrollments, salary mismatches, and ID discrepancies.
"""

import pandas as pd
import sys
from datetime import datetime

def reconcile_payroll(payroll_file, benefits_file):
    """
    Reconcile payroll master file against benefits registry.
    Flags missing enrollments and salary mismatches.
    """
    print(f"\n{'='*60}")
    print(f"PAYROLL RECONCILIATION REPORT | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    # Load files
    print(f"[*] Loading payroll file: {payroll_file}")
    try:
        payroll_df = pd.read_csv(payroll_file)
    except Exception as e:
        print(f"[!] ERROR loading payroll file: {e}")
        sys.exit(1)

    print(f"[*] Loading benefits file: {benefits_file}")
    try:
        benefits_df = pd.read_csv(benefits_file)
    except Exception as e:
        print(f"[!] ERROR loading benefits file: {e}")
        sys.exit(1)

    print(f"[+] Payroll records: {len(payroll_df)}")
    print(f"[+] Benefits records: {len(benefits_df)}\n")

    # Check 1: Employees in payroll but missing from benefits
    print("--- ENROLLMENT AUDIT ---")
    payroll_ids = set(payroll_df['Employee_ID'].dropna())
    benefits_ids = set(benefits_df['Employee_ID'].dropna())
    missing_enrollments = payroll_ids - benefits_ids

    if missing_enrollments:
        print(f"[!] {len(missing_enrollments)} employees in payroll but NOT enrolled in benefits:")
        missing_recs = payroll_df[payroll_df['Employee_ID'].isin(missing_enrollments)][['Employee_ID', 'Full_Name', 'Department']]
        print(missing_recs.to_string(index=False))
    else:
        print("[+] All payroll employees are enrolled in benefits. ✓")

    # Check 2: Employees in benefits but missing from payroll
    orphaned = benefits_ids - payroll_ids
    if orphaned:
        print(f"\n[!] {len(orphaned)} benefits enrollments with no payroll record:")
        orphan_recs = benefits_df[benefits_df['Employee_ID'].isin(orphaned)][['Employee_ID', 'Full_Name']]
        print(orphan_recs.to_string(index=False))
    else:
        print("\n[+] No orphaned benefits records. ✓")

    # Check 3: Salary mismatch (if applicable)
    print("\n--- SALARY VERIFICATION ---")
    if 'Salary' in payroll_df.columns and 'Salary' in benefits_df.columns:
        merged = pd.merge(payroll_df[['Employee_ID', 'Full_Name', 'Salary']], 
                         benefits_df[['Employee_ID', 'Salary']], 
                         on='Employee_ID', 
                         suffixes=('_payroll', '_benefits'))
        salary_mismatches = merged[merged['Salary_payroll'] != merged['Salary_benefits']]
        if not salary_mismatches.empty:
            print(f"[!] {len(salary_mismatches)} salary discrepancies detected:")
            print(salary_mismatches[['Employee_ID', 'Full_Name', 'Salary_payroll', 'Salary_benefits']].to_string(index=False))
        else:
            print("[+] All salaries match between payroll and benefits. ✓")
    else:
        print("    [*] Salary columns not found—skipping comparison.")

    # Summary
    print(f"\n{'='*60}")
    print("RECONCILIATION COMPLETE")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python payroll_reconciliation.py <payroll_csv> <benefits_csv>")
        print("Example: python payroll_reconciliation.py payroll.csv benefits.csv")
        sys.exit(1)
    
    reconcile_payroll(sys.argv[1], sys.argv[2])
