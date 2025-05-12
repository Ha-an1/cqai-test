def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        swapped = False
        
        for j in range (i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                
        if not swapped:
            break
        
arr = [3,6,9,1,2,0,4,5,7,8]
bubble_sort(arr)
print("Sorted array is",arr)