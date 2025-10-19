def display_set(name, fset):
    print(f"{name} = {{ " + ", ".join([f"{x}:{m}" for x, m in fset.items()]) + " }}")

def union(A,B):
    print("\nFormula: μA∪B(x) = max(μA(x), μB(x))")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(max(A.get(x,0),B.get(x,0)),3) for x in set(A)|set(B)}
    display_set("Union", result); return result

def intersection(A,B):
    print("\nFormula: μA∩B(x) = min(μA(x), μB(x))")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(min(A.get(x,0),B.get(x,0)),3) for x in set(A)|set(B)}
    display_set("Intersection", result); return result

def complement(A,name="Set"):
    print(f"\nFormula: μ{name}ᶜ(x) = 1 - μ{name}(x)")
    display_set(name, A)
    result = {x:round(1-m,3) for x,m in A.items()}
    display_set(f"{name} Complement", result); return result

def algebraic_sum(A,B):
    print("\nFormula: μA⊕B(x) = μA(x) + μB(x) - μA(x)μB(x)")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(A.get(x,0)+B.get(x,0)-A.get(x,0)*B.get(x,0),3) for x in set(A)|set(B)}
    display_set("Algebraic Sum", result); return result

def algebraic_product(A,B):
    print("\nFormula: μA⊗B(x) = μA(x) * μB(x)")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(A.get(x,0)*B.get(x,0),3) for x in set(A)|set(B)}
    display_set("Algebraic Product", result); return result

def bounded_sum(A,B):
    print("\nFormula: μA⊞B(x) = min(1, μA(x)+μB(x))")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(min(1,A.get(x,0)+B.get(x,0)),3) for x in set(A)|set(B)}
    display_set("Bounded Sum", result); return result

def bounded_product(A,B):
    print("\nFormula: μA⊠B(x) = max(0, μA(x)+μB(x)-1)")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(max(0,A.get(x,0)+B.get(x,0)-1),3) for x in set(A)|set(B)}
    display_set("Bounded Product", result); return result

def drastic_sum(A,B):
    print("\nFormula: μA⊕dB(x) = { B(x) if A(x)=0 ; A(x) if B(x)=0 ; 1 otherwise }")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:(B.get(x,0) if A.get(x,0)==0 else (A.get(x,0) if B.get(x,0)==0 else 1)) for x in set(A)|set(B)}
    display_set("Drastic Sum", result); return result

def drastic_product(A,B):
    print("\nFormula: μA⊗dB(x) = { A(x) if B(x)=1 ; B(x) if A(x)=1 ; 0 otherwise }")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:(A.get(x,0) if B.get(x,0)==1 else (B.get(x,0) if A.get(x,0)==1 else 0)) for x in set(A)|set(B)}
    display_set("Drastic Product", result); return result

def hamacher_sum(A,B,gamma):
    print(f"\nFormula: μA⊕hB(x) = (μA+μB - (2-γ)μAμB) / (1 - (1-γ)μAμB)")
    display_set("Set A", A); display_set("Set B", B)
    result={}
    for x in set(A)|set(B):
        a,b=A.get(x,0),B.get(x,0)
        denom=1-(1-gamma)*a*b
        val= (a+b-(2-gamma)*a*b)/denom if denom!=0 else 1
        result[x]=round(val,3)
    display_set("Hamacher Sum", result); return result

def hamacher_product(A,B,gamma):
    print(f"\nFormula: μA⊗hB(x) = (ab) / (γ + (1-γ)(a+b-ab))")
    display_set("Set A", A); display_set("Set B", B)
    result={}
    for x in set(A)|set(B):
        a,b=A.get(x,0),B.get(x,0)
        denom=gamma+(1-gamma)*(a+b-a*b)
        val= (a*b)/denom if denom!=0 else 0
        result[x]=round(val,3)
    display_set("Hamacher Product", result); return result

def bounded_difference(A,B):
    print("\nFormula: μA−B(x) = max(0, μA(x) - μB(x))")
    display_set("Set A", A); display_set("Set B", B)
    result = {x:round(max(0,A.get(x,0)-B.get(x,0)),3) for x in set(A)|set(B)}
    display_set("Bounded Difference", result); return result
    

def t_norm(A,B): return intersection(A,B)
def t_conorm(A,B): return union(A,B)


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
    print("\n--- Fuzzy Set Operations Menu ---")
    print("1. Union\n2. Intersection\n3. Complement")
    print("4. Algebraic Sum\n5. Algebraic Product")
    print("6. Bounded Sum\n7. Bounded Product")
    print("8. Drastic Sum\n9. Drastic Product")
    print("10. Hamacher Sum\n11. Hamacher Product")
    print("12. Bounded Difference\n13. T-norm\n14. T-conorm\n15. Exit")
    display_set("Set A", setA); display_set("Set B", setB)
    choice=int(input("Enter your choice: "))
    if choice==1: union(setA,setB)
    elif choice==2: intersection(setA,setB)
    elif choice==3: complement(setA,"Set A"); complement(setB,"Set B")
    elif choice==4: algebraic_sum(setA,setB)
    elif choice==5: algebraic_product(setA,setB)
    elif choice==6: bounded_sum(setA,setB)
    elif choice==7: bounded_product(setA,setB)
    elif choice==8: drastic_sum(setA,setB)
    elif choice==9: drastic_product(setA,setB)
    elif choice==10: 
        gamma=float(input("Enter γ (0-1): "))
        hamacher_sum(setA,setB,gamma)
    elif choice==11: 
        gamma=float(input("Enter γ (0-1): "))
        hamacher_product(setA,setB,gamma)
    elif choice==12: bounded_difference(setA,setB);bounded_difference(setB,setA)
    elif choice==13: t_norm(setA,setB)
    elif choice==14: t_conorm(setA,setB)
    elif choice==15: break
    else: print("Invalid choice!")
