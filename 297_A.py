def judge(n: int, d: int, t: list) -> int:
    for i in range(n - 1):
        if t[i + 1] - t[i] <= d:
            return t[i + 1]
    
    return -1

if __name__ == "__main__":
    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    print(judge(n, d, t))