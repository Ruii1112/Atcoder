import time

def judge(a: int, b: int) -> int:
    cnt = 0
    while a != b:
        cnt += 1
        if a > b:
            a -= b
        else:
            b -= a
    
    return cnt

if __name__ == "__main__":
    start = time.time()
    a, b = map(int, input().split())
    print(judge(a,b))
    end = time.time()
    print(end - start)