# s = int(input())
s = input()

slist = list(s)
# print(str(slist))
count = 1
ans = "Yes"
low_flag = False
up_flag = False
for st in slist:
    if count % 2 == 1 and st.isupper():
        # 奇数番目が大文字だったら
        ans = "No"
        
    elif count % 2 == 0 and st.islower():
        # 偶数番目が小文字だったら
        ans = "No"
    count+=1

print(ans)
# 出力
# print("{}".format(a))