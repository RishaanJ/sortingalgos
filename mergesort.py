import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def merge_sort(arr, update_func):
    def merge_sort_rec(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort_rec(L)
            merge_sort_rec(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            update_func(arr)
            yield arr

    yield from merge_sort_rec(arr)


def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)


arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Merge Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)


def animate(frame):
    update_plot(frame)


ani = FuncAnimation(fig, animate, frames=merge_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
