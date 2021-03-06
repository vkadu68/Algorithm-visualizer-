from tkinter import *
from tkinter import ttk
import random
import time
import time
def merge_sort(data,drawData,timeTick):
    merge_sort_alg(data,0,len(data)-1,drawData,timeTick)

def merge_sort_alg(data,left,right,drawData,timeTick):
    if left < right:
        middle=(left+right)//2
        merge_sort_alg(data,left,middle,drawData,timeTick)
        merge_sort_alg(data,middle+1,right,drawData,timeTick)
        merge(data,left,middle,right,drawData,timeTick)

def merge(data,left,middle,right,darwData,timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart= data[left: middle +1]
    rightPart=data[middle + 1:right+1]
    leftIdx = rightIdx =0
    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx< len(rightPart):
            if leftPart[leftIdx]<=rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx +=1
            else:
                data[dataIdx]=rightPart[rightIdx]
                rightIdx +=1
        elif leftIdx <len(leftPart):
            data[dataIdx]= leftPart[leftIdx]
            leftIdx +=1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx +=1
    drawData(data,['green' if x>=left and x<=right else 'white' for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left,middle,right):
    colorArray=[]
    for i in range(length):
        if i > left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append('black')
        else:
            colorArray.append('White')
    return colorArray

def insertion(l,drawData,timeTick):
    for i in range(len(l)):
        j=i
        while j>0 and l[j-1]>l[j]:
            l[j],l[j-1]=l[j-1],l[j]
            j=j-1
            drawData(l, ['green' if x < i  else 'red' for x in range(len(l))] )
            time.sleep(timeTick)
    drawData(l, ['green' for x in range(len(l))]) 

def selectionsort(l,drawData, timeTick):
    print('Program went here')
    indexing=range(0,len(l)-1)
    for i in indexing:
        min_value=i
        for j in range(i+1,len(l)):
            drawData(l, ['green' if x == j or x==min_value else 'red' for x in range(len(l))] )
            if l[j]<l[min_value]:
                min_value=j
        if min_value !=i:
            l[min_value], l[i]=l[i], l[min_value]
            
            time.sleep(timeTick)
    drawData(l, ['green' for x in range(len(l))])

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()


def Generate():
    global data
    #print(selected_alg.get())

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    x=selected_alg.get()
    print(x)
    if x=='Selection Sort':
        selectionsort(data,drawData,speedScale.get())
    elif x=='Insertion Sort':
        insertion(data,drawData,speedScale.get())
    elif x=="Merge Sort":
        merge_sort(data,drawData,speedScale.get())    
    else:
        bubble_sort(data, drawData, speedScale.get())

#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Insertion Sort','Selection Sort','Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()