import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def bubble_sort(arr, update_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                update_func(arr)
                yield arr  


def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()  
    plt.pause(0.05)  


arr = np.random.randint(1, 100, size=20)

fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')

ax.set_title('Bubble Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)


def animate(frame):
    update_plot(frame)


ani = FuncAnimation(fig, animate, frames=bubble_sort(arr, update_plot), repeat=False,
                    interval=2)  

plt.show()
