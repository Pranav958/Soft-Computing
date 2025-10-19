import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def washing_machine_controller_dynamic():
    print("\n--- WASHING MACHINE FUZZY CONTROL SYSTEM (DYNAMIC RANGE) ---")

    # 🧩 User-defined ranges
    dirt_min = float(input("Enter MIN dirtiness level: "))
    dirt_max = float(input("Enter MAX dirtiness level: "))
    load_min = float(input("Enter MIN load level: "))
    load_max = float(input("Enter MAX load level: "))

    # Define fuzzy variables
    dirt = ctrl.Antecedent(np.arange(dirt_min, dirt_max + 0.1, 0.1), 'dirt')
    load = ctrl.Antecedent(np.arange(load_min, load_max + 0.1, 0.1), 'load')
    wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')

    # Dynamic membership functions
    d_range = dirt_max - dirt_min
    dirt['low'] = fuzz.trimf(dirt.universe, [dirt_min, dirt_min, dirt_min + d_range / 2.5])
    dirt['medium'] = fuzz.trimf(dirt.universe, [dirt_min + d_range / 4, dirt_min + d_range / 2, dirt_min + 3 * d_range / 4])
    dirt['high'] = fuzz.trimf(dirt.universe, [dirt_min + d_range / 2, dirt_max, dirt_max])

    l_range = load_max - load_min
    load['light'] = fuzz.trimf(load.universe, [load_min, load_min, load_min + l_range / 2.5])
    load['medium'] = fuzz.trimf(load.universe, [load_min + l_range / 4, load_min + l_range / 2, load_min + 3 * l_range / 4])
    load['heavy'] = fuzz.trimf(load.universe, [load_min + l_range / 2, load_max, load_max])

    # Output membership functions (fixed in minutes)
    wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 0, 30])
    wash_time['normal'] = fuzz.trimf(wash_time.universe, [15, 30, 45])
    wash_time['long'] = fuzz.trimf(wash_time.universe, [30, 60, 60])

    # Fuzzy rules
    rule1 = ctrl.Rule(dirt['high'] | load['heavy'], wash_time['long'])
    rule2 = ctrl.Rule(dirt['medium'] & load['medium'], wash_time['normal'])
    rule3 = ctrl.Rule(dirt['low'] & load['light'], wash_time['short'])
    rule4 = ctrl.Rule(dirt['medium'] & load['heavy'], wash_time['long'])
    rule5 = ctrl.Rule(dirt['high'] & load['light'], wash_time['normal'])

    # Build and simulate
    wash_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    wash_sim = ctrl.ControlSystemSimulation(wash_ctrl)

    # 🧍 User enters actual condition
    dirt_val = float(input(f"\nEnter current dirtiness level ({dirt_min}–{dirt_max}): "))
    load_val = float(input(f"Enter current load level ({load_min}–{load_max}): "))

    # Clip inputs to defined ranges
    dirt_val = np.clip(dirt_val, dirt_min, dirt_max)
    load_val = np.clip(load_val, load_min, load_max)

    # Simulate
    wash_sim.input['dirt'] = dirt_val
    wash_sim.input['load'] = load_val
    wash_sim.compute()

    print(f"\n🧺 Dirtiness: {dirt_val}")
    print(f"⚖️ Load: {load_val}")
    print(f"⏱️ Recommended Wash Time: {wash_sim.output['wash_time']:.2f} minutes")

    wash_time.view(sim=wash_sim)
    plt.show()

# Run
if __name__ == "__main__":
    washing_machine_controller_dynamic()
