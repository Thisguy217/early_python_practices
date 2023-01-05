def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

genotype1=input("Enter First Genotypic String:")
genotype2=input("Enter Second Genotypic String:")

if len(genotype1)%2==1 or len(genotype2)%2==1:
    print("Invalid Length")
    exit()

phenotype1=genotype1[0]+genotype2[0]+genotype1[2]+genotype2[2]
phenotype2=genotype1[0]+genotype2[0]+genotype1[2]+genotype2[3]
phenotype3=genotype1[0]+genotype2[0]+genotype1[3]+genotype2[2]
phenotype4=genotype1[0]+genotype2[0]+genotype1[3]+genotype2[3]
phenotype5=genotype1[0]+genotype2[1]+genotype1[2]+genotype2[2]
phenotype6=genotype1[0]+genotype2[1]+genotype1[2]+genotype2[3]
phenotype7=genotype1[0]+genotype2[1]+genotype1[3]+genotype2[2]
phenotype8=genotype1[0]+genotype2[1]+genotype1[3]+genotype2[3]
phenotype9=genotype1[1]+genotype2[0]+genotype1[2]+genotype2[2]
phenotype10=genotype1[1]+genotype2[0]+genotype1[2]+genotype2[3]
phenotype11=genotype1[1]+genotype2[0]+genotype1[3]+genotype2[2]
phenotype12=genotype1[1]+genotype2[0]+genotype1[3]+genotype2[3]
phenotype13=genotype1[1]+genotype2[1]+genotype1[2]+genotype2[2]
phenotype14=genotype1[1]+genotype2[1]+genotype1[2]+genotype2[3]
phenotype15=genotype1[1]+genotype2[1]+genotype1[3]+genotype2[2]
phenotype16=genotype1[1]+genotype2[1]+genotype1[3]+genotype2[3]

phenotype1=Convert(phenotype1)
phenotype2=Convert(phenotype2)
phenotype3=Convert(phenotype3)
phenotype4=Convert(phenotype4)
phenotype5=Convert(phenotype5)
phenotype6=Convert(phenotype6)
phenotype7=Convert(phenotype7)
phenotype8=Convert(phenotype8)
phenotype9=Convert(phenotype9)
phenotype10=Convert(phenotype10)
phenotype11=Convert(phenotype11)
phenotype12=Convert(phenotype12)
phenotype13=Convert(phenotype13)
phenotype14=Convert(phenotype14)
phenotype15=Convert(phenotype15)
phenotype16=Convert(phenotype16)


if phenotype1[0].islower()==True or phenotype1[2].islower()==True:
    if phenotype1[0].islower() and phenotype1[1].isupper():
        phenotype1[0]=phenotype1[0].upper()
        phenotype1[1]=phenotype1[1].lower()
    if phenotype1[2].islower() and phenotype1[3].isupper():
        phenotype1[2]=phenotype1[2].upper()
        phenotype1[3]=phenotype1[3].lower()
if phenotype2[0].islower()==True or phenotype2[2].islower()==True:
    if phenotype2[0].islower() and phenotype2[1].isupper():
        phenotype2[0]=phenotype2[0].upper()
        phenotype2[1]=phenotype2[1].lower()
    if phenotype2[2].islower() and phenotype2[3].isupper():
        phenotype2[2]=phenotype2[2].upper()
        phenotype2[3]=phenotype2[3].lower()
if phenotype3[0].islower()==True or phenotype3[2].islower()==True:
    if phenotype3[0].islower() and phenotype3[1].isupper():
        phenotype3[0]=phenotype3[0].upper()
        phenotype3[1]=phenotype3[1].lower()
    if phenotype3[2].islower() and phenotype3[3].isupper():
        phenotype3[2]=phenotype3[2].upper()
        phenotype3[3]=phenotype3[3].lower()
if phenotype4[0].islower()==True or phenotype4[2].islower()==True:
    if phenotype4[0].islower() and phenotype4[1].isupper():
        phenotype4[0]=phenotype4[0].upper()
        phenotype4[1]=phenotype4[1].lower()
    if phenotype4[2].islower() and phenotype4[3].isupper():
        phenotype4[2]=phenotype4[2].upper()
        phenotype4[3]=phenotype4[3].lower()
