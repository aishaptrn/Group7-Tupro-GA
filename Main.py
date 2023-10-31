import math
import random

# Deklarasi Konstanta
ukuranPopulasi = 10
jumGenerasi = 10
populasi = []
probCrossOver = 0.7
probMutasi = 0.01
x1_min = -10
x2_min = -10
x1_max = 10
x2_max = 10

# Fungsi Inisialisasi Populasi
def inisialisasi(populasi, ukuranPopulasi):
    for i in range (ukuranPopulasi):
        kromosom = []
        for i in range(jumGenerasi):
            kromosom.append(random.randint(-10, 10))
        populasi.append(kromosom)
    return populasi

# Fungsi Dekode Kromosom
def dekode(kromosom):
    gen = kromosom
    x1 = x1_min + (x1_max - x1_min) * (gen[0] + gen[1] + gen[2] + gen[3] + gen[4])
    x2 = x2_min + (x2_max - x2_min) * (gen[5] + gen[6] + gen[7] + gen[8] + gen[9])
    return x1, x2

# Fungsi Perhitungan Fitness Minimum
def fitness(x1, x2):
    a = 0.5
    h = -(math.sin(x1) * math.cos(x2) + 4/5 * math.exp(1 - math.sqrt(math.pow(x1, 2) + math.pow(x2, 2))))
    return 1 / (h + a)

def fitnessPopulasi(populasi):
    fitPop = []
    for i in range (len(populasi)):
        kromosom = populasi[i]
        x1, x2 = dekode(kromosom)
        fitPop.append(fitness(x1, x2))
    return fitPop

def fitnessMax(fitnessPopulasi):
    global max
    idx = 0
    for i in range(len(fitnessPopulasi)):
        if (fitnessPopulasi[i] > fitnessPopulasi[idx]):
            idx = i
            max = fitnessPopulasi[idx]
    return max

def fitnessMin(fitnessPopulasi):
    global min
    idx = 0
    for i in range(len(fitnessPopulasi)):
        if (fitnessPopulasi[i] < fitnessPopulasi[idx]):
            idx = i
            min = fitnessPopulasi[idx]
    return min

# Fungsi Pemilihan Orang Tua
def roulette(populasi, fitness, fitnessTotal):
    fitPop = fitnessPopulasi(populasi)
    fitnessTotal = 0
    for i in range(len(fitnessPopulasi(populasi))):
        fitnessTotal += fitPop[i]
    rand = random.random()
    
    k = 0
    while (rand > 0):
        rand -= (fitPop[k] / fitnessTotal)
        k += 1
        if (k == (len(populasi) - 1)):
            break
    parent = populasi[k]
    return parent

# Fungsi Crossover
def crossover(parent1, parent2):
    crossover1 = []
    crossover2 = []
    cross = []
    prob = random.random()
    
    if (prob < probCrossOver):
        point = random.randint(0,4)
        crossover1[:point] = parent1[:point]
        crossover1[point:] = parent2[point:]
        crossover2[:point] = parent2[:point]
        crossover2[point:] = parent1[point:]
        
        cross.append(crossover1)
        cross.append(crossover2)
    else:
        cross.append(parent1)
        cross.append(parent2)
    return cross

# Fungsi Mutasi
def mutasi(crossover1, crossover2):
    cross = []
    
    for i in range(len(crossover1)):
        p = random.random()
        if (p < 0.01):
            crossover1[i] = random.randint(-10,10)
    
    for j in range(len(crossover2)):
        q = random.random()
        if (q < 0.01):
            crossover2[i] = random.randint(-10,10)
            
    cross.append(crossover1)
    cross.append(crossover2)
    return cross

# Fungsi Pergantian Generasi
popInit = inisialisasi(populasi, ukuranPopulasi)
while (jumGenerasi < 11):
    idList = []
    fitList = []
    newPop = []
    children = []
    bestChrom = fitnessMax(popInit)
    total = 0
    
    print("Generasi ke-", jumGenerasi, "=", popInit, "\n")
    
    for i in range(len(popInit)):
        idList = popInit[i]
        print("Kromosom ke-", i+1, "=", idList)
        
        dec = dekode(idList)
        print("Dekode kromosom ke-", i+1, "=", dec)
        
        fness = fitnessPopulasi(popInit)
        print("Nilai fitness ke-", i+1, "=", fness[i], "\n")
        
        fitList.append(fitnessPopulasi(popInit))
        total += fness[i]
    
    for j in range(int(len(popInit)/2)):
        parent1 = roulette(popInit, fitList, total)
        parent2 = roulette(popInit, fitList, total)
        
        print("Parent 1 = ", parent1)
        print("Parent 2 = ", parent2)
        
        children = crossover(parent1, parent2)
        children = mutasi(children[0], children[1])
        
        print("Children = ", children, "\n")
        
        newPop.append(children[0])
        newPop.append(children[1])
        
    print("New Population", jumGenerasi, "=", newPop)
    
    bestChrom = fitnessMax(newPop)
    popInit = newPop
    jumGenerasi += 1
    
print("\nKromosom Terbaik = ", bestChrom)

dcd = dekode(bestChrom)

print("Dekode Kromosom = ", dcd)
print("Nilai Fitness = ", fitness(dcd[0], dcd[1]))