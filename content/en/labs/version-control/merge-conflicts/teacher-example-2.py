Example 2 (continues from Example 1)

1) git switch main
2) create app.py
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))
3) add + commit

-----
1) git switch -c mode
2) Rename app.py -> main.py
3) main.py
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))

    numbers = [8, 9, 10, 10, 20]
    print(stats.calculate_stats(numbers))
4) stats.py
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    min_val = min(numbers)
    max_val = max(numbers)
    mode = max(numbers, key=numbers.count)
    median = sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 != 0 else (sorted(numbers)[len(numbers) // 2 - 1] + sorted(numbers)[len(numbers) // 2]) / 2

    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "median": median, "mode": mode, "count": count, "min": min_val, "max": max_val, "std_dev": std_dev}
5) add + commit
----
6) git checkout main
7) stats.py
import math

def calculate_stats(numbers):
    count = len(numbers)
    mean = sum(numbers) / count
    
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"mean": mean, "std_dev": std_dev}
8) app.py
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))

    numbers = [2, 2, 2]
    print(stats.calculate_stats(numbers))
9) add + commit
10) git merge mode

