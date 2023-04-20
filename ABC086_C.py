def judge(n: int, x: list) -> bool:
    pre_t = 0
    pre_x = 0
    pre_y = 0

    for i in range(n):
        d = abs(x[i][1] - pre_x) + abs(x[i][2] - pre_y)
        t = x[i][0] - pre_t

        if t < d or (t - d) % 2 == 1:
            return False
        else:
            pre_t = x[i][0]
            pre_x = x[i][1]
            pre_y = x[i][2]
    
    return True


if __name__ == "__main__":
    n = int(input())
    x = []

    for i in range(n):
        x.append(list(map(int, input().split())))

    if judge(n, x):
        print("Yes")
    else:
        print("No")