import sys
import math

def resolve():
    N = int(input())
    count = 0
    n = 1
    while(n < N+1):
        
        n_len = len(str(n))
        print("見るn"+str(n))
        if n_len % 2 == 1 :
            print("nの桁数が奇数")
            if n_len == 1:
                n = 10
            else:
                
                print("fdsaffdsafsfd")
                print(n_len)
                n = pow(10,(n_len))
            print("nの桁数を偶数にした: 次は: " + str(n))

        elif (n_len % 2 == 0 and str(n)[:int(n_len/2)] == str(n)[int(n_len/2):]):
            # print("dfsaf")
            count += 1
            
        
        n+=1
        
            
    print(count)


resolve()


