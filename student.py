import csv
import json
import os
import re
import shutil

list_of_students = []
path_to_dir = "C:/Users/Andreea/PycharmProjects/SDA/Algoritmi_si_structuri_de_date/2023_03_18/Student"
json_path = f"{path_to_dir}/Json files"
csv_path = f"{path_to_dir}/CSV files"

def create_student():
    id = input(f"ID: ")
    surname = input(f"Surname: ")
    name = input(f"Name: ")
    age = input(f"Age: ")
    occupation = input(f"Occupation: ")
    hobby = input(f"Hobby: ")
    email = input(f"Email: ")
    while not re.search(r'^[a-z][a-z0-9]+[._]*[a-z0-9]*[._]*[a-z0-9]*[._]*[a-z0-9]*[@]\D+[.]\D{2,3}$', email):
        print("Please enter a valid email. Ex.: username@domainname.top-leveldomain")
        email = input(f"Email: ")
    phone = input(f"Phone: ")
    while not re.match(r'^07[0-9]{8}', phone):
        print("Please enter a valid phone number that starts with '07'.")
        phone = input(f"Phone: ")


    student_details = {
        "ID": id,
        "Surname": surname,
        "Name": name,
        "Age": age,
        "Occupation": occupation,
        "Hobby": hobby,
        "Email": email,
        "Phone": phone
    }
    return student_details

def add_student_to_list():
    student_details = create_student()
    list_of_students.append(student_details)
    return list_of_students

def save_student_to_json():
    if not os.path.exists(json_path):
        os.makedirs(json_path)

    for filename in os.listdir(json_path):
        file_path = os.path.join(json_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for student in list_of_students:
        filename = f'{json_path}/Json_{student["ID"]}.json'
        with open(filename, "w") as f:
            f.write(json.dumps(student, indent=4))
    with open(f'{json_path}/MasterJson.json', 'w') as m:
        m.write(json.dumps(list_of_students, indent=4))

def save_student_to_csv():
    if not os.path.exists(csv_path):
        os.makedirs(csv_path)

    for filename in os.listdir(csv_path):
        file_path = os.path.join(csv_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for student in list_of_students:
        filename = f'{csv_path}/CSV_{student["ID"]}.csv'
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=student.keys())
            writer.writeheader()
            writer.writerow(student)
    with open(f'{csv_path}/MasterCSV.csv', 'w') as m:
        writer = csv.DictWriter(m, fieldnames=["ID", "Surname", "Name", "Age", "Occupation", "Hobby", "Email", "Phone"])
        writer.writeheader()
        writer.writerows(list_of_students)


while True:
        ans = input("Want to add a student? y/n: ").lower()
        if ans == "y":
            add_student_to_list()
        elif ans == 'n':
            break
        else:
            print("The answer should be y or n.")

save_student_to_json()
save_student_to_csv()
