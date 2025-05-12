def binary_sort(arr,x):
    low=0
    high=len(arr)
    mid=0
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
        
    return -1

arr = [3,6,9,1,2,0,4,5,7,8]
x=7
result = binary_sort(arr,x)
print("Index of element is",result)