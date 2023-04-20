def sums(n: int, a: int, b: int) -> int:
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        x = 0
        for j in s:
            x += int(j)
        if x >= a and x <= b:
            ans += i
    
    return ans

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    print(sums(n, a, b))