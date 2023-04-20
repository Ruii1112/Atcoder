def judge(n: int, y: int) -> bool:
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if y == 10000 * i + 5000 * j + 1000 * k:
                print(f"{i} {j} {k}")
                return True
    return False

if __name__ == "__main__":
    n, y = map(int, input().split())
    if not (judge(n, y)):
        print(-1, -1, -1)