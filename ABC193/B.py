s = int(input())

# N = 0から
min = 1000000000000000000000
for N in range(s):
    A, P, X = map(int, input().split())
    count = 0
    while(A>0.5):
        if(count==0):
            count+=1
            A = A - 0.5
        else:
            count=int(A+1)
            A=0
    NUM = X - count
    if NUM > 0 and min>P:
        min = P
    # print("count"+str(count)+" num" + str(NUM))

if min == 1000000000000000000000:
    min = -1
print(min)
