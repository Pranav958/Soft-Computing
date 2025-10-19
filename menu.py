import numpy as np

def max_min(R, S):
    """Max-Min Composition"""
    m, n = R.shape
    n2, p = S.shape
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            result[i, j] = max(min(R[i, k], S[k, j]) for k in range(n))
    return result.round(2)

def max_product(R, S):
    """Max-Product Composition"""
    m, n = R.shape
    n2, p = S.shape
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            result[i, j] = max(R[i, k] * S[k, j] for k in range(n))
    return result.round(2)

def max_average(R, S):
    """Max-Average Composition"""
    m, n = R.shape
    n2, p = S.shape
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            result[i, j] = max((R[i, k] + S[k, j]) / 2 for k in range(n))
    return result.round(2)


# ---------------- Main Program ----------------
print("Enter dimensions of first matrix R (m x n):")
m, n = map(int, input().split())
print(f"Enter the {m}x{n} matrix R (row by row):")
R = np.array([list(map(float, input().split())) for _ in range(m)])

print("\nEnter dimensions of second matrix S (n x p):")
n2, p = map(int, input().split())
if n != n2:
    print("Error: Inner dimensions must match (R: m×n, S: n×p)")
    exit()

print(f"Enter the {n}x{p} matrix S (row by row):")
S = np.array([list(map(float, input().split())) for _ in range(n)])
while True:
    print("\n--- Fuzzy Relation Composition Menu ---")
    print("1. Max-min Composition\n2. Max-product Composition\n3. Max-average Composition\n4.Exit")
  # Compute compositions
    print("\nMatrix R:\n", R)
    print("Matrix S:\n", S)
    choice=int(input("Enter your choice: "))
    if choice==1: print("Max-Min Composition:\n", max_min(R, S))
    elif choice==2: print("\nMax-Product Composition:\n", max_product(R, S))
    elif choice==3: print("\nMax-Average Composition:\n", max_average(R, S))
    elif choice==4: break
    else: print("Invalid choice!")






