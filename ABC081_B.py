def shift(nums: list) -> bool:
    if all(x % 2 == 0 for x in nums):
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    count = 0
    while(shift(nums)):
        count += 1
        nums = [x // 2 for x in nums]
    print(count)