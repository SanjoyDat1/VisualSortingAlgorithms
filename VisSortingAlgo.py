import numpy as np
import matplotlib.pyplot as plt
import random

#******************************************************************

#Variables for the unsorted list of integers
length = 50
max = 100
min = 1
randomNums = []
step = 0

#******************************************************************

#Basic Sorting Algorithm Functions (Bubble, Merge, BOGO, Selection, Insertion)

#Bubble Sort
def BubbleSort(randArray):
    n = len(randArray)
    step = 0
    for j in range(n):
        print(j,"/",n)
        for i in range(n-j-1):
            step +=1
            #Compare first and second num
            numOne = randArray[i]
            numTwo = randArray[i+1]
            if numOne>numTwo:
                #Change order of nums if first num is greater than second num
                randArray[i],randArray[i+1] = randArray[i+1], randArray[i]
    #Print number of steps for sorting
    print("Total number of steps: ",step)
    return randArray

#Merge Sort
def MergeSort(randArray):
    
    n = len(randArray)
    #Divide array if more than one element
    if n  > 1:
        mid = n // 2
        #Divide array into two halves
        left_half = randArray[:mid]
        right_half = randArray[mid:]
        
        #Recursively sort both halves
        MergeSort(left_half)
        MergeSort(right_half)
        i = j = k = 0
    
        #Merge the halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                randArray[k] = left_half[i]
                i += 1
            else:
                randArray[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any elements were left in the left_half
        while i < len(left_half):
            randArray[k] = left_half[i]
            i += 1
            k += 1
        
        # Checking if any elements were left in the right_half
        while j < len(right_half):
            randArray[k] = right_half[j]
            j += 1
            k += 1
    
    #Return sorted array
    return randArray

#Bogo Sort
def BogoSort(randArray):
    step = 0
    #Randomly arrange array until sorted correctly
    while not IsSorted(randArray):
        random.shuffle(randArray)
        step +=1
        print(step)
    return randArray

#Checking if the current function is sorted (for Bogo Sort def)
def IsSorted(arr):
    for i in range (len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

#Selection Sort
def SelectionSort(randArray):
    n = len(randArray)
    step = 0
    #Find the smallest element and swap it with the first unsorted element in the array
    for i in range(n):
        for j in range(n,i):
            step += 1
            if randArray[j-1] < randArray[j]:
                randArray[j-1], randArray[j] = randArray[j], randArray[j-1]
                print(randArray)
    return randArray

#Insertion Sort
def InsertionSort(randArray):
    n = len(randArray)
    #Iterate through array and find location for each next integer in the series
    for i in range (1, n):
        move = randArray[i]
        j = i-1
        while j >=0 and move < randArray[j]:
            randArray[j+1] = randArray[j]
            j -= 1
        randArray[j+1] = move
    return randArray


#******************************************************************

#Visualized Sorting Algorithm Functions (Bubble, Merge, BOGO, Selection, Insertion)

#Bubble Sort Visualization
def VisualizeBubbleSort(arr,time):
    #Check if the array is empty
    if not arr:
        print("The array is empty.")
        return

    print("Initial array:", arr)
    
    n = len(arr)
    step = 0
    plt.ion()  
    fig, ax = plt.subplots()
    
    for j in range(n):
        print(f"{j + 1} / {n}")
        for i in range(n - j - 1):
            step += 1
            numOne = arr[i]
            numTwo = arr[i + 1]
            
            #Clear graph
            ax.clear()
            #Create blue bars
            ax.bar(range(n), arr, color='blue')  
            
            #Highlight current bars being compared
            ax.bar(i, numOne, color='red')
            ax.bar(i + 1, numTwo, color='green')

            #Swap if first num is greater than second num
            if numOne > numTwo:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            #Titles and pause intervals between each iteration
            ax.set_title(f'Bubble Sort: Step {step}')  
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(time)  

    plt.ioff()  
    plt.show()

#Merge Sort Visualization
def VisualizeMergeSort(arr, time):
    global step

    # Check if the array is empty
    if not arr:
        print("The array is empty.")
        return

    print("Initial array:", arr)
    
    #Set up  environment
    n = len(arr)
    plt.ion()  
    fig, ax = plt.subplots()

    #Recursive function for merge sort with visualization
    def merge_sort_visualize(arr, left_index, right_index):
        global step
        if left_index < right_index:
            mid = (left_index + right_index) // 2

            #Recursive calls to sort left and right halves
            merge_sort_visualize(arr, left_index, mid)
            merge_sort_visualize(arr, mid + 1, right_index)

            # Merge the sorted halves
            merge(arr, left_index, mid, right_index)

    # Function to merge two halves and visualize
    def merge(arr, left_index, mid, right_index):
        global step
        left_half = arr[left_index:mid + 1]
        right_half = arr[mid + 1:right_index + 1]

        i = j = 0
        k = left_index

        while i < len(left_half) and j < len(right_half):
            step += 1
            ax.clear()
            ax.bar(range(n), arr, color='blue')

            #Highlight the merging area
            ax.bar(range(left_index, right_index + 1), arr[left_index:right_index + 1], color='green')
            ax.bar(k, arr[k], color='red')

            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            ax.set_title(f'Merge Sort: Step {step}')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(time)

        #Check if any elements were left in left_half
        while i < len(left_half):
            step += 1
            arr[k] = left_half[i]
            ax.clear()
            ax.bar(range(n), arr, color='blue')
            ax.bar(range(left_index, right_index + 1), arr[left_index:right_index + 1], color='green')
            ax.bar(k, arr[k], color='red')
            i += 1
            k += 1
            ax.set_title(f'Merge Sort: Step {step}')
            plt.pause(time)

        #Check if any elements were left in right_half
        while j < len(right_half):
            step += 1
            arr[k] = right_half[j]
            ax.clear()
            ax.bar(range(n), arr, color='blue')
            ax.bar(range(left_index, right_index + 1), arr[left_index:right_index + 1], color='green')
            ax.bar(k, arr[k], color='red')
            j += 1
            k += 1
            ax.set_title(f'Merge Sort: Step {step}')  
            plt.pause(time)

    # Initial call to recursive merge sort function
    merge_sort_visualize(arr, 0, len(arr) - 1)

    plt.ioff()
    plt.show() 

#Bogo Sort Visualization
def VisualizeBogoSort(arr, time):
    if not arr:
        print("The array is empty.")
        return

    print("Initial array:", arr)
    
    #Set up environment
    n = len(arr)
    step = 0
    plt.ion()
    fig, ax = plt.subplots()

    while not IsSorted(arr):
        #Randomize the array
        random.shuffle(arr)
        step += 1

        #Clear the previous bar graph
        ax.clear()  
        ax.bar(range(n), arr, color='blue')

        #Titles and pause intervals between each iteration
        ax.set_title(f'Bogo Sort: Step {step}')  
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(time)
    
    plt.ioff()
    plt.show()

#Selection Sort Visualization
def VisualizeSelectionSort(arr, time):
    if not arr:
        print("The array is empty.")
        return

    print("Initial array:", arr)
    
    # Set up visualization environment
    n = len(arr)
    step = 0
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()

    # Selection Sort algorithm with visualization
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            step += 1

            #Clear graph
            ax.clear()  
            ax.bar(range(n), arr, color='blue')
            
            #Highlight element being checked
            ax.bar(j, arr[j], color='red')
            
            #Highlight current min element
            ax.bar(min_idx, arr[min_idx], color='green')
            
            # If a new minimum is found, update min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
            
            #Titles and pause intervals between each iteration
            ax.set_title(f'Selection Sort: Step {step}') 
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(time)
        
        # Swap the min element with the next unsorted element (at index i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        #Clear the previous bar graph
        ax.clear()  
        ax.bar(range(n), arr, color='blue') 
        ax.bar(i, arr[i], color='green')  

        #Titles and pause intervals between each iteration
        ax.set_title(f'Selection Sort: Step {step}')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(time)

    plt.ioff()
    plt.show()  

#Insertion Sort Visualization
def VisualizeInsertionSort(arr, time):
    if len(arr) == 0:
        print("The array is empty.")
        return

    print("Initial array:", arr)
    
    #Set up environment
    n = len(arr)
    step = 0
    plt.ion()
    fig, ax = plt.subplots()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        height = arr[j+1]
        
        #Clear the previous bar graph
        ax.clear()  
        ax.bar(range(n), arr, color='blue')  
        #Highlight bar being moved
        ax.bar(j+1, height, color='red')  
    
        #Titles and pause intervals between each iteration
        ax.set_title(f'Insertion Sort: Step {step}') 
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(time)

        #Set height of key bar
        

        #Shift elements that are greater than the key
        while j >= 0 and arr[j] > key:
            step += 1
            arr[j + 1] = arr[j]
            j -= 1

            #Clear the previous bar graph
            ax.clear()  
            ax.bar(range(n), arr, color='blue') 
            #Highlight bar being shifted
            ax.bar(j + 1, height, color='red')  
            #Titles and pause intervals between each iteration
            ax.set_title(f'Insertion Sort: Step {step}') 
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(time) 

        #Insert the key
        arr[j + 1] = key

        #Visualization after inserting the key
        step += 1
        ax.clear()
        ax.bar(range(n), arr, color='blue')
        ax.bar(j + 1, arr[j + 1], color='green')

        #Titles and pause intervals between each iteration
        ax.set_title(f'Insertion Sort: Step {step}') 
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(time)

    plt.ioff() 
    plt.show() 

#******************************************************************

#Change any variables (if needed)
length = length
max = max
min = min

#Create a list of random unsorted numbers
for i in range(length):
    randomNums.append(random.randint(min,max))

#Call the functions below to see the visualizations of each sorting algorithm

#Uncomment below to activate

#VisualizeBubbleSort(randomNums,0.001)
#VisualizeMergeSort(randomNums,0.001)
#VisualizeBogoSort(randomNums, 0.001)
#VisualizeSelectionSort(randomNums, 0.001)
#isualizeInsertionSor(randomNums,0.001)

#******************************************************************
