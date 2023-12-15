import time
import random


def bubble(array):  # Даниил
    for i_ in range(len(array)-1):
        for j_ in range(len(array)-i_-1):
            if array[j_] > array[j_+1]:
                buff = array[j_]
                array[j_] = array[j_+1]
                array[j_+1] = buff


times = dict()
for i in range(2, 7):
    times[10 ** i] = []
    for j in range(5):
        with open(f'{10 ** i}.txt', mode='r') as f:
            data = list(map(int, f.read().split('\n')))
        start = time.time()
        bubble(data)
        end = time.time()
        times[10 ** i].append(end - start)
print(times)


def comb(array):  # Олеся
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = int(gap // 1.25)
        swaps = False
        for i in range(len(array) - gap):
            j = i + gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True


sizes = [100, 1000, 10000, 1000000]
for size in sizes:
    numbers = random.sample(range(size), size)
    start_time = time.time()
    comb(numbers)
    finish_time = time.time()
    print(finish_time - start_time)


def bystraya_sortirovka(spisok):  # Никита
    if len(spisok) <= 1:
        return spisok
    opora = spisok[len(spisok) // 2]
    levaya = [x for x in spisok if x < opora]
    srednyaya = [x for x in spisok if x == opora]
    pravaya = [x for x in spisok if x > opora]
    return bystraya_sortirovka(levaya) + srednyaya + bystraya_sortirovka(pravaya)

# Генерация списка случайных чисел указанного размера
def generirovat_sluchaynyy_spisok(razmer):
    return [random.randint(1, 1000) for _ in range(razmer)]

# Замер времени выполнения сортировки
def izmerit_vremya_sortirovki(spisok):
    nachalnoe_vremya = time.time()
    ototsortirovannyy_spisok = bystraya_sortirovka(spisok)
    konechnoe_vremya = time.time()
    return konechnoe_vremya - nachalnoe_vremya

# Размеры списков для сортировки
razmery = [100, 1000, 10000, 100000, 1000000]

# Выполнение сортировки и замер времени для каждого размера списка
for razmer in razmery:
    spisok = generirovat_sluchaynyy_spisok(razmer)
    vremya_sortirovki = izmerit_vremya_sortirovki(spisok)
    print(f"Размер списка: {razmer}, Время сортировки: {vremya_sortirovki} сек.")
