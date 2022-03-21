def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apel_baru , jeruk_baru = 0,0 
    apl = [a+d for d in apples ] 
    jrk = [b+d for d in oranges]
    
    for i in apl :
        if i >= s and  i <=   t:
            apel_baru+= 1 
        if i >= s and i <= t :
            jeruk_baru += 1 
    print (apel_baru)
    print (jeruk_baru)
     
    
    
     
    
           
            
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))
