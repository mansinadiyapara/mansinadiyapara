# Memory Challenge — Large CSV Processing

## 1. Problem Statement

A CSV dataset may be larger than the available system memory. Loading the entire file into a Pandas DataFrame can cause high memory consumption, slow execution, or a `MemoryError`.

The objective is to identify a suitable method for processing large datasets without requiring the entire dataset to be loaded into memory at once.

## 2. Approaches Investigated

### Reading Only Required Columns

Pandas supports the `usecols` parameter in `read_csv()`. It loads only the columns needed for the task.

This reduces unnecessary data loading but may not be sufficient when the selected columns are themselves very large.

### Reducing Data Types

Appropriate numeric types and categorical representations can reduce memory usage. Data types must be chosen carefully to preserve valid values and required precision.

### Chunk Processing

Pandas supports the `chunksize` parameter in `read_csv()`. It returns an iterable that provides the CSV in smaller DataFrame batches.

This avoids loading the entire dataset into a single DataFrame.

### Incremental Processing

Each chunk can be processed independently, and its partial result can be combined with a running result.

This is suitable for calculations such as sums and counts, provided the business rules and aggregation logic are applied consistently.

### Streaming-Style Processing

Streaming processes records or batches sequentially instead of retaining the entire dataset. It can be useful for large files or continuously arriving data.

Some operations, such as global sorting and cross-record duplicate detection, may require additional storage or processing.

### Alternative Tools

Pandas is suitable when the data fits into available memory or can be processed in chunks.

DuckDB may be useful for SQL-based analytical queries over large files. Dask may be useful for larger parallel or distributed DataFrame workloads.

The choice depends on the operation, available resources, and complexity of the task.

## 3. Selected Approach

**Selected approach: Pandas chunk processing with incremental aggregation.**

The implementation reads only the required sales columns and processes a fixed number of records at a time.

For each chunk, it validates the required numeric values, calculates net sales for eligible records, and adds the chunk's subtotal to a running total.

## 4. Reason for the Choice

1. The task is a sales-total calculation that can be expressed as an aggregation of partial totals.
2. Only three columns are required for the initial calculation.
3. The entire CSV does not need to be stored in a single DataFrame.
4. Pandas is already part of the project, so no additional framework is initially required.
5. The chunk size can be adjusted according to measured memory usage and execution time.

## 5. Limitations and Risks

- The chosen chunk size may still consume too much memory on some systems.
- The calculation requires confirmed rules for refunds, cancellations, discounts, and payment status.
- Invalid records should be reported rather than silently discarded.
- Detecting duplicates across different chunks requires additional logic or storage.
- Incremental sums work well for additive totals, but not every analysis can be combined using a simple running total.
- The final result must be checked for correctness against a smaller dataset whose expected answer is known.

## 6. Validation Plan

1. Test the implementation on a small dataset.
2. Compare its result with a calculation performed on the same dataset loaded completely into memory.
3. Confirm that both methods follow the same business rules.
4. Increase the dataset size gradually.
5. Measure execution time and memory usage where practical.
6. Adjust the chunk size if memory consumption is excessive.
7. Record invalid records and explain how they are handled.

## 7. Conclusion

Pandas chunk processing with incremental aggregation is a reasonable initial approach for calculating sales totals from a CSV that is too large to load all at once.

The decision is based on the nature of the calculation, the ability to process records in batches, and the existing project tools.

The approach should be validated with actual data and measurements. If the requirements become more complex or performance remains insufficient, alternatives such as DuckDB or Dask can be evaluated.