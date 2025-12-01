import time
import csv
from word_count import word_count

def benchmark_word_count(filename, repetitions=5):
    """Benchmark word_count function and return average time."""
    times = []
    for _ in range(repetitions):
        start_time = time.time()
        word_count(filename)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

sizes = [1, 5, 10, 20, 50]
results = []

for size in sizes:
    filename = f'corpus_{size}MB.txt'
    times = benchmark_word_count(filename)
    avg_time = sum(times) / len(times)
    row = [size] + times + [avg_time]
    results.append(row)
    print(f'Size {size}MB: Times {times}, Avg {avg_time:.4f}s')

with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Size_MB', 'Time1', 'Time2', 'Time3', 'Time4', 'Time5', 'Average'])
    writer.writerows(results)

print('Results saved to results.csv')
