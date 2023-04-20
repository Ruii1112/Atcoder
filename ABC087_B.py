def coins(a: int, b: int, c: int, x: int) -> int:
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                y = 500 * i + 100 * j + 50 * k
                if y == x :
                    ans += 1
    return ans

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    print(coins(a, b, c, x))