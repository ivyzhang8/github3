
university = {
    "student1": {"Name": "Joe", "Age": 18, "Major": "Economics", "GPA": 3.0},
    "student2": {"Name": "Lily", "Age": 22, "Major": "Biology", "GPA": 3.2},
    "student3": {"Name": "Rachel", "Age": 24, "Major": "Psychology", "GPA": 3.3}
}

def display_students_info(university_dict):
    for details in university_dict.values():
        print(details['Name'], "-", details['Major'], "- Age:", details['Age'], "- GPA:", details['GPA'])

display_students_info(university)

