from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort


# Main window 
window = Tk()
window.title("Visualization & Comparison of Sorting Algorithms")
window.maxsize(2000, 1400)
window.config(bg = WHITE)


speed_name = StringVar()
data = []
#['Quick Sort','Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort','Heap Sort']
speed_list = ['Fast', 'Medium', 'Slow']


#Generating the numerical array as bars after the sorting
def drawData(data, colorArray, Identity):
        if Identity==1:
            canvas1.delete("all")
        if Identity==2:
            canvas2.delete("all")
        if Identity==3:
            canvas3.delete("all")
        if Identity==4:
            canvas4.delete("all")
        if Identity==5:
            canvas5.delete("all")
        if Identity==6:
            canvas6.delete("all")
        
        canvas_width = 400
        canvas_height = 200
        x_width = canvas_width / (len(data) + 1)
        offset = 4
        spacing = 2
        normalizedData = [i / max(data) for i in data]

        if Identity==1:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas1.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        elif Identity==2:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        elif Identity==3:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas3.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        elif Identity==4:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas4.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        elif Identity==5:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas5.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        elif Identity==6:
            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 190
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas6.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        window.update_idletasks()

# Genrating Random array as bars
def GenerateData(data, colorArray):
        #Creating 6 Frames and Set all attributes
        canvas1.delete("all")
        canvas2.delete("all")
        canvas3.delete("all")
        canvas4.delete("all")
        canvas5.delete("all")
        canvas6.delete("all")
        
        canvas_width = 400
        canvas_height = 200
        x_width = canvas_width / (len(data) + 1)
        offset = 4
        spacing = 2
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 190
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            canvas1.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas3.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas4.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas5.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas6.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

        window.update_idletasks()


#Randomly generate array numbers
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    GenerateData(data, [BLACK for x in range(len(data))])

def generate2(Identity):
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLACK for x in range(len(data))],Identity)

#Speed variations
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.03
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0.001


def sort():
    global data 
    timeTick = set_speed()

    #Set a frame for a particular sorting 
    #Frame 1
    quick_sort(data, 0, len(data)-1, drawData, timeTick)
    generate2(3)

    #Frame 3
    insertion_sort(data, drawData, timeTick)
    generate2(5)
    
    #Frame 5
    merge_sort(data, 0, len(data)-1, drawData, timeTick)
    generate2(4)

    #Frame 4
    selection_sort(data, drawData, timeTick)
    generate2(6)

    #Frame 6
    heap_sort(data, drawData, timeTick)
    generate2(2)

    #Frame 2
    bubble_sort(data, drawData, timeTick)

#User interface
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Speed Block
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#First frame top-left (Quick Sort)
canvas1 = Canvas(window, width=400, height=200, bg=WHITE)
canvas1.grid(row=1, column=0, padx=10, pady=5)
canvas1.place(x = 30, y = 130)
label = ttk.Label(window, text="Quick Sort")
label.place(x=200, y=350)

#Second frame Bottom-left (Bubble Sort)
canvas2 = Canvas(window, width=400, height=200, bg=WHITE)
canvas2.grid(row=1, column=0, padx=10, pady=5)
canvas2.place(x = 30, y = 400)  
label = ttk.Label(window, text="Bubble Sort")
label.place(x=200, y=620)

#Third frame top-middle (Insertion Sort)
canvas3 = Canvas(window, width=400, height=200, bg=WHITE)
canvas3.grid(row=1, column=0, padx=10, pady=5)
canvas3.place(x = 550, y = 130)
label = ttk.Label(window, text="Insertion Sort")
label.place(x=720, y=350)

#Fourth frame Bottom-middle (Selection Sort)
canvas4 = Canvas(window, width=400, height=200, bg=WHITE)
canvas4.grid(row=1, column=0, padx=10, pady=5)
canvas4.place(x = 550, y = 400) 
label = ttk.Label(window, text="Selection Sort")
label.place(x=720, y=620)

#Fifth frame top-right (Merge Sort)
canvas5 = Canvas(window, width=400, height=200, bg=WHITE)
canvas5.grid(row=1, column=0, padx=10, pady=5)
canvas5.place(x = 1070, y = 130) 
label = ttk.Label(window, text="Merge Sort")
label.place(x=1240, y=350)

#Sixth frame Bottom-right (Heap Sort)
canvas6 = Canvas(window, width=400, height=200, bg=WHITE)
canvas6.grid(row=1, column=0, padx=10, pady=5)
canvas6.place(x = 1070, y = 400) 
label = ttk.Label(window, text="Heap Sort")
label.place(x=1240, y=620)

#Sort Button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

#Genrate Array
b2 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b2.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()