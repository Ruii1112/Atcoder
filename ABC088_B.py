def game(nums: list) -> int:
    nums.sort(reverse=True)
    return sum(nums[0::2]) - sum(nums[1::2])

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))
    print(game(nums))
    