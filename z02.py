import timeit
import random

cnt = 0

def fun(arr, target):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == target:
            cnt += 1
            return mid  
        elif arr[mid] < target: 
            left = mid + 1
            cnt += 1
            return left  
        else: 
            right = mid - 1
            cnt += 1
            return right
    return cnt

start = timeit.default_timer()
print('The start time is :', start)
fun()
print('The difference of time :', timeit.default_timer() - start)