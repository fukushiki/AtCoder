N, K = map(int, input().split())

A_list = []
A_list.append(N)
for x in range(K):
    str_num = str(A_list[x])
    llist_num = list(str_num)
    list_num = [int(s) for s in llist_num]

    g1_ls = sorted(list_num, reverse=True)
    g1 = int("".join([str(n) for n in g1_ls]))

    g2_ls = sorted(list_num)
    g2 = int("".join([str(n) for n in g2_ls]))

    f = g1-g2
    A_list.append(f)


print(A_list[K])
# print("A1" + a)


# for n in range(K):
    
#     f = g1 - g2