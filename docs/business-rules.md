# Business Rules — Sales Data Analysis

## 1. Purpose

The purpose of this project is to calculate total sales from a sales dataset and identify suspicious transactions.

The dataset contains the following fields:

- `customer_id`
- `product_id`
- `date`
- `quantity`
- `unit_price`
- `discount`
- `payment_status`

The business requirement is:

**Calculate total sales and identify suspicious transactions.**

Additional business rules must be clarified before the final calculations are implemented.

## 2. Known Requirements

The following requirements are explicitly provided:

1. Work with a sales dataset.
2. Calculate total sales.
3. Identify suspicious transactions.
4. Consider customer ID, product ID, date, quantity, unit price, discount, and payment status.
5. Document business rules before writing the analysis code.

The exact sales formula and definition of a suspicious transaction have not yet been specified.

## 3. Assumptions

The following are preliminary assumptions for planning. They must be confirmed before being treated as final business rules.

1. Quantity represents the number of units in a transaction.
2. Unit price represents the price of one unit before discount.
3. Discount is assumed to be a percentage between 0 and 100.
4. Normal sales should have a positive quantity and a non-negative unit price.
5. Missing required fields should be flagged for review.
6. Duplicate transactions should be investigated before being counted.
7. Cancelled transactions should not count as completed sales.
8. Only transactions confirmed as paid should count toward confirmed-paid sales.
9. Refunds should be represented separately or handled using an explicitly defined refund rule.
10. Unusual transactions should be flagged for investigation rather than automatically classified as fraud.

## 4. Questions Requiring Business Clarification

### Quantity and Price

- Can quantity be zero?
- Can quantity be negative to represent returns?
- Are fractional quantities allowed?
- Can unit price be zero for free products?
- Can unit price be negative?
- Is unit price recorded before or after discount?

### Discount

- Is discount stored as a percentage or a monetary amount?
- Is a 100% discount allowed?
- Can discounts exceed 100% under any special circumstance?
- Are discounts applied before or after taxes and other charges?

### Payment Status

- What payment statuses are valid?
- Can payment status be empty?
- Should pending transactions count toward sales?
- Should failed or cancelled payments count?
- How should partially paid orders be handled?

### Duplicate Transactions

- Is there a unique transaction ID or order ID?
- How should duplicate records be identified?
- Can the same customer buy the same product more than once on the same date?
- Should duplicate records be removed automatically or sent for review?

### Dates

- Are future-dated transactions permitted?
- What date format is expected?
- Which date should be used: order date, payment date, or shipment date?
- What reporting period should be used for total sales?

### Refunds and Cancellations

- How are refunds recorded?
- Do refunds reduce total sales?
- Are partial refunds supported?
- Should cancelled orders be excluded?
- How should returned products be represented?

### Suspicious Transactions

- What quantity should be considered unusually high?
- What transaction amount should trigger a review?
- Should repeated transactions within a short period be flagged?
- Should unusual prices or discounts be flagged?
- Should suspicious transactions be excluded from the sales total or reported separately?

## 5. Proposed Sales Calculation

If the discount is a percentage and the unit price is before discount:

Gross sales = Quantity × Unit Price

Discount amount = Gross Sales × Discount Percentage / 100

Net sales before taxes, fees, and refunds = Gross Sales − Discount Amount

The final total-sales calculation depends on the business decision about payment status, cancellations, refunds, taxes, and the reporting period.

## 6. Proposed Suspicious Transaction Categories

Transactions may be flagged for review when they contain:

- Missing required values
- Invalid dates
- Unexpected negative quantities or prices
- Discounts outside the permitted range
- Possible duplicate records
- Unusually high quantities or transaction amounts
- Unknown payment statuses
- Future dates that are not permitted
- Inconsistent refund or cancellation records

A suspicious flag indicates that a transaction needs investigation. It does not prove fraud.

## 7. Data Handling Principles

1. Do not silently delete invalid or suspicious records.
2. Keep the original dataset unchanged.
3. Record the reason for every flag or correction.
4. Separate invalid data from unusual but potentially valid transactions.
5. Document assumptions and obtain clarification before finalizing business calculations.
6. Report excluded transactions and explain why they were excluded.

## 8. Conclusion

The initial requirement is not sufficient to determine a single correct sales total.

Before implementation, the business must clarify the sales formula, valid payment statuses, refund and cancellation handling, duplicate identification, and suspicious transaction thresholds.

Once these rules are confirmed, they can be implemented and tested in Python using Pandas.