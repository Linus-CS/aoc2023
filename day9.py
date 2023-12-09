def get_diff(nums):
    diffs = []
    for i in range(0, len(nums) - 1):
        diffs.append(nums[i + 1] - nums[i])
    return diffs


sum = 0
with open("input/day9.txt", "r+") as file:
    for line in file:
        nums = list(map(int, line.split(" ")))
        all_diffs = [nums.copy()]
        while nums[-1] != 0:
            nums = get_diff(nums)
            all_diffs.append(nums)

        for i in range(len(all_diffs) - 2, -1, -1):
            all_diffs[i].insert(0, all_diffs[i][0] - all_diffs[i + 1][0])
        sum += all_diffs[0][0]

print(sum)
