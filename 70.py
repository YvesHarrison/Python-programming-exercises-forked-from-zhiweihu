import math
def search(li,target):
    left=0
    right=len(li)-1
    while(left<=right):
        mid=math.floor((left+right)/2)
        if li[mid]==target:
            return mid
        elif li[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

def Question70():
    li=[2,5,7,9,11,17,222]
    print(search(li,11))
    print(search(li,223))
    
Question70()