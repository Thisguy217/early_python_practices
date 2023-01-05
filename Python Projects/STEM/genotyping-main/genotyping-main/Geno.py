def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]

geno1=input("First Genotype string:")
geno2=input("Second Genotype string:")

genotype1=Convert(geno1)
genotype2=Convert(geno2)

phenotype1=genotype1[0]+genotype2[0]
phenotype2=genotype1[1]+genotype2[0]
phenotype3=genotype1[0]+genotype2[1]
phenotype4=genotype1[1]+genotype2[1]

if phenotype1[0].isupper()==False:
    phenotype1=reverse(phenotype1)
else:
    phenotype1
if phenotype2[0].isupper()==False:
    phenotype2=reverse(phenotype2)
else:
    phenotype2
if phenotype3[0].isupper()==False:
    phenotype3=reverse(phenotype3)
else:
    phenotype3
if phenotype4[0].isupper()==False:
    phenotype4=reverse(phenotype4)
else:
    phenotype4

print(" ",genotype1[0]," ",genotype1[1])
print(genotype2[0],phenotype1,phenotype2)
print(genotype2[1],phenotype3,phenotype4)

percentages=[]
percentages.append(phenotype1)
percentages.append(phenotype2)
percentages.append(phenotype3)
percentages.append(phenotype4)
print(str(int(percentages.count(geno1[0].upper()+geno1[0].upper())/len(percentages)*100))+"% of",geno1[0].upper()+geno1[1].upper())
print(str(int(percentages.count(geno1[0].upper()+geno1[0].lower())/len(percentages)*100))+"% of",geno1[0].upper()+geno1[1].lower())
print(str(int(percentages.count(geno1[0].lower()+geno1[0].lower())/len(percentages)*100))+"% of",geno1[0].lower()+geno1[1].lower())