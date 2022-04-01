c= int(input())
for i in range(c):
    n = list(map(int,input().split()))
    avg = sum(n[1:])/n[0]
    
    cnt = 0
    for i in n[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/n[0])*100
    print('%.3f' %per + '%')