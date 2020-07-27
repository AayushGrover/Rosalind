if __name__ == "__main__":
    '''
    geno_1 : AA-AA
    geno_2 : AA-Aa
    geno_3 : AA-aa
    geno_4 : Aa-Aa
    geno_5 : Aa-aa
    geno_6 : aa-aa
    '''
    geno = [19609, 19487, 19517, 19365, 19627, 19596]
    probab = [1, 1, 1, 0.75, 0.5, 0]
    mean = 0

    for i in range(len(geno)):
        val = 2*geno[i]*probab[i]
        mean += val

    print(mean)