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

def get_complement(dna):
    mapping = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    comp = ''
    for base in dna:
        comp += mapping[base]
    return comp

def dna2prot(dna, table):
    chunk_size = 3
    prot = ''
    for i in range(0, len(dna), chunk_size):
        try:
            prot += table[str(dna[i:i+chunk_size])]
        except:
            continue
    return prot

def solution(prot):
    c = 0
    i = list()
    j = -1
    while c < len(prot):
        if prot[c] == 'M':
            i.append(c)
        if prot[c] == '_':
            j = c
        if  j!=-1 and len(i) > 0:
            for val in i:
                if val < j:
                    print(prot[val:j])
            if val < j: 
                j = -1
                i = list()
        c += 1

if __name__ == "__main__":
    table = { 
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
        }
    
    dna_list,_ = read_fasta('rosalind_orf.txt')
    dna_str = dna_list[0]
    aa_str1 = dna2prot(dna_str, table)
    aa_str2 = dna2prot(dna_str[1:], table)
    aa_str3 = dna2prot(dna_str[2:], table)
    dna_comp = get_complement(dna_str[::-1])
    aa_str4 = dna2prot(dna_comp, table)
    aa_str5 = dna2prot(dna_comp[1:], table)
    aa_str6 = dna2prot(dna_comp[2:], table)
    solution(aa_str1)
    solution(aa_str2)
    solution(aa_str3)
    solution(aa_str4)
    solution(aa_str5)
    solution(aa_str6)