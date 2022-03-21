def diagonalDifference(arr):
    # Write your code here
    a1,a2 = 0,0
    jumlah = len(arr)
    for i in range(jumlah):
        a1 += arr[i][i]
        a2 += arr[i][n-i-1]
    return abs(a1-a2)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
