import time
import matplotlib.pyplot as plt

def tablice():
    number = [100, 1000, 10000, 100000, 1000000]
    normal_times = []
    comprehension_times = []

    for i in number:
        numbers = list(range(1, i))

        start = time.time()
        tab = []
        for num in numbers:
            if num % 2 == 0:
                tab.append(num ** 2)
        end = time.time()
        normal_times.append(end - start)

        start1 = time.time()
        tab1 = [num ** 2 for num in numbers if num % 2 == 0]
        end1 = time.time()
        comprehension_times.append(end1 - start1)

        if tab == tab1:
            print("Both are equal")
        else:
            print("Both are not equal")

    return number, normal_times, comprehension_times

def slowniki():
    number = [100, 1000, 10000, 100000, 1000000]
    normal_times = []
    comprehension_times = []

    for i in number:
        numbers = list(range(1, i))

        start = time.time()
        tab = {}
        for num in numbers:
            if num % 2 == 0:
                tab[num] = num ** 2
        end = time.time()
        normal_times.append(end - start)

        start1 = time.time()
        tab1 = {num: num ** 2 for num in numbers if num % 2 == 0}
        end1 = time.time()
        comprehension_times.append(end1 - start1)

        if tab == tab1:
            print("Both are equal")
        else:
            print("Both are not equal")

    return number, normal_times, comprehension_times

number1, normal_times1, comprehension_times1 = tablice()
number2, normal_times2, comprehension_times2 = slowniki()

fig, ax = plt.subplots()
ax.plot(number1, normal_times1, label="Tablice normal", color='orange')
ax.plot(number1, comprehension_times1,'r--', label="Tablice comprehension", color='orange')
ax.plot(number2, normal_times2,label="Slowniki normal", color='blue')
ax.plot(number2, comprehension_times2,'r--', label="Slowniki comprehension", color='blue')
ax.set_xlabel('Number of elements')
ax.set_ylabel('Time (seconds)')
ax.legend()
plt.show()