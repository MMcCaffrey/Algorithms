def bubblesort(input):
    n = len(input)
    for i in range(n):
        for j in range(0,n-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    return input

def merge(left, right):
    result=[]
    while len(left)!=0 and len(right)!=0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)==0:
        result+=right
    else:
        result+=left
    return result

def mergesort(input):
    if len(input) < 2:
        return input
    else:
        middle = len(input)//2
        left = mergesort(input[:middle])
        right = mergesort(input[middle:])
        return merge(left, right)  