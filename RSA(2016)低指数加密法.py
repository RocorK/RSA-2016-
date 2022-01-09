# 低加密指数攻击
# 经过输出检测,发现Frame3,Frame8,Frame12,Frame16,Frame20采用低加密指数e=5进行加密
for i in range(21):
    with open("D:\大学生活\大三\密码\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）\Frame"+str(i), "r") as f:
        tmp = f.read()
        ns.append(tmp[0:256])
        es.append(tmp[256:512])
        cs.append(tmp[512:768])
# 前置函数中国剩余定理
def chinese_remainder_theorem(items):
    N = 1
    for a, n in items:
        N *= n
        result = 0
    for a, n in items:
        m = N//n
        d, r, s = egcd(n, m)
        if d != 1:
            N = N//n
            continue
        result += a*s*m
    return result % N, N
# 低加密指数e == 3
def bruce_e_3():
    bruce_range = [7, 11, 15]
    for i in range(3):
        c = int(cs[bruce_range[i]], 16)
        n = int(ns[bruce_range[i]], 16)
        print("This is frame" + str(i))
        for j in range(20):
            plain = gmpy2.iroot(gmpy2.mpz(c+j*n), 3)
            print("This is test" + str(j))
            print(binascii.a2b_hex(hex(plain[0])[2:]))
def low_e_3():
    sessions=[{"c": int(cs[7], 16) ,"n": int(ns[7], 16)},
    {"c":int(cs[11], 16) ,"n":int(ns[11], 16)},
    {"c":int(cs[15], 16) ,"n":int(ns[15], 16)}]
    data = []
    for session in sessions:
        data = data+[(session['c'], session['n'])]
    x, y = chinese_remainder_theorem(data)
    # 直接开三次方根
    plaintext7_11_15 = gmpy2.iroot(gmpy2.mpz(x), 3)
    print(binascii.a2b_hex(hex(plaintext7_11_15[0])[2:])) 
def low_e_5():
    sessions=[{"c": int(cs[3], 16),"n": int(ns[3], 16)},
    {"c":int(cs[8], 16) ,"n":int(ns[8], 16) },
    {"c":int(cs[12], 16),"n":int(ns[12], 16)},
    {"c":int(cs[16], 16),"n":int(ns[16], 16)},
    {"c":int(cs[20], 16),"n":int(ns[20], 16)}]
    data = []
    for session in sessions:
        data = data+[(session['c'], session['n'])]
    x, y = chinese_remainder_theorem(data)
    # 直接开五次方根
    plaintext3_8_12_16_20 = gmpy2.iroot(gmpy2.mpz(x),5)
    print(binascii.a2b_hex(hex(plaintext3_8_12_16_20[0])[2:]))
low_e_3()
low_e_5()
