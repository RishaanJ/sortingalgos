import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def quick_sort(arr, update_func):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            update_func(arr)
            yield arr
            yield from quick_sort_rec(low, pi - 1)
            yield from quick_sort_rec(pi + 1, high)

    yield from quick_sort_rec(0, len(arr) - 1)

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Quick Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=quick_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
