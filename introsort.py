import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import heapq

def introsort(arr, update_func):
    def introsort_rec(arr, start, end, depth_limit):
        if end - start <= 16:
            insertion_sort(arr, start, end)
        elif depth_limit == 0:
            heap_sort(arr, start, end)
        else:
            pivot = partition(arr, start, end)
            introsort_rec(arr, start, pivot - 1, depth_limit - 1)
            introsort_rec(arr, pivot + 1, end, depth_limit - 1)
        update_func(arr)
        yield arr

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def heap_sort(arr, start, end):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = end - start + 1
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr[start:end+1], n, i)
        for i in range(n - 1, 0, -1):
            arr[start], arr[start + i] = arr[start + i], arr[start]
            heapify(arr[start:end+1], i, 0)

    depth_limit = 2 * int(np.log2(len(arr)))
    yield from introsort_rec(arr, 0, len(arr) - 1, depth_limit)

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('IntroSort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=introsort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
