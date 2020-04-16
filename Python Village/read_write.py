i = 1
with open("rosalind_ini5.txt", 'r') as f:
    for line in f:
        if i%2== 0:
            print(line)
        i+=1
