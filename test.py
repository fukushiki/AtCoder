import itertools
l_list=["〇","✕"]
ll_list = itertools.product(l_list, repeat=5)
ls_marubatsu = []
sums = 0
for ls in ll_list:
    num = 0
    count = 0
    ls_temp = []
    for l in ls:
        ls_temp.append(l)
        count += 1
        if l == "〇":
            num+=1
        
        if num == 3 :
            if ls_temp not in ls_marubatsu:
                plus = (pow(0.7,3) * pow(0.3, (count - 3)))
                sums = sums + plus
                ls_marubatsu.append(ls_temp)
            break

print(sums)
print(str(ls_marubatsu))
