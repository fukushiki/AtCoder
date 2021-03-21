N = int(input())
# N
ls = []
# for Num in range(N):
#     if Num+1 > N:
#         break
#     else:
#         ls.append(Num+1)
 
ls = list(range(N))
ls.append(N)
ls.remove(0)
for num in range(N-1):
    a = num + 2
    b = 2
    while(b<=N):
        pows = a ** b
        # print(str(a)+"     "+str(b)+"     "+str(pows))
        try:
            if(pows<=N):
                ls.remove(pows)
            else:
                break
        except:
            pass
        b+=1

# for l in ls:
#     print(l)
# print("   ")
print(len(ls))
