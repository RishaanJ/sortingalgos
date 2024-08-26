import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def tim_sort(arr, update_func):
    RUN = 32
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        update_func(arr)
        yield arr

    def merge(arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = arr[l:l + len1], arr[m + 1:m + 1 + len2]
        i = j = k = 0
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len2:
            arr[k] = right[j]
            j += 1
            k += 1
        update_func(arr)
        yield arr

    def tim_sort_rec(arr, l, r):
        for i in range(l, r + 1, RUN):
            insertion_sort(arr, i, min((i + RUN - 1), r))
        size = RUN
        while size < r - l + 1:
            for start in range(l, r, 2 * size):
                mid = min(start + size - 1, r)
                end = min(start + 2 * size - 1, r)
                if mid < end:
                    yield from merge(arr, start, mid, end)
            size *= 2

    yield from tim_sort_rec(arr, 0, len(arr) - 1)

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Tim Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=tim_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
