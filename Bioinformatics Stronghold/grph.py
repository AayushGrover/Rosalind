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

def solution(dna, id, k=3):

    for i, dna1 in enumerate(dna):
        dna_s = dna1[-k:]
        for j, dna2 in enumerate(dna):
            if dna1 != dna2:
                dna_p = dna2[:k]
                if dna_s == dna_p:
                    print(id[i], id[j])


if __name__ == "__main__":
    
    dna_list, id_list = read_fasta('rosalind_grph.txt')
    solution(dna_list, id_list)