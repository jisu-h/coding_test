n = int(input())
s = list(map(int,input().split()))
m = max(s)

new_list=[]
for i in s:
    new_list.append(i/m*100)
print(sum(new_list)/n)