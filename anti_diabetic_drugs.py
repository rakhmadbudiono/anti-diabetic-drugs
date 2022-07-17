import csv

with open('data.csv') as f:
    a = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('2_combination.csv') as f:
    two_combination = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('3_combination.csv') as f:
    three_combination = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

def data_per_patient():
    patients = {}
    for item in a:
        if item['No'] not in patients:
            patients[item['No']] = []

        patients[item['No']].append(item)

    return patients

patients = data_per_patient()

import pandas as pd

def array_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename)

def process_two_combination():
    data = []

    for combination in two_combination:
        count = 0
        for patient_number in patients:
            first_found = False
            second_found = False

            for first_iter in patients[patient_number]:
                if first_iter['Kode ATC'] == combination['first']:
                    first_found = True
                    break
            for second_iter in patients[patient_number]:
                if second_iter['Kode ATC'] == combination['second']:
                    second_found = True
                    break

            if first_found and second_found: count += 1

        data.append([count])

    array_to_csv(data, '2_combination_result.csv')

process_two_combination()

def process_three_combination():
    data = []

    for combination in three_combination:
        count = 0
        for patient_number in patients:
            first_found = False
            second_found = False
            third_found = False

            for first_iter in patients[patient_number]:
                if first_iter['Kode ATC'] == combination['first']:
                    first_found = True
                    break
            for second_iter in patients[patient_number]:
                if second_iter['Kode ATC'] == combination['second']:
                    second_found = True
                    break
            for third_iter in patients[patient_number]:
                if third_iter['Kode ATC'] == combination['third']:
                    third_found = True
                    break

            if first_found and second_found and third_found: count += 1

        data.append([count])

    array_to_csv(data, '3_combination_result.csv')

process_three_combination()