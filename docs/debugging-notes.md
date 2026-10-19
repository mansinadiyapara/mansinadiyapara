# Debugging Notes — Incorrect Sales Total

## 1. What I Observed

The application completed its data-processing pipeline and exported a report, but the reported sales total was higher than the expected total.

The program performed these operations:

1. Loaded source data.
2. Cleaned the data.
3. Merged datasets.
4. Calculated sales totals.
5. Exported the report.

The report was generated successfully, but the result was incorrect.

## 2. What I Suspected

I considered the following possible causes:

- Incorrect values in the source data.
- Duplicate transactions.
- Missing records during cleaning.
- Duplicate keys in a dataset used for merging.
- Incorrect aggregation or sales formula.
- Incorrect numeric type conversion.
- Incorrect payment-status filtering.
- Incorrect report export.

At this stage, these were possible explanations, not confirmed causes.

## 3. What I Investigated

### Source Data

I checked the source files for missing values, duplicate transaction IDs, invalid numeric values, and unexpected data types.

### Cleaning Stage

I compared row counts and important column values before and after cleaning.

I checked whether any records had been changed, excluded, or converted to missing values.

### Merge Stage

I checked the uniqueness of customer IDs in the customer dataset and compared row counts before and after merging.

I also checked whether the merge created repeated transaction IDs.

### Aggregation Stage

I verified the sales formula and confirmed which payment statuses and transaction types should contribute to the total.

### Export Stage

I compared the exported report with the validated in-memory result.

## 4. Evidence

Example evidence from a hypothetical investigation:

| Check | Result |
|---|---:|
| Sales rows before merge | 2 |
| Sales total before merge | ₹1,500 |
| Customer rows for C101 | 2 |
| Rows after merge | 3 |
| Sales total after merge | ₹2,500 |

These results indicate that the sales total increased during the merge.

The duplicate customer ID caused one sales transaction to match two customer records.

**Note:** These are illustrative values. Replace them with actual measurements from your own application.

## 5. Root Cause

The customer dataset contained duplicate customer IDs, even though the merge logic expected each customer ID to identify a single customer record.

The merge therefore duplicated a sales transaction. The subsequent aggregation counted the repeated transaction more than once.

The sales formula itself was not the root cause.

## 6. Fix

I added merge validation using Pandas:

`validate="many_to_one"`

This checks that the customer dataset has no more than one matching row per customer ID.

I also added an investigation step for duplicate customer IDs.

Duplicate records must be resolved using an appropriate business rule before the data is used for reporting.

## 7. Test Added to Prevent Recurrence

I added a test to verify that duplicate customer keys are detected and that the application rejects an invalid merge instead of generating a misleading sales total.

The test should also verify that a valid merge preserves the expected sales total.

## 8. Conclusion

The incorrect total was caused by duplicated records introduced during the merge, not by the final calculation.

The investigation compared intermediate results, identified the first stage where the data became incorrect, and addressed the underlying cause.

Future tests will help detect similar problems before a report is generated.