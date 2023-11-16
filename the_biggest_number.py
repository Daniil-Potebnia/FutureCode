def nums(data):
    res = []
    while data > 0:
        res.append(data % 10)
        data //= 10
    res.reverse()
    return res


def find_bigger(a, b):
    new_a = nums(a)
    new_b = nums(b)
    for i in range(len(min(new_b, new_a))):
        if new_b[i] > new_a[i]:
            return False
        if new_a[i] > new_b[i]:
            return True


def sort_nums(inventory):
    for i in range(len(inventory) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if find_bigger(inventory[i], inventory[j]):
                inventory[i], inventory[j] = inventory[j], inventory[i]
    return inventory


def create_one_num(mas):
    one_num = 0
    for i in mas:
        one_num *= 10 ** len(nums(i))
        one_num += i
    return one_num


numbers = [56, 9, 11, 2]
print(create_one_num(sort_nums(numbers)))
