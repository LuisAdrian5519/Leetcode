

def TripleSum(Opt,i,j,arr):
    if i <= len(arr)-1:
        Opt[j] += arr[i]
        TripleSum(Opt,i+2,j,arr)
    else:
        return Opt
    
def maxSubsetSum(arr):
    
    Opt = [0] * len(arr)
    
    for i in range(len(arr)):
        if i+2 <= len(arr)-1:
            TripleSum(Opt,i,i,arr)
            for j in range(i+2,len(arr)):
                if arr[i]+arr[j] > Opt[i]:
                   Opt[i] = arr[i]+arr[j]
        else:
            pass
            
    return max(Opt)


arr = [3, 7, 4, 6, 5]
maxSubsetSum(arr)