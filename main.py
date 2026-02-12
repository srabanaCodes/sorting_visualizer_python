import tkinter as tk
import random
import time

WIDTH = 800
HEIGHT = 400

root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("900x700")

data = []

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack(pady=20)

speed_scale = tk.Scale(root, from_=0.01, to=0.3, resolution=0.01,
                       orient="horizontal", label="Speed", length=300)
speed_scale.set(0.05)
speed_scale.pack()


def draw_data(data, colors):
    canvas.delete("all")

    if len(data) == 0:
        return

    bar_width = WIDTH / len(data)

    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = HEIGHT - value
        x1 = (i + 1) * bar_width
        y1 = HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

    root.update()


def generate_data():
    global data
    data = [random.randint(20, HEIGHT - 20) for _ in range(60)]
    draw_data(data, ["white"] * len(data))


def bubble_sort():
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            colors = ["white"] * n
            colors[j] = "red"
            colors[j + 1] = "red"

            draw_data(data, colors)
            time.sleep(speed_scale.get())

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    draw_data(data, ["green"] * n)


def selection_sort():
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            colors = ["white"] * n
            colors[i] = "red"
            colors[j] = "yellow"
            colors[min_index] = "blue"

            draw_data(data, colors)
            time.sleep(speed_scale.get())

            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    draw_data(data, ["green"] * n)
def insertion_sort():
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]

            colors = ["white"] * n
            colors[j] = "red"
            colors[j + 1] = "yellow"

            draw_data(data, colors)
            time.sleep(speed_scale.get())

            j -= 1

        data[j + 1] = key

    draw_data(data, ["green"] * n)


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        colors = ["white"] * len(data)
        colors[k] = "red"
        draw_data(data, colors)
        time.sleep(speed_scale.get())

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort_recursive(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort_recursive(arr, left, mid)
        merge_sort_recursive(arr, mid + 1, right)

        merge(arr, left, mid, right)


def merge_sort():
    if len(data) <= 1:
        return

    merge_sort_recursive(data, 0, len(data) - 1)
    draw_data(data, ["green"] * len(data))


frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Generate Data", command=generate_data).pack(side="left", padx=5)
tk.Button(frame, text="Bubble Sort", command=bubble_sort).pack(side="left", padx=5)
tk.Button(frame, text="Selection Sort", command=selection_sort).pack(side="left", padx=5)
tk.Button(frame, text="Insertion Sort", command=insertion_sort).pack(side="left", padx=5)
tk.Button(frame, text="Merge Sort", command=merge_sort).pack(side="left", padx=5)

root.mainloop()
