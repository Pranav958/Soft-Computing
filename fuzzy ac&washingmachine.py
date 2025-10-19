import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def ac_controller():
    print("\n--- ROOM AIR CONDITIONER FUZZY CONTROL SYSTEM ---")

    # Define fuzzy variables
    temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 11, 1), 'humidity')
    fan_speed = ctrl.Consequent(np.arange(0, 6, 1), 'fan_speed')

    # Membership functions
    temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
    temperature['medium'] = fuzz.trimf(temperature.universe, [15, 25, 30])
    temperature['high'] = fuzz.trimf(temperature.universe, [25, 40, 40])

    humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 5])
    humidity['medium'] = fuzz.trimf(humidity.universe, [3, 5, 8])
    humidity['high'] = fuzz.trimf(humidity.universe, [5, 10, 10])

    fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 3])
    fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [1, 3, 4])
    fan_speed['high'] = fuzz.trimf(fan_speed.universe, [3, 5, 5])

    # Rules
    rule1 = ctrl.Rule(temperature['high'] | humidity['high'], fan_speed['high'])
    rule2 = ctrl.Rule(temperature['medium'] & humidity['medium'], fan_speed['medium'])
    rule3 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
    rule4 = ctrl.Rule(temperature['medium'] & humidity['high'], fan_speed['high'])
    rule5 = ctrl.Rule(temperature['high'] & humidity['low'], fan_speed['medium'])

    # Control system
    ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    ac_sim = ctrl.ControlSystemSimulation(ac_ctrl)

    # Take user input
    temp = float(input("Enter room temperature (0–40 °C): "))
    hum = float(input("Enter humidity (0–10): "))

    # Validate ranges
    temp = np.clip(temp, 0, 40) 
    hum = np.clip(hum, 0, 10)

    


    # Simulate
    ac_sim.input['temperature'] = temp
    ac_sim.input['humidity'] = hum
    ac_sim.compute()

    print(f"\n🌡️ Temperature: {temp} °C")
    print(f"💧 Humidity: {hum} %")
    print(f"🌀 Recommended Fan Speed: {ac_sim.output['fan_speed']:.2f} ")

    fan_speed.view(sim=ac_sim)
    plt.show()


def washing_machine_controller():
    print("\n--- WASHING MACHINE FUZZY CONTROL SYSTEM ---")

    # Define fuzzy variables
    dirt = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt')
    load = ctrl.Antecedent(np.arange(0, 11, 1), 'load')
    wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')

    # Membership functions
    dirt['low'] = fuzz.trimf(dirt.universe, [0, 0, 5])
    dirt['medium'] = fuzz.trimf(dirt.universe, [2, 5, 8])
    dirt['high'] = fuzz.trimf(dirt.universe, [5, 10, 10])

    load['light'] = fuzz.trimf(load.universe, [0, 0, 5])
    load['medium'] = fuzz.trimf(load.universe, [2, 5, 8])
    load['heavy'] = fuzz.trimf(load.universe, [5, 10, 10])

    wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 0, 30])
    wash_time['normal'] = fuzz.trimf(wash_time.universe, [15, 30, 45])
    wash_time['long'] = fuzz.trimf(wash_time.universe, [30, 60, 60])

    # Rules
    rule1 = ctrl.Rule(dirt['high'] | load['heavy'], wash_time['long'])
    rule2 = ctrl.Rule(dirt['medium'] & load['medium'], wash_time['normal'])
    rule3 = ctrl.Rule(dirt['low'] & load['light'], wash_time['short'])
    rule4 = ctrl.Rule(dirt['medium'] & load['heavy'], wash_time['long'])
    rule5 = ctrl.Rule(dirt['high'] & load['light'], wash_time['normal'])

    # Control system
    wash_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    wash_sim = ctrl.ControlSystemSimulation(wash_ctrl)

    # Take user input
    dirt_val = float(input("Enter dirtiness level (0–10): "))
    load_val = float(input("Enter load weight level (0–10): "))

    # Validate ranges
    dirt_val = np.clip(dirt_val, 0, 10)
    load_val = np.clip(load_val, 0, 10)

    # Simulate
    wash_sim.input['dirt'] = dirt_val
    wash_sim.input['load'] = load_val
    wash_sim.compute()

    print(f"\n🧺 Dirtiness Level: {dirt_val}")
    print(f"⚖️ Load Weight Level: {load_val}")
    print(f"⏱️ Recommended Wash Time: {wash_sim.output['wash_time']:.2f} minutes")

    wash_time.view(sim=wash_sim)
    plt.show()


# -------- MAIN MENU ---------
def main():
    while True:
        print("\n========== FUZZY CONTROL SYSTEM ==========")
        print("1. Room Air Conditioner Controller")
        print("2. Washing Machine Controller")
        print("3. Exit")

        choice = input("Select system (1/2/3): ").strip()

        if choice == '1':
            ac_controller()
        elif choice == '2':
            washing_machine_controller()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()

