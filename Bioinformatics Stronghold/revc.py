s = "TCTGCGCTCGGAATAACGAAGCACGATACGACTAATCGCCTTTCTCTCCAACATAACATTGTACAGTCATAAAAATACTTGATAGGATCCTTTATAATCCTCAGCCGAATGTTTATCTTGGACGCGCGGTAGAACTTTCTGAACTGTTATAAAACCAGAAAAAGACTTCTAGCAGAGATAAGTTGCAGGACCCACAACTCCCGCCGAGTTCAAGTCTATGACAGAGTATTGAAAGTTTGTAGCGCAGCTCGCATCGCATAGTTGTGTCCCTATTACCACATTAATCGATGCTCTCCAAAGTAGATAGGTGGGCCGACTCGTGCCCTGTGGTTAGCAACCAGCGCCCACAGAGCGGATAGTAGTATAAATGACACAGGTTTTGTTAAACCAAATCCTTCAAAGCCAAATCATCATGGTCCGGAATCCCGGGGCAAATTTGCTCCTAGCAGTATTAAACAAGCGACCTTAGAGCCTCCATTAGTTAATGTCGCACCCGTTAGATCATAGAACTTACAACGTAGATAGCGGACTCGAACAGCGGAACGCAGGAATCGATTCTGGACAAATGTTTTACCTACTAAGCTCACGGGATGGTGGTGCGATCCTTAAGTGCAGTCGTTTCCGAAACGCGTCATAAGCCAAGACGGGTCGTTGTTGCTGTGTGAAAATGCCTGCCGGTTAGAGTTGGCCGCTCTTGCAGTAGAGCCATGGACCTTGGAGCTATGCGTTAACCTCGCGTTCCCAAAGCTCACGTTCTAGCCACTCGCAACCCGGGATAAAGATCGTCAGGGCTCTCGGGCCCAGCCGATGAATAGCTCCGGCCCC"
d = {"A": "T", "C": "G", "G": "C", "T": "A"}
u = ""

for i in s:
    u += d[i]

print(u[::-1])