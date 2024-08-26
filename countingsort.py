import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def counting_sort(arr, update_func):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for num, cnt in enumerate(count):
        sorted_arr.extend([num] * cnt)
        update_func(sorted_arr)
        yield sorted_arr

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(0, 50, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Counting Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=counting_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
