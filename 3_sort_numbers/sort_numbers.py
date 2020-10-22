nums = [0, 0, 0]
for i in range(0, 3):
    nums[i] = int(input(f"Ingrese número {i+1}: "))

nums.sort(reverse=True)
print(nums)