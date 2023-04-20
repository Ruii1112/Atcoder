def even_judge(a: int, b: int) -> bool:
    if a % 2 == 0 or b % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    if even_judge(a, b):
        print("Even")
    else:
        print("Odd")