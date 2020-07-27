def str_to_index(s, l):
    for i in range(9):
        if l[i] == s:
            return i

def get_probab(s, k, mat, l):
    if k == 1:
        return mat[str_to_index("Aa-Bb", l)][str_to_index(s, l)]
    sum_s = 0
    for i in l:
        sum_s += get_probab(i, k-1, mat, l)*mat[str_to_index(i, l)][str_to_index(s, l)]
    return sum_s

def make(p1,p2):
    assert len(p1) == len(p2)
    a = {'AA': 0, 'Aa': 0, 'aa': 0}
    b = {'BB': 0, 'Bb': 0, 'bb': 0}
    
    s1 = p1[0][0]+p2[0][0]
    s2 = p1[0][1]+p2[0][0]
    s3 = p1[0][0]+p2[0][1]
    s4 = p1[0][1]+p2[0][1]
    s = [s1, s2, s3, s4]

    a_tot = 0
    for i in a: 
        for aa in s:
            if aa == "aA":
                aa = "Aa"
            if aa == i:
                a[i]+=1
                a_tot+=1

    s1 = p1[1][0]+p2[1][0]
    s2 = p1[1][1]+p2[1][0]
    s3 = p1[1][0]+p2[1][1]
    s4 = p1[1][1]+p2[1][1]
    s = [s1, s2, s3, s4]

    b_tot = 0
    for i in b: 
        for aa in s:
            if aa == "bB":
                aa = "Bb"
            if aa == i:
                b[i]+=1
                b_tot+=1


    d = dict()
    for i in a:
        for j in b:
            s = i+"-"+j
            d[s] = a[i]*b[j]/(a_tot*b_tot)
    
    return d

def make_row(i, l):
    p1 = l[i]
    p2 = "Aa-Bb"
    p1 = p1.split('-')
    p2 = p2.split('-')

    d = make(p1, p2)
    row = []
    for ind in range(len(l)):
        row.append(d[l[ind]])
    return row

def fact(n):
    p = 1
    for i in range(1,n+1):
        p*=i
    return p

def c(n, i):
    return fact(n)/(fact(n-i)*fact(i))

def probab(i, p, N):
    return c(N,i)*(p**i)*((1-p)**(N-i))

def ans(k, n):
    '''
    mat - matrix of parent*child - 9x9
    '''
    mat = []
    
    l = ["AA-BB","AA-Bb","AA-bb","Aa-BB","Aa-Bb","Aa-bb","aa-BB","aa-Bb","aa-bb"]

    for i in range(len(l)):
        mat.append(make_row(i, l))

    p = get_probab("Aa-Bb", k, mat, l)

    print(p)

    s = 0
    N = 2**k
    for i in range(n, N+1):
        s += probab(i,p,N)
    return s

if __name__ == "__main__":
    k, n = 5, 3

    print(ans(k, n))