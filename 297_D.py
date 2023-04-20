import time

def judge(a: int, b: int) -> int:
    cnt = 0
    while a != b:
        if a > b:
            if a % b == 0:
                tmp = a // b
                cnt += tmp - 1
                break
            else:
                tmp = a // b
                cnt += tmp
                a -= b * tmp
        else:
            if b % a == 0:
                tmp = b // a
                cnt += tmp - 1
                break
            else:
                tmp = b // a
                cnt += tmp
                b -= a * tmp
    
    return cnt

if __name__ == "__main__":
    start = time.time()
    a, b = map(int, input().split())
    print(judge(a,b))
    end = time.time()
    print(end - start)