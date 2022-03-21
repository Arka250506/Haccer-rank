def staircase(n):
    # Write your code here
    for i in range (1,1 + n):
        s =  "#" * i
        print (s.rjust(n))
        
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
