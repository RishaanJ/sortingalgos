import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def bucket_sort(arr, update_func):
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key

    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(num * bucket_count / (max_val + 1))
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)
        update_func(sorted_arr)
        yield sorted_arr

def update_plot(arr):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(0.1)

arr = np.random.randint(1, 100, size=20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_title('Bucket Sort Visualization')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.ylim(0, max(arr) + 10)

def animate(frame):
    update_plot(frame)

ani = FuncAnimation(fig, animate, frames=bucket_sort(list(arr), update_plot), repeat=False, interval=100)
plt.show()
