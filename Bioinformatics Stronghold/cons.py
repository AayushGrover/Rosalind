def read_fasta(f_name):
    i=0
    id_list = list()
    dna_list = list()
    with open(f_name, 'r') as f:
        for line in f:
            if line[0] == ">":
                if i != 0:
                    dna_list.append(dna.replace("\n",""))
                id_list.append(line[1:].replace("\n",""))
                dna = ""
            else:
                dna += line
                i=1
    dna_list.append(dna.replace("\n",""))

    return dna_list, id_list

def solution(dna_l):
    n = len(dna_l[0])
    c_list = list()
    for i in range(n):
        d = {'A':0, 'C':0, 'G':0, 'T':0}
        for dna in dna_l:
            d[dna[i]] += 1
        c_list.append({k: v for k,v in sorted(d.items(), key=lambda item: item[1], reverse=True)})
    
    concensus = ""
    for d in c_list:
        concensus+=list(d.keys())[0]
    print(concensus)

    l = ['A', 'C', 'G', 'T']
    for base in l:
        print(base+':', end=' ')
        for d in c_list:
            print(d[base], end=' ')
        print()  


if __name__ == "__main__":
    
    dna_l, _ = read_fasta('rosalind_cons.txt')
    solution(dna_l)