i=0
id_list = list()
dna_list = list()
with open("rosalind_gc.txt", 'r') as f:
    for line in f:
        if line[0] == ">":
            if i != 0:
                dna_list.append(dna.replace("\n",""))
            id_list.append(line[1:])
            dna = ""
        else:
            dna += line
            i=1
dna_list.append(dna.replace("\n",""))

# print(len(id_list), len(dna_list))

def gc_content(dna):
    l = len(dna)
    def count_gc(dna):
        count = 0.0
        for i in dna:
            if i == "G" or i == "C":
                count+=1.0
        return count
    gc = count_gc(dna)
    return gc/l

for i in range(len(id_list)):
    if i == 0:
        max_gc = 0
    gc = gc_content(dna_list[i])
    if gc > max_gc:
        max_gc = gc
        argmax = id_list[i]

print(argmax)
print(max_gc*100)