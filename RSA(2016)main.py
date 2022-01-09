def gcd(a,b):
    a = int(a,16)
    b = int(b,16)
    if a < b:
        a, b = b, a
    while a % b != 0:
        r = a % b
        a, b = b, r
    return b
ns = list()
es = list()
cs = list()
for i in range(21):
    with open("D:\大学生活\大三\密码\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）\Frame"+str(i), "r") as f:
        tmp = f.read()
        ns.append(tmp[0:256])
        es.append(tmp[256:512])
        cs.append(tmp[512:768])
'''print(ns)
print(es)
print(cs)
'''
ls3 = list()
ls5 = list()
lsn = list()
for a in range(21):
    if int(es[a],16) == 3:
        ls3.append(a)
    if int(es[a],16) == 5:
        ls5.append(a)
    if int(es[a],16) ==65537 :
        lsn.append(a)
    for b in range(21):
        if ns[a] == ns[b] and a != b and a < b:
            print('Frame'+str(a)+'和 Frame'+str(b)+'的模数N相同')
            continue
        if gcd(ns[a],ns[b]) != 1 and a != b and a < b:
            print('Frame'+str(a)+'和 Frame'+str(b)+'的模数N具有公共因子')
        

for i in ls3:
    print('Frame'+str(i),end=' ')
print('采用低加密指数e=3进行加密')
for i in ls5:
    print('Frame'+str(i),end=' ')
print('采用低加密指数e=5进行加密')
for i in lsn:
    print('Frame'+str(i),end=' ')
print('采用加密指数e=65537进行加密')
