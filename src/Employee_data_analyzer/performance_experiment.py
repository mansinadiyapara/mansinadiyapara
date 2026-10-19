import time
import numpy as np
import pandas as pd


def python_calculation(quantities, prices, discounts):
    """Calculate total sales using a Python loop."""
    total = 0.0

    for quantity, price, discount in zip(quantities, prices, discounts):
        gross = quantity * price
        net = gross - (gross * discount / 100)
        total += net

    return total


def numpy_calculation(quantities, prices, discounts):
    """Calculate total sales using NumPy vectorization."""
    net_sales = (quantities * prices * (1 - discounts / 100))

    return net_sales.sum()


def benchmark(size):
    print(f"\nTesting {size:,} records...")

    
    rng = np.random.default_rng(42)

    quantities = rng.integers(1, 11, size=size, dtype=np.int32)
    prices = rng.uniform(100, 5000, size=size).astype(np.float64)
    discounts = rng.uniform(0, 30, size=size).astype(np.float64)

    start = time.perf_counter()
    python_total = python_calculation( quantities, prices, discounts )
    python_time = time.perf_counter() - start

    start = time.perf_counter()
    numpy_total = numpy_calculation( quantities, prices, discounts )
    numpy_time = time.perf_counter() - start

    results_match = np.isclose(python_total, numpy_total, rtol=1e-9, atol=1e-6)

    input_memory = (
        quantities.nbytes
        + prices.nbytes
        + discounts.nbytes
    )

    print(f"Python total:       {python_total:.2f}")
    print(f"NumPy total:        {numpy_total:.2f}")
    print(f"Python time:        {python_time:.4f} seconds")
    print(f"NumPy time:         {numpy_time:.4f} seconds")
    print(f"Input array memory: {input_memory / (1024**2):.2f} MB")
    print(f"Results match:      {results_match}")

    return {
        "records": size,
        "python_seconds": python_time,
        "numpy_seconds": numpy_time,
        "input_memory_mb": input_memory / (1024**2),
        "results_match": results_match,
    }


def main():
    sizes = [
        10_000,
        100_000,
        1_000_000,
        5_000_000,
    ]

    results = []

    for size in sizes:
        try:
            results.append(benchmark(size))
        except MemoryError:
            print(f"Not enough memory for {size:,} records.")
            break

    if results:
        report = pd.DataFrame(results)
        report.to_csv(
            "data/performance_results.csv", index=False
        )

        print("\nPerformance Summary:")
        print(report.to_string(index=False))
        print("\nSaved results to performance_results.csv")


if __name__ == "__main__":
    main()
