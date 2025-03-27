import numpy as np
import random
import timeit

def naiveMultiply(A, B):
    n = len(A)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def strassenMultiply(A, B, threshold=8):
    n = len(A)

    if n <= threshold:
        return naiveMultiply(A, B)
    
    mid = n // 2

    A1_1 = A[:mid, :mid]
    A1_2 = A[:mid, mid:]
    A2_1 = A[mid:, :mid]
    A2_2 = A[mid:, mid:]

    B1_1 = B[:mid, :mid]
    B2_2 = B[:mid, mid:]
    B2_1 = B[mid:, :mid]
    B2_2 = B[mid:, mid:]

    M1 = strassenMultiply(A1_1 + A2_2, B1_1 + B2_2, threshold)
    M2 = strassenMultiply(A2_1 + A2_2, B1_1, threshold)
    M3 = strassenMultiply(A1_1, B1_2 - B2_2, threshold)
    M4 = strassenMultiply(A2_2, B2_1 - B1_1, threshold)
    M5 = strassenMultiply(A1_1 + A1_2, B2_2, threshold)
    M6 = strassenMultiply(A2_1 - A1_1, B1_1 + B1_2, threshold)
    M7 = strassenMultiply(A1_2 - A2_2, B2_1 + B2_2, threshold)
    
    C1_1 = M1 + M4 - M5 + M7
    C1_2 = M3 + M5
    C2_1 = M2 + M4
    C2_2 = M1 - M2 + M3 + M6
    
    C = np.zeros((n, n))
    C[:mid, :mid], C[:mid, mid:], C[mid:, :mid], C[mid:, mid:] = C1_1, C1_2, C2_1, C2_2
    
    return C

    
if __name__ == "__main__":
    sizes = [64,128,256,512]
    for n in sizes:

        A = []
        B = []

        for n2 in range(n):
            x = []
            for n3 in range(n):
                x.append(random.randrange(n))
            A.append(x)

        for n2 in range(n):
            x = []
            for n3 in range(n):
                x.append(random.randrange(n))
            B.append(x)
        
        A = np.array(A)
        B = np.array(B)

        time = timeit.default_timer()
        C1 = naiveMultiply(A, B)
        print(f"Naive Multiply: {abs(time - timeit.default_timer())}")

        time = timeit.default_timer()
        C2 = strassenMultiply(A, B)
        print(f"Strassen Multiply: {abs(time - timeit.default_timer())}")

        if C1.all() == C2.all():
            print("Matricies are equal.")
        else:
            print("Matrices are not equal.")