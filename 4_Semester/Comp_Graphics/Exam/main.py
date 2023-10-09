import numpy as np

def calculate_intensity(A, B, C, P):
    

    dB = distance(P, B)/distance(A,C)
    dC = distance(P, C)/distance(A,B)
    dA = distance(P, A)/distance(C,B)
    sum=dA+dB+dC
    dA=dA/(sum)
    dB=dB/(sum)
    dC=dC/(sum)
    intensity_P = (dA * I_A + dB * I_B + dC * I_C) 
    return intensity_P


def calculate_i(A, B, K,I_A,I_B): ##calculate for 2 points


    t=distance(A,K)/distance(A,B)
    I_K=I_A*t+I_B*(1-t)    
    return I_K


def distance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5


I_A = 3  # інтенсивність освітлення вершини А
I_B = 4  # інтенсивність освітлення вершини В
I_C = 5  # інтенсивність освітлення вершини С

# Задані координати вершин трикутника
A = (-100, 0)
B = (0, 100)
C = (100, 0)

# Задані координати кінців горизонтального відрізка
M = (-60, 40)
N = (60, 40)


# Задані координати точки P
P = (20, 60)

I_M=calculate_i(A,B,M,I_A,I_B)
I_N=calculate_i(B,C,N,I_B,I_C)
I_P=calculate_i(M,N,P,I_M,I_N)

print("Інтенсивність освітлення на першому кінці відрізка:", I_M)
print("Інтенсивність освітлення на другому кінці відрізка:", I_N)
# Обчислення інтенсивності освітлення в точці P
print("Інтенсивність освітлення в точці P:", I_P)
intensity_P = calculate_intensity(A, B, C, P)
print("Інтенсивність освітлення в точці P(v2):", intensity_P)