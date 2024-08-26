import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def cocktail_shaker_sort(arr, update_func):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    start, end = 0, n - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)
                swapped = True
            update_func(arr)
            yield arr
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start - 1, -1):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)
                swapped = True
            update_func(arr)
            yield arr
        start += 1

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Cocktail Shaker Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=cocktail_shaker_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
