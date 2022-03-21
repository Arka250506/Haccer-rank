def minimumBribes(q):
    # Write your code here
    suap = 0
    q = [i-1 for i in q]
    for i, o in enumerate(q):
        sekarang = i

        if o - sekarang > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o -1,0 ):i]:
            if k > o:
                suap += 1

    print(suap)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
