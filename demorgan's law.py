# Demonstrating De Morgan's Law in Fuzzy Sets with User Input

def fuzzy_not(setA):
    """Negation of a fuzzy set"""
    return {x: round(1 - mu,2) for x, mu in setA.items()}

def fuzzy_and(setA, setB):
    """Intersection of two fuzzy sets"""
    return {x: min(setA[x], setB[x]) for x in setA|setB}

def fuzzy_or(setA, setB):
    """Union of two fuzzy sets"""
    return {x: max(setA[x], setB[x]) for x in setA|setB}


# Input universe size
n = int(input("Enter the number of elements: "))

# Input fuzzy set A
A = {}
print("\nEnter membership values for fuzzy set A (between 0 and 1):")
for i in range(1, n + 1):
    A[i] = float(input(f"Membership of element {i} in A: "))
    

# Input fuzzy set B
B = {}
print("\nEnter membership values for fuzzy set B (between 0 and 1):")
for i in range(n):
    
    B[i] = float(input(f"Membership of element {i} in B: "))
    

print("\nFuzzy Set A:", A)
print("Fuzzy Set B:", B)

# De Morgan's Law 1: NOT(A AND B) = (NOT A) OR (NOT B)
lhs1 = fuzzy_not(fuzzy_and(A, B))
rhs1 = fuzzy_or(fuzzy_not(A), fuzzy_not(B))

# De Morgan's Law 2: NOT(A OR B) = (NOT A) AND (NOT B)
lhs2 = fuzzy_not(fuzzy_or(A, B))
rhs2 = fuzzy_and(fuzzy_not(A), fuzzy_not(B))

print("\n--- De Morgan's Law Verification ---")
print("\nA AND B:", fuzzy_and(A, B))
print("\nNOT (A AND B):", lhs1)
print("\nNOT A:",fuzzy_not(A))
print("\nNOT B:",fuzzy_not(B))
print("\n(NOT A) OR (NOT B):", rhs1)
print("\nEqual?", all(abs(lhs1[x] - rhs1[x]) < 1e-6 for x in lhs1))
print("\n A OR B:",fuzzy_or(A,B))
print("\nNOT (A OR B):", lhs2)
print("\nNOT A:",fuzzy_not(A))
print("\nNOT B:",fuzzy_not(B))
print("(NOT A) AND (NOT B):", rhs2)
print("Equal?", all(abs(lhs2[x] - rhs2[x]) < 1e-6 for x in lhs2))
