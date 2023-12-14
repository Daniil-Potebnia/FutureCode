import time


def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff


times = dict()
for i in range(2, 7):
    times[10 ** i] = []
    for j in range(15):
        with open(f'{10 ** i}.txt', mode='r') as f:
            data = list(map(int, f.read().split('\n')))
        start = time.time()
        bubble(data)
        end = time.time()
        times[10 ** i].append(end - start)
print(times)
