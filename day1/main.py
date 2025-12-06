import time


def profile(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")

    return wrapper


@profile
def main():
    # Read from file
    left: list[int] = []
    right: list[int] = []
    with open("input.txt", "r") as f:
        for line in f:
            first, second = map(int, line.split())
            left.append(first)
            right.append(second)
    left.sort()
    right.sort()

    sum = 0
    similarity = 0
    for first, second in zip(left, right):
        sum += abs(first - second)
        similarity += first * right.count(first)

    print(sum)
    print(similarity)


if __name__ == "__main__":
    main()
