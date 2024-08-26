import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time
import threading

def sleep_sort(arr, update_func):
    def sleep(num):
        time.sleep(num / 1000.0)
        sorted_arr.append(num)
        update_func(sorted_arr)
        yield sorted_arr

    sorted_arr = []
    threads = [threading.Thread(target=lambda: sleep(num)) for num in arr]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Sleep Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=sleep_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
