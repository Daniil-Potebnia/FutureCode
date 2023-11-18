import random


def random_password(length, big_letters=True, spec_sym=True):
    password = ''
    for i in range(length):
        if not big_letters and not spec_sym:
            rand_sym = random.choice(list(random.choice([eng, ru, nums])))
        elif not big_letters:
            rand_sym = random.choice(list(random.choice([eng, ru, nums, sym])))
        elif not spec_sym:
            rand_sym = random.choice(list(random.choice([eng, ru, nums, ru_big, eng_big])))
        else:
            rand_sym = random.choice(list(random.choice([eng, ru, nums, ru_big, eng_big, sym])))
        password += rand_sym
    return password


eng = set('qwertyuioplkjhgfdsazxcvbnm')
eng_big = set('qwertyuioplkjhgfdsazxcvbnm'.upper())
ru = set('йцукенгшщзхъфывапролдячсмитьбю')
ru_big = set('йцукенгшщзхъфывапролдячсмитьбю'.upper())
sym = set('!@#$%^&*()_+}{":?><,./=-`~')
nums = set('11234567890')
all_sym = eng, eng_big, ru, ru_big, sym, nums
print(random_password(16))
