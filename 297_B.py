def judge(s: str) -> bool:
    b_pos = []
    r_pos = []
    
    b_pos.append(s.find("B"))
    b_pos.append(s.rfind("B"))
    r_pos.append(s.find("R"))
    r_pos.append(s.rfind("R"))
    k_pos = s.find("K")

    if b_pos[0] % 2 == b_pos[1] % 2:
        return False
    if not (r_pos[0] < k_pos and k_pos < r_pos[1]):
        return False
    
    return True


if __name__ == "__main__":
    s = input()
    if judge(s):
        print("Yes")
    else:
        print("No")