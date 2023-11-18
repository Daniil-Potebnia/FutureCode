def find_nums(n):
    nums = []
    for i in range(1, 10):
        for j in range(10):
            for x in range(10):
                if i + j + x == n:
                    nums.append(i * 100 + j * 10 + x)
    return nums
