import binascii
import gmpy2
from Crypto.Util.number import*
# 欧几里得算法
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
ns = list()
es = list()
cs = list()
for i in range(21):
    with open("D:\大学生活\大三\密码\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）\Frame"+str(i), "r") as f:
        tmp = f.read()
        ns.append(tmp[0:256])
        es.append(tmp[256:512])
        cs.append(tmp[512:768])
# 公共模数攻击
def same_modulus(index1,index2):
    # 寻找公共模数
    '''index1 = 0
    index2 = 0
    for i in range(21):
        for j in range(i+1, 21):
            if ns[i] == ns[j]:
                print('Same modulus found!' + str((ns[i], ns[j])))
                index1 ,index2 = i, j  '''
    e1 = int(es[index1], 16)
    e2 = int(es[index2], 16)
    n = int(ns[index1], 16)
    c1 = int(cs[index1], 16)
    c2 = int(cs[index2], 16)
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    # 求模反元素
    if s1<0:
        s1 = - s1
        c1 = gmpy2.invert(c1, n)
    elif s2<0:
        s2 = - s2
        c2 = gmpy2.invert(c2, n)

    m = pow(c1,s1,n)*pow(c2,s2,n) % n

    print(m)
    print(long_to_bytes(m))
same_modulus(0,4)