if phenotype5[0].islower()==True or phenotype5[2].islower()==True:
    if phenotype5[0].islower() and phenotype5[1].isupper():
        phenotype5[0]=phenotype5[0].upper()
        phenotype5[1]=phenotype5[1].lower()
    if phenotype5[2].islower() and phenotype5[3].isupper():
        phenotype5[2]=phenotype5[2].upper()
        phenotype5[3]=phenotype5[3].lower()
if phenotype6[0].islower()==True or phenotype6[2].islower()==True:
    if phenotype6[0].islower() and phenotype6[1].isupper():
        phenotype6[0]=phenotype6[0].upper()
        phenotype6[1]=phenotype6[1].lower()
    if phenotype6[2].islower() and phenotype6[3].isupper():
        phenotype6[2]=phenotype6[2].upper()
        phenotype6[3]=phenotype6[3].lower()
if phenotype7[0].islower()==True or phenotype7[2].islower()==True:
    if phenotype7[0].islower() and phenotype7[1].isupper():
        phenotype7[0]=phenotype7[0].upper()
        phenotype7[1]=phenotype7[1].lower()
    if phenotype7[2].islower() and phenotype7[3].isupper():
        phenotype7[2]=phenotype7[2].upper()
        phenotype7[3]=phenotype7[3].lower()
if phenotype8[0].islower()==True or phenotype8[2].islower()==True:
    if phenotype8[0].islower() and phenotype8[1].isupper():
        phenotype8[0]=phenotype8[0].upper()
        phenotype8[1]=phenotype8[1].lower()
    if phenotype8[2].islower() and phenotype8[3].isupper():
        phenotype8[2]=phenotype8[2].upper()
        phenotype8[3]=phenotype8[3].lower()
if phenotype9[0].islower()==True or phenotype9[2].islower()==True:
    if phenotype9[0].islower() and phenotype9[1].isupper():
        phenotype9[0]=phenotype9[0].upper()
        phenotype1[1]=phenotype9[1].lower()
    if phenotype9[2].islower() and phenotype9[3].isupper():
        phenotype9[2]=phenotype9[2].upper()
        phenotype9[3]=phenotype9[3].lower()
if phenotype10[0].islower()==True or phenotype10[2].islower()==True:
    if phenotype10[0].islower() and phenotype10[1].isupper():
        phenotype10[0]=phenotype10[0].upper()
        phenotype10[1]=phenotype10[1].lower()
    if phenotype10[2].islower() and phenotype10[3].isupper():
        phenotype10[2]=phenotype10[2].upper()
        phenotype10[3]=phenotype10[3].lower()
if phenotype11[0].islower()==True or phenotype11[2].islower()==True:
    if phenotype11[0].islower() and phenotype11[1].isupper():
        phenotype11[0]=phenotype11[0].upper()
        phenotype11[1]=phenotype11[1].lower()
    if phenotype11[2].islower() and phenotype11[3].isupper():
        phenotype11[2]=phenotype11[2].upper()
        phenotype11[3]=phenotype11[3].lower()
if phenotype12[0].islower()==True or phenotype12[2].islower()==True:
    if phenotype12[0].islower() and phenotype12[1].isupper():
        phenotype12[0]=phenotype12[0].upper()
        phenotype12[1]=phenotype12[1].lower()
    if phenotype12[2].islower() and phenotype12[3].isupper():
        phenotype12[2]=phenotype12[2].upper()
        phenotype12[3]=phenotype12[3].lower()
if phenotype13[0].islower()==True or phenotype13[2].islower()==True:
    if phenotype13[0].islower() and phenotype13[1].isupper():
        phenotype13[0]=phenotype13[0].upper()
        phenotype13[1]=phenotype13[1].lower()
    if phenotype13[2].islower() and phenotype13[3].isupper():
        phenotype13[2]=phenotype13[2].upper()
        phenotype13[3]=phenotype13[3].lower()
if phenotype14[0].islower()==True or phenotype14[2].islower()==True:
    if phenotype14[0].islower() and phenotype14[1].isupper():
        phenotype14[0]=phenotype14[0].upper()
        phenotype14[1]=phenotype14[1].lower()
    if phenotype14[2].islower() and phenotype14[3].isupper():
        phenotype14[2]=phenotype14[2].upper()
        phenotype14[3]=phenotype14[3].lower()
