"""
Employee Roster Data Audit Tool
Author: Cataleya | HR Tech Specialist
Description: Scans an employee master CSV export for missing mandatory fields,
duplicate IDs, and format mismatches. Generates a detailed compliance report.
"""

import pandas as pd
import sys
from datetime import datetime

def audit_roster(file_path):
    """
    Main audit function. Loads CSV and runs comprehensive data quality checks.
    """
    print(f"\n{'='*60}")
    print(f"HR ROSTER AUDIT REPORT | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Load file
    print(f"[*] Loading roster from: {file_path}")
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"[!] ERROR: Cannot load file. {e}")
        sys.exit(1)

    # Define mandatory columns for HR compliance
    mandatory_cols = ['Employee_ID', 'Full_Name', 'Department', 'Email', 'Start_Date']
    
    # Check 1: Verify all mandatory columns exist
    missing_cols = [col for col in mandatory_cols if col not in df.columns]
    if missing_cols:
        print(f"[!] CRITICAL ERROR: Missing mandatory columns: {missing_cols}")
        print(f"    Expected columns: {mandatory_cols}")
        sys.exit(1)
    
    print(f"[+] Total records in roster: {len(df)}")
    print(f"[+] Total columns: {len(df.columns)}\n")

    # Check 2: Missing values in mandatory fields
    print("--- MISSING DATA AUDIT ---")
    missing_data = df[mandatory_cols].isnull().sum()
    if missing_data.sum() > 0:
        print(f"[!] {missing_data.sum()} missing values found:")
        for col in mandatory_cols:
            if missing_data[col] > 0:
                print(f"    • {col}: {missing_data[col]} records")
    else:
        print("[+] No missing values in mandatory fields. ✓")

    # Check 3: Duplicate Employee IDs
    print("\n--- DUPLICATE ID AUDIT ---")
    duplicates = df[df.duplicated(subset=['Employee_ID'], keep=False)].sort_values('Employee_ID')
    if not duplicates.empty:
        print(f"[!] {len(duplicates)} duplicate Employee ID records found:")
        print(duplicates[['Employee_ID', 'Full_Name', 'Department']].to_string(index=False))
    else:
        print("[+] No duplicate Employee IDs detected. ✓")

    # Check 4: Email format validation
    print("\n--- EMAIL FORMAT AUDIT ---")
    invalid_emails = df[~df['Email'].str.contains('@', na=False, regex=False)]
    if not invalid_emails.empty:
        print(f"[!] {len(invalid_emails)} records with invalid email format:")
        print(invalid_emails[['Employee_ID', 'Full_Name', 'Email']].to_string(index=False))
    else:
        print("[+] All email addresses contain '@' symbol. ✓")

    # Check 5: Data completeness score
    print("\n--- OVERALL DATA QUALITY SCORE ---")
    total_cells = len(df) * len(mandatory_cols)
    missing_cells = df[mandatory_cols].isnull().sum().sum()
    accuracy_rate = ((total_cells - missing_cells) / total_cells) * 100
    print(f"[+] Completeness: {accuracy_rate:.2f}%")
    
    if accuracy_rate >= 99:
        print("    Status: EXCELLENT ✓✓✓")
    elif accuracy_rate >= 95:
        print("    Status: GOOD ✓✓")
    elif accuracy_rate >= 90:
        print("    Status: ACCEPTABLE ✓")
    else:
        print("    Status: NEEDS ATTENTION ⚠️")

    # Summary
    print(f"\n{'='*60}")
    print(f"AUDIT COMPLETE | Recommendations:")
    print(f"{'='*60}")
    if missing_data.sum() > 0 or not duplicates.empty or not invalid_emails.empty:
        print("[!] Action items detected. Review errors above and remediate.")
    else:
        print("[+] Roster is clean and audit-ready!")
    print(f"\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python employee_roster_audit.py <path_to_csv>")
        print("Example: python employee_roster_audit.py employee_data.csv")
        sys.exit(1)
    
    audit_roster(sys.argv[1])
