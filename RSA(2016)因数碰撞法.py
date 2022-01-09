for i in range(21):
    with open("D:\大学生活\大三\密码\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）\Frame"+str(i), "r") as f:
        tmp = f.read()
        ns.append(tmp[0:256])
        es.append(tmp[256:512])
        cs.append(tmp[512:768])
# 因数碰撞法
def same_factor():
    plaintext = []
    index = []
    for i in range(21):
        for j in range(i+1, 21):
            if int(ns[i], 16) == int(ns[j], 16):
                continue
            prime = gmpy2.gcd(int(ns[i], 16), int(ns[j], 16))
            if prime != 1:
                print((ns[i], ns[j]))
                print((i, j))
                index.append(i)
                index.append(j)
                p_of_frame = prime
    q_of_frame1 = int(ns[index[0]], 16) // p_of_frame
    q_of_frame18 = int(ns[index[1]], 16) // p_of_frame
    print(p_of_frame)
    print(q_of_frame1, q_of_frame18)

    phi_of_frame1 = (p_of_frame-1)*(q_of_frame1-1)
    phi_of_frame18 = (p_of_frame-1)*(q_of_frame18-1)

    d_of_frame1 = gmpy2.invert(int(es[index[0]],16) ,phi_of_frame1)
    d_of_frame18 = gmpy2.invert(int(es[index[1]], 16), phi_of_frame18)

    plaintext_of_frame1 = gmpy2.powmod(int(cs[index[0]], 16), d_of_frame1, int(ns[index[0]], 16))
    plaintext_of_frame18 = gmpy2.powmod(int(cs[index[1]], 16), d_of_frame18, int(ns[index[1]], 16))

    final_plain_of_frame1 = binascii.a2b_hex(hex(plaintext_of_frame1)[2:])
    final_plain_of_frame18 = binascii.a2b_hex(hex(plaintext_of_frame18)[2:])

    plaintext.append(final_plain_of_frame1)
    plaintext.append(final_plain_of_frame18)

    print(plaintext) 
same_factor()
