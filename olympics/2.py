nums = input()
nums_str = []
result = ""
for num in nums:
    nums_str.append(str(num))
nums_str_sorted = sorted(nums_str, reverse=True)
for i in range(len(nums_str_sorted) - 1):
    if nums_str_sorted[i]+nums_str_sorted[i+1] < nums_str_sorted[i+1]+nums_str_sorted[i]:
        nums_str_sorted[i], nums_str_sorted[i+1] = nums_str_sorted[i+1], nums_str_sorted[i]
for num in nums_str_sorted:
    result += num

print(result)
