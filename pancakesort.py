import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def flip(arr, k):
    arr[:k+1] = arr[:k+1][::-1]

def pancake_sort(arr, update_func):
    def find_max_index(arr, n):
        return arr.index(max(arr[:n]))

    n = len(arr)
    for size in range(n, 1, -1):
        max_index = find_max_index(arr, size)
        if max_index != size - 1:
            if max_index != 0:
                flip(arr, max_index)
                update_func(arr)
                yield arr
            flip(arr, size - 1)
            update_func(arr)
            yield arr

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Pancake Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=pancake_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
