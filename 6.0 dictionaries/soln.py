from prettytable import PrettyTable
import os
import csv
from datetime import datetime

MAIN_TITLE = """
  ____                _        __  __                                   
 / ___|_ __ __ _  __| | ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |  _| '__/ _` |/ _` |/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_| | | | (_| | (_| |  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   
 \____|_|  \__,_|\__,_|\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                         |___/            
"""

CSV_FILE = 'students.csv'

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_csv():
    """Create CSV file if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'grade1', 'grade2', 'grade3', 'date_added'])

def validate_name(name):
    """Validate that name contains only letters and spaces."""
    return name.replace(' ', '').isalpha()

def validate_grade(grade):
    """Validate that grade is between 0 and 100."""
    try:
        grade = float(grade)
        return 0 <= grade <= 100
    except ValueError:
        return False

def get_grade_letter(grade):
    """Convert numerical grade to letter grade."""
    if grade >= 90: return 'A'
    elif grade >= 80: return 'B'
    elif grade >= 70: return 'C'
    elif grade >= 60: return 'D'
    else: return 'F'

def add_student():
    """Add a new student to the system."""
    clear_screen()
    print("\n=== Add New Student ===")
    
    while True:
        name = input("Enter student name (letters only): ").strip()
        if not validate_name(name):
            print("Error: Name must contain only letters and spaces.")
            continue
            
        # Check if student already exists
        with open(CSV_FILE, 'r') as file:
            if any(name == row[0] for row in csv.reader(file)):
                print("Error: Student already exists.")
                continue
        
        break
    
    # Add student with empty grades
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, '', '', '', datetime.now().strftime('%Y-%m-%d')])
    print(f"\nStudent '{name}' added successfully!")
    input("\nPress Enter to continue...")

def view_students():
    """Display all students and their grades."""
    clear_screen()
    print("\n=== Student List ===")
    
    table = PrettyTable()
    table.field_names = ["Name", "Grade 1", "Grade 2", "Grade 3", "Average", "Date Added"]
    
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                grades = [float(g) for g in row[1:4] if g]
                avg = sum(grades) / len(grades) if grades else 0
                table.add_row([
                    row[0],
                    row[1] if row[1] else 'N/A',
                    row[2] if row[2] else 'N/A',
                    row[3] if row[3] else 'N/A',
                    f"{avg:.1f}" if grades else 'N/A',
                    row[4]
                ])
    except FileNotFoundError:
        print("No students found.")
        return
    
    print(table)
    input("\nPress Enter to continue...")

def add_grade():
    """Add or update a student's grade."""
    clear_screen()
    print("\n=== Add Grade ===")
    
    # Show existing students
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        students = list(reader)
    
    if not students:
        print("No students found. Please add students first.")
        input("\nPress Enter to continue...")
        return
    
    print("\nAvailable students:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student[0]}")
    
    while True:
        try:
            choice = int(input("\nSelect student number: ")) - 1
            if not 0 <= choice < len(students):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please try again.")
    
    student = students[choice]
    print(f"\nCurrent grades for {student[0]}:")
    print(f"Grade 1: {student[1] if student[1] else 'N/A'}")
    print(f"Grade 2: {student[2] if student[2] else 'N/A'}")
    print(f"Grade 3: {student[3] if student[3] else 'N/A'}")
    
    while True:
        grade_num = input("\nWhich grade to add/update (1-3)? ")
        if grade_num not in ['1', '2', '3']:
            print("Invalid grade number. Please enter 1, 2, or 3.")
            continue
            
        grade = input("Enter grade (0-100): ")
        if not validate_grade(grade):
            print("Invalid grade. Please enter a number between 0 and 100.")
            continue
            
        break
    
    # Update grade in CSV
    students[choice][int(grade_num)] = grade
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'grade1', 'grade2', 'grade3', 'date_added'])
        writer.writerows(students)
    
    print("\nGrade updated successfully!")
    input("\nPress Enter to continue...")

def view_reports():
    """Display grade distribution and statistics."""
    clear_screen()
    print("\n=== Grade Reports ===")
    
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            students = list(reader)
    except FileNotFoundError:
        print("No data available.")
        input("\nPress Enter to continue...")
        return
    
    # Calculate grade distribution
    grades = []
    for student in students:
        for grade in student[1:4]:
            if grade:
                grades.append(float(grade))
    
    if not grades:
        print("No grades available.")
        input("\nPress Enter to continue...")
        return
    
    # Calculate statistics
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Count grade letters
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        grade_counts[get_grade_letter(grade)] += 1
    
    # Display statistics
    print(f"\nClass Statistics:")
    print(f"Average Grade: {avg:.1f}")
    print(f"Highest Grade: {highest:.1f}")
    print(f"Lowest Grade: {lowest:.1f}")
    
    # Display grade distribution
    print("\nGrade Distribution:")
    for grade, count in grade_counts.items():
        print(f"{grade}: {'█' * count} ({count})")
    
    input("\nPress Enter to continue...")

def main_menu():
    """Display main menu and handle user input."""
    while True:
        clear_screen()
        print(MAIN_TITLE)
        print("""
    ===== STUDENT GRADE MANAGER =====
    1. Add Student
    2. View Students
    3. Add Grade
    4. View Reports
    5. Exit
    ================================
    """)
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            view_reports()
        elif choice == '5':
            clear_screen()
            print("\nThank you for using Grade Manager!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    initialize_csv()
    main_menu()