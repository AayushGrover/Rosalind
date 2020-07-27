import requests
import re

def get_aa(prot):

    url = f'https://www.uniprot.org/uniprot/{prot}.fasta'

    r = requests.get(url, allow_redirects=True)

    s = r.content.decode('utf-8')
    k = s.find('\n')
    s = s[k:]

    return s.replace('\n','') 

def solution(name2aa):
    pattern = 'N[^P](S|T)[^P]'

    sol = dict()

    for key,val in name2aa.items():
        sol[key] = list()
        match = re.search(pattern, val)
        k1 = 0
        while match:
            k = match.span()[0]
            k1 += k+1
            sol[key].append(k1)
            val = val[k+1:]
            match = re.search(pattern, val)

    return sol

if __name__ == "__main__":
    name2aa = dict()
    with open('rosalind_mprt.txt', 'r') as f:
        for line in f:
            line = line.replace('\n','')
            name2aa[line] = get_aa(line)

    sol = solution(name2aa)
    
    for key, val in sol.items():
        if len(val) > 0:
            print(key)
            for idx in val:
                print(idx, end=" ")
            print()