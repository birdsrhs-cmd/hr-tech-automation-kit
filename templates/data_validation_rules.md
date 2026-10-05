# Excel Data Validation Rules for HR

## Why Data Validation Matters
Poor data hygiene costs HR teams hours every week. Typos in department names, unformatted dates, and duplicate IDs cascade into payroll errors, compliance headaches, and audit failures.

Excel's Data Validation feature is your first line of defense—forcing users to input clean, consistent data from day one.

---

## Common HR Data Validation Rules

### 1. Department Names (Dropdown List)
**Problem:** Users type "HR", "Human Resources", "hr dept" inconsistently.  
**Solution:** Restrict input to a pre-approved list.

**Steps:**
1. Create a reference list on a separate sheet (e.g., Sheet2: Departments)
   ```
   HR
   IT
   Finance
   Operations
   Sales
   ```
2. Select the Department column (e.g., Column C).
3. Go to **Data → Data Validation**.
4. Settings:
   - Allow: **List**
   - Source: `=Departments!$A$1:$A$5`
5. Check **Show dropdown in cell**.
6. Error Alert: "Invalid department. Select from dropdown."

---

### 2. Employee ID Format (Custom Pattern)
**Problem:** IDs entered as "EMP001", "001", "emp-1" inconsistently.  
**Solution:** Enforce a pattern like `EMP0001`.

**Steps:**
1. Select Employee ID column.
2. Data Validation → Settings:
   - Allow: **Custom**
   - Formula: `=AND(LEN(A2)=7, LEFT(A2,3)="EMP", ISNUMBER(VALUE(MID(A2,4,4))))`
3. Error Alert: "Employee ID must follow format: EMP0001"

---

### 3. Email Address Format
**Problem:** Missing "@" symbol or malformed addresses.  
**Solution:** Validate email contains "@" and a domain.

**Steps:**
1. Select Email column.
2. Data Validation → Settings:
   - Allow: **Custom**
   - Formula: `=AND(ISNUMBER(FIND("@",D2)), ISNUMBER(FIND(".",D2)), LEN(D2)>5)`
3. Error Alert: "Invalid email format. Must contain @ and domain."

---

### 4. Date Format (Start Date / Hire Date)
**Problem:** Mixed formats ("01/15/2024", "Jan 15", "2024-01-15").  
**Solution:** Force dates to be valid and within a reasonable range.

**Steps:**
1. Select Start Date column.
2. Data Validation → Settings:
   - Allow: **Date**
   - Data: **between**
   - Start date: `01/01/2020`
   - End date: `12/31/2030`
3. Error Alert: "Invalid date. Use MM/DD/YYYY between 2020-2030."

---

### 5. Salary Range Validation
**Problem:** Accidentally typing 100000000 instead of 100000.  
**Solution:** Set realistic min/max bounds.

**Steps:**
1. Select Salary column.
2. Data Validation → Settings:
   - Allow: **Decimal**
   - Data: **between**
   - Minimum: `30000`
   - Maximum: `500000`
3. Error Alert: "Salary must be between $30,000 and $500,000."

---

### 6. Mandatory Fields (Cannot Be Blank)
**Problem:** Critical fields left empty (Employee ID, Full Name).  
**Solution:** Block submission if blank.

**Steps:**
1. Select mandatory column (e.g., Full Name).
2. Data Validation → Settings:
   - Allow: **Custom**
   - Formula: `=LEN(TRIM(B2))>0`
3. Error Alert: "This field is mandatory and cannot be left blank."

---

## Visual Indicators with Conditional Formatting

### Highlight Missing Values (Red Background)
1. Select data range (e.g., A2:F100).
2. **Home → Conditional Formatting → New Rule**.
3. Rule type: **Use a formula to determine which cells to format**.
4. Formula: `=ISBLANK(A2)` (adjust for each column).
5. Format: **Red fill, white text**.

### Highlight Duplicate Employee IDs
1. Select Employee ID column.
2. **Conditional Formatting → Highlight Cells Rules → Duplicate Values**.
3. Choose **Red fill** for duplicates.

---

## Testing Your Validation Rules

1. **Test invalid input:** Try entering "Marketing Dept" in the Department dropdown → Should be blocked.
2. **Test blank mandatory field:** Leave Full Name empty → Should show error alert.
3. **Test date out of range:** Enter "01/01/2015" → Should be rejected.
4. **Test duplicate ID:** Enter an existing Employee ID → Should highlight red.

---

## Next Steps
- Apply these rules to the `onboarding_tracker.xlsx` template.
- Train your HR team to recognize validation alerts.
- Review rejected data monthly to identify common input errors.

---

**Questions?** This guide is part of the HR Tech Automation Kit. Check the main README for contact details.
