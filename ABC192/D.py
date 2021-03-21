X = input()
M = int(input())

str_num = str(X)
llist_num = list(str_num)
list_num = [int(s) for s in llist_num]

d = max(list_num)
count = d+1
count_nums = 0
while(1):
    # count進法で判断
    out = int((X),count)
    # print(int((X),count))
    
    if(out<=M):
        count_nums += 1
        count += 1
    else:
        break

print(count_nums)
