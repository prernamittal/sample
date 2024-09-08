import random

def normalize_iq(iq):
    # Min is 70, Max is 150. Output should be 0 to 100
    return (iq - 70) * 100 / 90

def normalize_cgpa(cgpa):
    # Min is 6, Max is 10. Output should be 0 to 100
    return (cgpa - 6) * 100 / 4

def cost_function(cgpa, iq, w_cgpa, w_iq):
    # Output should be in the range of 0 to 100
    return (w_cgpa * normalize_cgpa(cgpa) + w_iq * normalize_iq(iq)) 

with open("dataset.csv", "w") as f:
    f.write("cgpa,iq,placement\n")
    
    placement_threshold = 50  # Lowering the threshold for more realistic results

    # Weight set 1: 0.6, 0.4
    for i in range(250):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        # Placement logic: lower threshold, tweak weights
        placement = 1 if cost_function(cgpa, iq, 0.6, 0.4) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    # Weight set 2: 0.5, 0.5
    for i in range(250):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.5, 0.5) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    # Weight set 3: 0.4, 0.6
    for i in range(250):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.4, 0.6) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    # Generate some outliers
    for i in range(20):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.8, 0.2) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    for i in range(20):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.9, 0.1) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    for i in range(20):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.2, 0.8) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    for i in range(20):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = 1 if cost_function(cgpa, iq, 0.1, 0.9) > placement_threshold else 0
        f.write(f"{cgpa},{iq},{placement}\n")

    # Generate some absolute random records 
    for i in range(20):
        cgpa = random.uniform(6, 10)
        iq = random.uniform(70, 150)
        placement = random.choice([0, 1])
        f.write(f"{cgpa},{iq},{placement}\n")
