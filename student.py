import csv
import json
import os

list_of_students = []
path_to_dir = input("Enter path: ")
json_path = f"{path_to_dir}/Json files"
csv_path = f"{path_to_dir}/CSV files"

def create_student():
    id = input(f"ID: ")
    surname = input(f"Surname: ")
    name = input(f"Name: ")
    age = int(input(f"Age: "))
    occupation = input(f"Occupation: ")
    hobby = input(f"Hobby: ")
    email = input(f"Email: ")
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
    for student in list_of_students:
        filename = f'{json_path}/Json_{student["ID"]}.json'
        with open(filename, "w") as f:
            f.write(json.dumps(student, indent=4))
    with open(f'{json_path}/MasterJson.json', 'w') as m:
        m.write(json.dumps(list_of_students, indent=4))

def save_student_to_csv():
    if not os.path.exists(csv_path):
        os.makedirs(csv_path)
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
