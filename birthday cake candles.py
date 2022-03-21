def birthdayCakeCandles(candles):
    # Write your code here
    total = 0
    tertinggi = max(candles)
    for bil in candles:
        if bil == tertinggi :
            total += 1 
    return total        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
