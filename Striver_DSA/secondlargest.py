def second_largest(arr,n):
    largest=arr[0]
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i]
    slargest=-1
    for i in range(0,n):
        if arr[i]>slargest and arr[i]!=largest:
            slargest=arr[i]

    return slargest

def second_smallest(arr,n):
    smallest=arr[0]
    for i in range(0,n):
        if arr[i]<smallest:
            smallest=arr[i]
    ssmallest=9999999999999999
    for i in range(0,n):
        if arr[i]<ssmallest and arr[i]!=smallest:
            ssmallest=arr[i]
    return ssmallest



if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,6,5,4,3,2,1,10,12,20,13]
    n=len(arr)
    sl=second_largest(arr,n)
    print("Second largest number is:",sl)
    ss=second_smallest(arr,n)
    print("Second smallest number is:",ss)

    