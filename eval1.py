
students = {}

def add_student(student_id, name, student_class, grades):
    
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
        return

    students[student_id] = {
        'name': name,
        'class': student_class,
        'grades': grades
    }
    print(f"Student {name} added successfully.")

def update_grades(student_id, new_grades):
   
    if student_id not in students:
        print(f"Student with ID {student_id} not found.")
        return

    students[student_id]['grades'] = new_grades
    print(f"Grades for student ID {student_id} updated successfully.")

def calculate_average(student_id):
   
    if student_id not in students:
        print(f"Student with ID {student_id} not found.")
        return None

    grades = students[student_id]['grades']
    if not grades:
        print(f"No grades available for student ID {student_id}.")
        return None

    average = sum(grades) / len(grades)
    return average


add_student('001', 'Yash', 'Math', [90, 85, 92])
add_student('002', 'Himashu', 'Math', [78, 81, 88])
add_student('003', 'Om', 'Science', [85, 90, 87])

update_grades('001', [95, 90, 93])

print(f"Yash average grade: {calculate_average('001')}")
print(f"Hiamsnhu average grade: {calculate_average('002')}")



