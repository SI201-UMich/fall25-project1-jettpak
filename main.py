# Name: Jessica Park
# Student ID: #4603 7241
# 3747 7615
# 2568 0286
# Email: jessicp@umich.edu
# donmoses@umich.edu
# mingyaom@umich.edu
# Collaborators: Mig Yao Ming, Donovan Moses
# AI Tools Used: Microsoft Copilot for debugging and help with questions, ChatGPT 5 to help with debugging
# - Ming: load_data, calculate_avg_flipper_length, calculate_avg_body_mass, write_results
# - Jessica: bill_length, bill_depth
# - Donovan: sex percentage, species yield

import csv

def load_data(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def calculate_avg_flipper_length(data):
    lengths = []
    for row in data:
        value = row['flipper_length_mm']
        if value and value != 'NA':
            lengths.append(float(value))
    return round(sum(lengths) / len(lengths), 2) if lengths else 0

def calculate_avg_body_mass(data):
    masses = []
    for row in data:
        value = row['body_mass_g']
        if value and value != 'NA':
            masses.append(float(value))
    return round(sum(masses) / len(masses), 2) if masses else 0

# SECTION FOR JESSICA
# def calculate_avg_bill_length(data):
def calculate_avg_bill_length(data):
    lengths = []
    for row in data:
        value = row.get('bill_length_mm')
        if value and value != 'NA':
            try:
                lengths.append(float(value))
            except ValueError:
                continue
    return round(sum(lengths) / len(lengths), 2) if lengths else 0


# def calculate_avg_bill_depth(data):
def calculate_avg_bill_depth(data):
    depths = []
    for row in data:
        value = row.get('bill_depth_mm')
        if value and value != 'NA':
            try:
                depths.append(float(value))
            except ValueError:
                continue
    return round(sum(depths) / len(depths), 2) if depths else 0        


# SECTION FOR DONOVAN
def calculate_male_percentage(data):
    males = 0
    known = 0
    for row in data:
        sex = row.get('sex')
        if sex and sex != 'NA':
            known += 1
            if sex.strip().lower() == 'male':
                males += 1
    return round((males / known) * 100, 2) if known else 0

# def calculate_species_yield(data):
def calculate_species_yield(data):
    species_stats = {} 
    for row in data:
        species = row.get('species')
        mass = row.get('body_mass_g')
        if not species or species == 'NA' or not mass or mass == 'NA':
            continue
        try:
            mass = float(mass)
        except ValueError:
            continue

        if species not in species_stats:
            species_stats[species] = [0, 0]

        species_stats[species][1] += 1
        if mass > 5000:
            species_stats[species][0] += 1

    return {
        species: round((heavy / total) * 100, 2) if total else 0
        for species, (heavy, total) in species_stats.items()
    }
def run_tests(data):
    print("Running test cases...")

    # Ming's tests
    assert calculate_avg_flipper_length(data) > 180
    assert calculate_avg_body_mass(data) > 3000

    empty_data = []
    assert calculate_avg_flipper_length(empty_data) == 0 if empty_data else True
    assert calculate_avg_body_mass(empty_data) == 0 if empty_data else True

    # Jessica's tests
    assert calculate_avg_bill_length(data) > 30
    assert calculate_avg_bill_depth(data) > 10

    empty_data = []
    assert calculate_avg_bill_length(empty_data) == 0 if empty_data else True
    assert calculate_avg_bill_depth(empty_data) == 0 if empty_data else True

    # SECTION FOR DONOVAN TESTS
    data = load_data("data/penguins.csv")
    male_pct = calculate_male_percentage(data)
    species_yield = calculate_species_yield(data)
    assert 40 <= male_pct <= 60, f"Unexpected male percentage: {male_pct}"
    assert "Gentoo" in species_yield and species_yield["Gentoo"] > 40
    assert "Adelie" in species_yield and species_yield["Adelie"] < 10
    assert "Chinstrap" in species_yield

    print("All tests passed.")

def main():
    data = load_data("data/penguins.csv")

    avg_flipper = calculate_avg_flipper_length(data)
    avg_mass = calculate_avg_body_mass(data)

    avg_bill_length = calculate_avg_bill_length(data)
    avg_bill_depth = calculate_avg_bill_depth(data)

    # SECTION FOR DONOVAN
    male_pct = calculate_male_percentage(data)
    species_yield_pct = calculate_species_yield(data)

    results = {
        "Average Flipper Length (mm)": avg_flipper,
        "Average Body Mass (g)": avg_mass,
        "Average Bill Length (mm)": avg_bill_length,
        "Average Bill Depth (mm)": avg_bill_depth,
        "Male Percentage": male_pct,
        "Species Yield > 5t/ha": species_yield_pct
    }

    write_results(results, "output/results.txt")
    run_tests(data)

def write_results(results, filename):
    with open(filename, "w") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()
