def main():
    print("Разностное множество Холла")
    p=int(input())
    print("проверка р =",p,checkP(p))
    v,k,L=findParametrsOfDiffSet(p)
    print("параметры разностного множества: v = ",v," k = ",k," L = ",L)
    generator=findGeneratorSequence(p)
    print("генератор ",generator)
    listForSampling=makeListForSampling(generator,p)
    print("остатки по модулю 6\n",listForSampling)
    D1=[]
    D2=[]
    D3=[]
    for i in range(len(listForSampling)):
        if (listForSampling[i]==0)|(listForSampling[i]==1)|(listForSampling[i]==3):
            D1.append(i+1)
        if (listForSampling[i]==1)|(listForSampling[i]==2)|(listForSampling[i]==4):
            D2.append(i+1)
        if (listForSampling[i]==2)|(listForSampling[i]==3)|(listForSampling[i]==5):
            D3.append(i+1)
    print("D1 =",D1)
    print("проверка множества ",checkDiffSet(D1,k,p,3))
    print("D2 =",D2)
    print("проверка множества ",checkDiffSet(D2,k,p,3))
    print("D3 =",D3)
    print("проверка множества ",checkDiffSet(D3,k,p,3))
####
def checkP(p):
    if(not isItPrimeNumber(p)):
        return False
    n=math.sqrt((p-27)/4)
    return int(n)==float(n)
#
def isItPrimeNumber(p):
    for i in range(2,int(math.sqrt(p)+1)):
        if (p%i==0):
            return False
    return True
#
def findParametrsOfDiffSet(p):
    v=p
    t=int((p+1)/4)
    k=2*t-1
    L=t-1
    return v,k,L
####
def findGeneratorSequence(p):
    dividersP_minus1=findDividersN(p-1)
    print("делители p-1",dividersP_minus1)
    for generator in range(2,p):
        generatorOfPreviousDegree=1
        previousDegree=0
        for divider in dividersP_minus1:
            generatorOfPreviousDegree=(generatorOfPreviousDegree*(generator**(divider-previousDegree)))%p
            previousDegree=divider
            #print(previousDegree,"  ",generatorOfPreviousDegree)
            if (generatorOfPreviousDegree==1):
                break
        if (divider==(p-1)):
            return generator
    return False
#
def findDividersN(n):
    dividers=[]
    for i in range(1,n+1):
        if (n%i==0):
            dividers.append(i)
    return dividers
####
def makeListForSampling(generator,p):
    generatorDegrees=findGeneratorDegrees(generator,p)
    print("степени генератора\n",generatorDegrees)
    indGenerator=findIndGenerator(generatorDegrees)
    print("ind генератора\n",indGenerator)
    listForSampling=[]
    for i in indGenerator:
        listForSampling.append(i%6)
    return listForSampling    
#
def findGeneratorDegrees(generator,p):
    generatorDegrees=[]
    generatorOfPreviousDegree=1
    for i in range(p-1):
        generatorOfPreviousDegree=generatorOfPreviousDegree*generator%p
        generatorDegrees.append(generatorOfPreviousDegree)
    return generatorDegrees
#
def findIndGenerator(generatorDegrees):
    indGenerator=[]
    for i in range(1,len(generatorDegrees)+1):
        indGenerator.append(generatorDegrees.index(i)+1)
    return indGenerator
####
def checkDiffSet(D,k,p,d):
    if len(D)!=k:
        return False
    diffSet=[];
    print("величина сдвига ",d)
    for i in range(p):
        if (i in D):
            diffSet.append(0)
        else:
            diffSet.append(1)
    print(diffSet)
    shiftDiffSet=diffSet[len(diffSet)-d:]+diffSet[:len(diffSet)-d]
    print(shiftDiffSet)
    sumDiffSet=[]
    numOfMismatches=0
    for i in range(p):
        sumDiffSet.append((diffSet[i]+shiftDiffSet[i])%2)
        if (diffSet[i]!=sumDiffSet[i]):
            numOfMismatches+=1
    print(sumDiffSet)
    print("количество несовпадений",numOfMismatches)
    if (numOfMismatches!=(p+1)/2):
        return False
    return True
####
import math
main()
