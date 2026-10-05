# HR Automation Workflow Guide

## Overview
This guide walks you through using the scripts and templates in this kit to establish bulletproof HR data management processes.

---

## Workflow 1: Monthly Employee Roster Audit

### Goal
Ensure your employee master file is clean, compliant, and audit-ready.

### Steps

1. **Export your employee roster** from your HRIS (ADP, BambooHR, etc.) as CSV.
   - Columns needed: Employee_ID, Full_Name, Department, Email, Start_Date

2. **Run the audit script:**
   ```bash
   python scripts/employee_roster_audit.py your_roster.csv
   ```

3. **Review the output:**
   - ✓ If accuracy > 99%: Your data is audit-ready.
   - ⚠️ If accuracy < 95%: Fix identified issues before payroll or benefits processing.

4. **Remediate issues:**
   - Use your HR system's data validation or Excel Data Validation (see templates) to fix duplicates, missing fields, and format errors.

5. **Re-run audit** after fixes to confirm 100% compliance.

---

## Workflow 2: Quarterly Payroll & Benefits Reconciliation

### Goal
Catch enrollment gaps, salary mismatches, and orphaned records before they cause compliance issues.

### Steps

1. **Export two files:**
   - **Payroll export** (from your payroll provider): employee_id, name, department, salary
   - **Benefits export** (from your benefits admin): employee_id, name, enrolled_plans

2. **Run reconciliation script:**
   ```bash
   python scripts/payroll_reconciliation.py payroll.csv benefits.csv
   ```

3. **Review discrepancies:**
   - Are all payroll employees enrolled in benefits?
   - Do salaries match between systems?
   - Are there orphaned benefits enrollments?

4. **Action plan:**
   - Create ticket(s) for any mismatches.
   - Ensure benefits team and payroll team are aligned.

---

## Workflow 3: New Hire Onboarding Tracking

### Goal
Ensure no new hire falls through the cracks during their first 30 days.

### Steps

1. **Open the template:** `templates/onboarding_tracker.xlsx`

2. **Add new hire information:**
   - Name, Department, Start Date, Manager Name
   - Automatically generates a 10-task checklist (Contract, IT Setup, Direct Deposit, etc.)

3. **Assign tasks** to respective teams (HR, IT, Finance, Manager).

4. **Update status** as tasks complete:
   - Red = Not Started
   - Yellow = In Progress
   - Green = Complete

5. **Use conditional formatting** to highlight overdue tasks at a glance.

---

## Data Validation Best Practices

### In Excel
- **Dropdowns for Department:** Prevents typos and ensures consistency.
- **Date format validation:** Ensures all dates are YYYY-MM-DD format.
- **Mandatory fields:** Cells marked red if employee_id or email is blank.

### Using Python
- Run the audit script monthly to catch errors programmatically.
- Export results to a shared dashboard or Slack notification.

---

## Troubleshooting

**Q: Script says "CSV file not found"**  
A: Ensure the file path is correct. Use full path: `C:\Users\yourname\Documents\payroll.csv`

**Q: Getting unexpected column errors?**  
A: Check that your CSV has the exact column names: `Employee_ID`, `Full_Name`, etc. (case-sensitive).

**Q: How do I automate this monthly?**  
A: Use Windows Task Scheduler or a cron job (Linux/Mac) to run the script on the 1st of each month.

---

## Next Steps
1. Customize these templates to match your company's onboarding process.
2. Integrate scripts into your existing HR workflow or dashboard.
3. Train your HR team on using these tools for consistent data hygiene.

---

**Questions?** Reach out on LinkedIn or check the main README for contact details.
