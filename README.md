# HR Tech Automation Kit 🚀

**Author:** Cataleya | HR Tech Specialist  
**Purpose:** Open-source templates, scripts, and documentation for streamlining HR operations, data validation, and employee record management.

---

## What's Inside

### 📊 **Scripts** (`scripts/`)
Python utilities for automating HR data audits and reconciliation:
- **`employee_roster_audit.py`** — Detect duplicate IDs, missing mandatory fields, and format errors in employee master files.
- **`payroll_reconciliation.py`** — Cross-reference payroll CSV exports against benefits/tax registries to catch discrepancies.

### 📑 **Templates** (`templates/`)
Production-ready Excel/CSV templates with built-in validation:
- **`onboarding_tracker.xlsx`** — Automated new-hire onboarding checklist with status tracking and document verification.
- **`data_validation_rules.md`** — Step-by-step guide to set up Excel Data Validation, conditional formatting, and error alerts.

### 📖 **Documentation** (`docs/`)
Standard Operating Procedures (SOPs) for HR data management:
- **`workflow_guide.md`** — How to use these scripts and templates in a real HR workflow.

---

## Quick Start

### Running the Audit Script
```bash
python scripts/employee_roster_audit.py path/to/employee_data.csv
```

Output: Summary of missing values, duplicate IDs, and overall data quality score.

### Using the Onboarding Template
1. Open `templates/onboarding_tracker.xlsx` in Excel or Google Sheets.
2. Add new hire details (Name, Department, Start Date).
3. Status dropdowns auto-populate; conditional formatting highlights overdue tasks.

---

## Who This Is For
- **HR Managers & Team Leads** building systems for growing remote teams.
- **Freelance HR Specialists** managing client data audits and compliance projects.
- **Startups** scaling hiring and needing bulletproof record management.

---

## Contributions
Have a template or script to share? PRs welcome. This kit is a living resource for the HR tech community.

---

## License
MIT License — Use freely for personal and commercial projects.

---

**Questions?** Connect with me on LinkedIn: [Your LinkedIn URL]  
**Need custom HR automation?** Reach out for freelance projects: [Upwork/Portfolio Link]
