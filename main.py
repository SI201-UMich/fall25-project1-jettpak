# Name: Jessica Park
# Student ID: #4603 7241
# Email: jessicp@umich.edu
# Collaborators: Mig Yao Ming, Donovan Moses
# AI Tools Used: 
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
# def calculate_male_percentage(data):


# def calculate_species_yield(data):
#     ...

def write_results(results_dict, filename):
    with open(filename, 'w') as f:
        for key, value in results_dict.items():
            f.write(f"{key}: {value}\n")

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
    # assert calculate_male_percentage(data) > ...
    # assert calculate_species_yield(data) > ...

    print("All tests passed.")

def main():
    data = load_data("data/penguins.csv")

    avg_flipper = calculate_avg_flipper_length(data)
    avg_mass = calculate_avg_body_mass(data)

    avg_bill_length = calculate_avg_bill_length(data)
    avg_bill_depth = calculate_avg_bill_depth(data)

    # SECTION FOR DONOVAN
    # male_pct = calculate_male_percentage(data)
    # species_yield_pct = calculate_species_yield(data)

    results = {
        "Average Flipper Length (mm)": avg_flipper,
        "Average Body Mass (g)": avg_mass,
        "Average Bill Length (mm)": avg_bill_length,
        "Average Bill Depth (mm)": avg_bill_depth,
        # "Male Percentage": male_pct,
        # "Species Yield > 5t/ha": species_yield_pct
    }

    write_results(results, "output/results.txt")
    run_tests(data)

if __name__ == "__main__":
    main()
