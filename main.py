import random
import csv
from grades import letter_grade





def get_score():
    while True:
        try:
            i = int(input("what's your marks? "))
        except ValueError:
            print("error")
            continue
        if 0 <= i <= 100:
            return i
        else:
            print("error")

students = []

def add_student():
    name = input("what's your name? ")
    score = get_score()
    grade = letter_grade(score)
    students.append({"name": name, "score": score, "grade": grade})

def print_all():
    for student in students:
        print(student)

def class_average():
    if not students:
        print("No students to average.")
        return None
    total = sum(s["score"] for s in students)
    average = total / len(students)
    print(f"Class average: {average:.2f}")
    return average

def find_student():
    name = input("Student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(student)
            return
    print("student not found")

          
def student_of_the_day():
    if not students:
        print("No student.")
        return None
    print (random.choice(students))

def save_students(filename="students.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score", "grade"])
        writer.writeheader()
        for student in students:    
          writer.writerow(student)

def load_students(filename="students.csv"):
    students.clear()

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["score"] = int(row["score"])
                students.append(row)

    except FileNotFoundError:
        pass


def main():
    load_students()

    while True:
        print("\n1) Add student")
        print("2) View all")
        print("3) Class average")
        print("4) Find student")
        print("5) Student of the day")
        print("6) Save & quit")

        choice = input("> ")

        if choice == "1":
            add_student()

        elif choice == "2":
            print_all()

        elif choice == "3":
            class_average()

        elif choice == "4":
            find_student()

        elif choice == "5":
            student_of_the_day()

        elif choice == "6":
            save_students()
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()