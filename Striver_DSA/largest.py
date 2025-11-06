# def largest(arr):
#     arr.sort()
#     return arr[-1]



# if __name__ == "__main__":

#     arr=[1,2,3,4,5,1,2,7,8,122,1,2]
# print("Largest element of array is: ",largest(arr))

def largest(arr):
    n=len(arr)
    max=arr[0]
    for i in range(0,n):
        if arr[i] > max:
            max=arr[i]
    return max



if __name__ == "__main__":

    arr=[1,2,3,4,5,1,2,7,8,122,1,2]
print("Largest element of array is: ",largest(arr))