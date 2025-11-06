Example 1

1) mkdir merge-conflicts/
2) git init
3) stats.py
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return {"total": total, "mean": mean, "count": count}
4) add + commit

=======
1) git switch -c stddev
2) modify stats.py
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "count": count, "std_dev": std_dev}
3) add + commit
4) git switch main
5) stats.py
# main: stats.py
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    min_val = min(numbers)
    max_val = max(numbers)
    return {"total": total, "mean": mean, "count": count, "min": min_val, "max": max_val}
6) add + commit
7) git merge stddev
8) explain and resolve merge conflicts
9) add + commit
