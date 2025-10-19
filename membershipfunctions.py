import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def triangular_mf():
    a = float(input("Enter 'a' (start): "))
    b = float(input("Enter 'b' (peak): "))
    c = float(input("Enter 'c' (end): "))
    x = np.linspace(a, c, 200)
    y = fuzz.trimf(x, [a, b, c])
    plt.plot(x, y)
    plt.title(f"Triangular Membership Function [{a}, {b}, {c}]")
    plt.xlabel("Input")
    plt.ylabel("Membership Degree")
    plt.grid(True)
    plt.show()

def trapezoidal_mf():
    a = float(input("Enter 'a' (start): "))
    b = float(input("Enter 'b' (left top start): "))
    c = float(input("Enter 'c' (right top end): "))
    d = float(input("Enter 'd' (end): "))
    x = np.linspace(a, d, 200)
    y = fuzz.trapmf(x, [a, b, c, d])
    plt.plot(x, y)
    plt.title(f"Trapezoidal Membership Function [{a}, {b}, {c}, {d}]")
    plt.xlabel("Input")
    plt.ylabel("Membership Degree")
    plt.grid(True)
    plt.show()

def gaussian_mf():
    mean = float(input("Enter 'mean': "))
    sigma = float(input("Enter 'sigma' (spread): "))
    x = np.linspace(mean - 4*sigma, mean + 4*sigma, 200)
    y = fuzz.gaussmf(x, mean, sigma)
    plt.plot(x, y)
    plt.title(f"Gaussian Membership Function (mean={mean}, sigma={sigma})")
    plt.xlabel("Input")
    plt.ylabel("Membership Degree")
    plt.grid(True)
    plt.show()

def bell_mf():
    a = float(input("Enter 'a' (width): "))
    b = float(input("Enter 'b' (slope): "))
    c = float(input("Enter 'c' (center): "))
    x = np.linspace(c - 4*a, c + 4*a, 200)
    y = fuzz.gbellmf(x, a, b, c)
    plt.plot(x, y)
    plt.title(f"Generalized Bell Membership Function (a={a}, b={b}, c={c})")
    plt.xlabel("Input")
    plt.ylabel("Membership Degree")
    plt.grid(True)
    plt.show()

def sigmoid_mf():
    b = float(input("Enter 'b' (slope): "))
    c = float(input("Enter 'c' (center): "))
    x = np.linspace(c - 10, c + 10, 200)
    y = fuzz.sigmf(x, b, c)
    plt.plot(x, y)
    plt.title(f"Sigmoid Membership Function (b={b}, c={c})")
    plt.xlabel("Input")
    plt.ylabel("Membership Degree")
    plt.grid(True)
    plt.show()

# === MAIN LOOP ===
while True:
    print("\n==== FUZZY MEMBERSHIP FUNCTION MENU ====")
    print("1. Triangular Membership Function")
    print("2. Trapezoidal Membership Function")
    print("3. Gaussian Membership Function")
    print("4. Generalized Bell Membership Function")
    print("5. Sigmoid Membership Function")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ").strip()

    if choice == '1':
        triangular_mf()
    elif choice == '2':
        trapezoidal_mf()
    elif choice == '3':
        gaussian_mf()
    elif choice == '4':
        bell_mf()
    elif choice == '5':
        sigmoid_mf()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")
