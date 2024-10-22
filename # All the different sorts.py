# All the different sorts 
global n
global letters
def menu():
    option = int(input("What option would you like to run?"))
    if option == 1 :
        print("Recursion!")
        factorial(base)
    elif option == 2 :
        print("Linear Search!")
        linearSearch(letters, n, item)
    elif option == 3 :
        print("Binary Search!")
        binarySearch()
    elif option == 4 :
        print("Bubble sort!")
        bubbleSort()
    elif option == 5:
        print("Insertsion sort!")
        insertionSort()
    elif option == 6:
        print("Merge sort!")
    else:
        print("you havent entered a correct command")
menu()

def factorial(base):
	if factorial == 0:
		return 1
	else:
		return base * factorial(base-1)
base = 4
answer = factorial(base)
print("Factorial of",base,"is",answer)
factorial(base)

def linearSearch(letters, n, item):
    for i in range(0, n):
        if (letters[i] == item):
            return i
        return -1

letters = ["B", "V", "D", "E", "T", "P"]
item = input("Enter the item to be found: ")
n = len(letters)
result = linearSearch(letters, n, item)
if(result == -1):
    print("Element not found.")
else:
    print("Element found at index: ", result)
linearSearch(letters, n, item)

def binarySearch(letters,item,lowerBound,upperBound):
    while lowerBound <= upperBound:
        midpoint = lowerBound+(upperBound-lowerBound)//2
        if letters[midpoint]==item:
            print(midpoint+1)
            return midpoint
        elif letters[midpoint]<item:
            lowerBound=midpoint+1
            print(midpoint+1)
        else:
            upperBound = midpoint-1
            print(midpoint+1)
    return -1
letters=["A","B","C","D","E","F","G","H","I","J"]
item=input("Enter the item to be found: ")
result = binarySearch(letters,item,0,len(letters)-1)
if result != -1:
    print (item,"found at position",str(result+1))
else:
    print (item,"not found")
binarySearch(letters,item,lowerBound,upperBound)

def bubbleSort(array):
    for i in range(len(array)):
        print(data)

    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


    data = [6,5,4,3,10]
    print('Sorted Array in Ascending Order:',data)
bubbleSort(data)

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key
        print(data)

    data = [3,6,5,11,2,7,1]
    print('Insertion Sorted Array in Ascending Order:',data)
insertionSort(data)

def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
    while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
    while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
    while j < len(M):
        array[k] = M[j]
        j += 1
        k += 1
    def printList(array):
        for i in range(len(array)):
            print(array[i], end=" ")
        print()

    if __name__ == '__main__':
        array = [6, 5, 12, 10, 9, 1]
        mergeSort(array)
        print("Merge sorted array is: ")
        printList(array)
mergeSort()
