def judge(h: int, w: int, s: list) -> None:
    for i in range(h):
        lst = list(s[i])
        for j in range(w - 1):
            if lst[j] == "T" and lst[j + 1] == "T":
                lst[j] = "P"
                lst[j + 1] = "C"
        s[i] = "".join(lst)                
    
    for a in s:
        print(a)


if __name__ == "__main__":
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())

    judge(h, w, s)

    