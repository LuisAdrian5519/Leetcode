

def maxSubsetSum(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return max(0, arr[0])

    dp = [0] * len(arr)
    
    # Estas condiciones se eligen porque podemos elegir el 0 como respuesta. 
    # Si el array inicia en numero negativo, sería incorrecto elegirlo como valor máximo
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], arr[i])

    return max(dp)


arr = [3, 7, 4, 6, 5]
maxSubsetSum(arr)