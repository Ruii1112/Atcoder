def marbles(nums: list) -> int:
    return sum(nums)

if __name__ == "__main__":
    s = list(map(int, input()))
    print(marbles(s))