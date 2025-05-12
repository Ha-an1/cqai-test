def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        
        swap=False
        
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
                
        if not swap:
            break
        
arr = [3,6,9,1,2,0,4,5,7,8]
bubble_sort(arr)
print("Sorted array is",arr)