if phenotype15[0].islower()==True or phenotype15[2].islower()==True:
    if phenotype15[0].islower() and phenotype15[1].isupper():
        phenotype15[0]=phenotype15[0].upper()
        phenotype15[1]=phenotype15[1].lower()
    if phenotype15[2].islower() and phenotype15[3].isupper():
        phenotype15[2]=phenotype15[2].upper()
        phenotype15[3]=phenotype15[3].lower()
if phenotype16[0].islower()==True or phenotype16[2].islower()==True:
    if phenotype16[0].islower() and phenotype16[1].isupper():
        phenotype16[0]=phenotype16[0].upper()
        phenotype16[1]=phenotype16[1].lower()
    if phenotype16[2].islower() and phenotype16[3].isupper():
        phenotype16[2]=phenotype16[2].upper()
        phenotype16[3]=phenotype16[3].lower()

phenotype1=''.join(phenotype1)
phenotype2=''.join(phenotype2)
phenotype3=''.join(phenotype3)
phenotype4=''.join(phenotype4)
phenotype5=''.join(phenotype5)
phenotype6=''.join(phenotype6)
phenotype7=''.join(phenotype7)
phenotype8=''.join(phenotype8)
phenotype9=''.join(phenotype9)
phenotype10=''.join(phenotype10)
phenotype11=''.join(phenotype11)
phenotype12=''.join(phenotype12)
phenotype13=''.join(phenotype13)
phenotype14=''.join(phenotype14)
phenotype15=''.join(phenotype15)
phenotype16=''.join(phenotype16)

print(phenotype1,phenotype2,phenotype3,phenotype4)
print(phenotype5,phenotype6,phenotype7,phenotype8)
print(phenotype9,phenotype10,phenotype11,phenotype12)
print(phenotype13,phenotype14,phenotype15,phenotype16)

percentages=[]
percentages.append(phenotype1)
percentages.append(phenotype2)
percentages.append(phenotype3)
percentages.append(phenotype4)
percentages.append(phenotype5)
percentages.append(phenotype6)
percentages.append(phenotype7)
percentages.append(phenotype8)
percentages.append(phenotype9)
percentages.append(phenotype10)
percentages.append(phenotype11)
percentages.append(phenotype12)
percentages.append(phenotype13)
percentages.append(phenotype14)
percentages.append(phenotype15)
percentages.append(phenotype16)

print(str(int(percentages.count(genotype1[0].upper()+genotype1[0].upper()+genotype1[2].upper()+genotype1[2].upper())/len(percentages)*100)),
    "% of",
    genotype1[0].upper()+genotype1[0].upper()+genotype1[2].upper()+genotype1[2].upper())
print(str(int(percentages.count(genotype1[0].upper()+genotype1[0].upper()+genotype1[2].upper()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].upper()+genotype1[0].upper()+genotype1[2].upper()+genotype1[2].lower())
print(str(int(percentages.count(genotype1[0].upper()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].upper()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].lower())

print(str(int(percentages.count(genotype1[0].upper()+genotype1[0].upper()+genotype1[2].lower()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].upper()+genotype1[0].upper()+genotype1[2].lower()+genotype1[2].lower())
print(str(int(percentages.count(genotype1[0].upper()+genotype1[0].lower()+genotype1[2].lower()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].upper()+genotype1[0].lower()+genotype1[2].lower()+genotype1[2].lower())
print(str(int(percentages.count(genotype1[0].lower()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].upper())/len(percentages)*100)),
    "% of",
    genotype1[0].lower()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].upper())
print(str(int(percentages.count(genotype1[0].lower()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].lower()+genotype1[0].lower()+genotype1[2].upper()+genotype1[2].lower())
print(str(int(percentages.count(genotype1[0].lower()+genotype1[0].lower()+genotype1[2].lower()+genotype1[2].lower())/len(percentages)*100)),
    "% of",
    genotype1[0].lower()+genotype1[0].lower()+genotype1[2].lower()+genotype1[2].lower())




