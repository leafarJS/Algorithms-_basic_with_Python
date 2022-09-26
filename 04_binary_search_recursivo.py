# Python 3 program for recursive binary search.

def binary_search(arr, low, high, x):

    if high >= low:
 
        mid = (high + low) // 2
 
  
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
          return -1
 

arr = [100,10,90,20,80,30,70,40,60,50]

x = 80
 
result = binary_search(sorted(arr, reverse= False), 0, len(arr)-1, x)
 
if result != -1:
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in array")  