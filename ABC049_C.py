def judge(s: str) -> bool:
    # "dream", "dreamer", "erase", "eraser"
    s = s.replace("eraser", "")
    s = s.replace("erase", "")
    s = s.replace("dreamer", "")
    s = s.replace("dream", "")

    if s :
        return False
    else:
        return True

if __name__ == "__main__":
    s = input()
    if judge(s):
        print("YES")
    else:
        print("NO")