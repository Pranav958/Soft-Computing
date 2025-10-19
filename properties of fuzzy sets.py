def display(fset, name):
    print(f"{name} = {{ " + ", ".join([f"{x}:{m}" for x,m in fset.items()]) + " }}")

def is_equal(setA, setB):
    print("\nFormula: A = B ⇔ μA(x) = μB(x) ∀x")
    display(setA,"Set A"); display(setB,"Set B")
    return all(round(setA.get(x,0),3) == round(setB.get(x,0),3) for x in set(setA)|set(setB))

def is_included(setA, setB):
    print("\nFormula: A ⊆ B ⇔ μA(x) ≤ μB(x) ∀x")
    display(setA,"Set A"); display(setB,"Set B")
    return all(round(setA.get(x,0),3) <= round(setB.get(x,0),3) for x in set(setA)|set(setB))

def cardinality(fset):
    print("\nFormula: |A| = Σ μA(x)")
    display(fset,"Set")
    return round(sum(fset.values()),3)

def is_empty(fset):
    print("\nFormula: Empty ⇔ μA(x)=0 ∀x")
    display(fset,"Set")
    return all(round(m,3)==0 for m in fset.values())

def alpha_cut(fset, alpha):
    print(f"\nFormula: α-cut(A) = {{ x | μA(x) ≥ {alpha} }}")
    display(fset,"Set")
    return [x for x,m in fset.items() if round(m,3)>=alpha]

def is_normal(fset):
    print("\nFormula: Normal ⇔ max μA(x) = 1")
    display(fset,"Set")
    return round(max(fset.values()),3)==1

def height(fset):
    print("\nFormula: height(A) = max μA(x)")
    display(fset,"Set")
    return round(max(fset.values()),3)

def core(fset):
    print("\nFormula: core(A) = { x | μA(x) = 1 }")
    display(fset,"Set")
    return [x for x,m in fset.items() if round(m,3)==1]

def support(fset):
    print("\nFormula: support(A) = { x | μA(x) > 0 }")
    display(fset,"Set")
    return [x for x,m in fset.items() if round(m,3)>0]

def is_singleton(fset):
    print("\nFormula: Singleton ⇔ only one element with μA(x) > 0")
    display(fset,"Set")
    return sum(1 for m in fset.values() if round(m,3)>0)==1

print("Enter elements and membership values for Fuzzy Set A:")
n1=int(input("How many elements in Set A? "))
setA={}
for _ in range(n1):
    x=input("Element: "); m=float(input("Membership (0-1): "))
    setA[x]=round(m,3)

print("\nEnter elements and membership values for Fuzzy Set B:")
n2=int(input("How many elements in Set B? "))
setB={}
for _ in range(n2):
    x=input("Element: "); m=float(input("Membership (0-1): "))
    setB[x]=round(m,3)


while True:
    print("\n--- Fuzzy Set Properties Menu ---")
    print("1. Display Set A and B\n2. Equality of A and B\n3. Inclusion (A ⊆ B ?)")
    print("4. Cardinality of A and B\n5. Check Empty Set\n6. α-cut")
    print("7. Normality & Height\n8. Core\n9. Support\n10. Check Singleton\n11. Exit")
    display(setA,"Set A"); display(setB,"Set B")
    choice=int(input("Enter your choice: "))
    if choice==1: display(setA,"Set A"); display(setB,"Set B")
    elif choice==2: print("Sets are Equal" if is_equal(setA,setB) else "Sets are NOT Equal")
    elif choice==3: print("A ⊆ B" if is_included(setA,setB) else "A is NOT a subset of B")
    elif choice==4:
        print("Cardinality of A:",cardinality(setA))
        print("Cardinality of B:",cardinality(setB))
    elif choice==5:
        print("Set A is Empty" if is_empty(setA) else "Set A is NOT Empty")
        print("Set B is Empty" if is_empty(setB) else "Set B is NOT Empty")
    elif choice==6:
        alpha=float(input("Enter α (0-1): "))
        print(f"α-cut of A:",alpha_cut(setA,alpha))
        print(f"α-cut of B:",alpha_cut(setB,alpha))
    elif choice==7:
        print("Set A is Normal" if is_normal(setA) else "Set A is NOT Normal")
        print("Height of A:",height(setA))
        print("Set B is Normal" if is_normal(setB) else "Set B is NOT Normal")
        print("Height of B:",height(setB))
    elif choice==8:
        print("Core of A:",core(setA))
        print("Core of B:",core(setB))
    elif choice==9:
        print("Support of A:",support(setA))
        print("Support of B:",support(setB))
    elif choice==10:
        print("Set A is Singleton" if is_singleton(setA) else "Set A is NOT Singleton")
        print("Set B is Singleton" if is_singleton(setB) else "Set B is NOT Singleton")
    elif choice==11: break
    else: print("Invalid choice!")
