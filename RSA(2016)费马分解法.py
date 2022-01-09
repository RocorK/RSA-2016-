# 定义费马分解法,适用于p,q相近的情况
# 爆破之后发现Frame10中的模数可以在短时间内使用此方法分解
for i in range(21):
    with open("D:\大学生活\大三\密码\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）\Frame"+str(i), "r") as f:
        tmp = f.read()
        ns.append(tmp[0:256])
        es.append(tmp[256:512])
        cs.append(tmp[512:768])
def pq(n):
    B=math.factorial(2**14)
    u=0;v=0;i=0
    u0=gmpy2.iroot(n,2)[0]+1
    while(i<=(B-1)):
        u=(u0+i)*(u0+i)-n
        if gmpy2.is_square(u):
            v=gmpy2.isqrt(u)
            break
        i=i+1  
    p=u0+i+v
    return p
def fermat_resolve():
    for i in range(10,14):
        N = int(ns[i], 16)
        p = pq(N)
        print(p)
def get_content_of_frame10():
    p = 9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978699
    n = int(ns[10], 16)
    c = int(cs[10], 16)
    e = int(es[10], 16)
    q = n // p
    phi_of_frame10 = (p-1)*(q-1)
    d = gmpy2.invert(e, phi_of_frame10)
    m = gmpy2.powmod(c, d, n)
    final_plain = binascii.a2b_hex(hex(m)[2:])
    print(final_plain) 
    
get_content_of_frame10()
