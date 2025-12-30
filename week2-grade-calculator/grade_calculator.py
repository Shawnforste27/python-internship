# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Author: Your Name Here

def calculate_grade(average):
    """Return grade letter and comment based on average"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """Validate numeric input within a range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")


def grade_color(grade):
    """Add color coding for grades"""
    colors = {
        'A': '\033[92m',  # Green
        'B': '\033[94m',  # Blue
        'C': '\033[93m',  # Yellow
        'D': '\033[91m',  # Red
        'F': '\033[41m',  # Red background
    }
    reset = '\033[0m'
    return colors.get(grade, '') + grade + reset


def save_results(student_names, student_results):
    """Save results to file"""
    with open("results_sample.txt", "w") as file:
        file.write("Name,Average,Grade,Comment\n")
        for i in range(len(student_names)):
            r = student_results[i]
            file.write(f"{student_names[i]},{r['average']:.1f},{r['grade']},{r['comment']}\n")


def search_student(student_names, student_results):
    """Search for a student by name"""
    name = input("\nEnter student name to search: ").strip()
    if name in student_names:
        index = student_names.index(name)
        r = student_results[index]
        print(f"\n{name}'s Result:")
        print(f"Average: {r['average']:.1f}")
        print(f"Grade: {r['grade']}")
        print(f"Comment: {r['comment']}")
    else:
        print("Student not found.")


def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Validate number of students
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Enter a whole number.")

    student_names = []
    student_results = []

    # Collect data
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")

        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Student name: ").strip()

        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_names.append(name)
        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    # Display results
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^7} | Comment")
    print("-" * 65)

    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        colored_grade = grade_color(grade)

        print(f"{name:<20} | {avg:>5.1f} | {colored_grade:^7} | {comment}")

    # Class statistics
    averages = [r['average'] for r in student_results]
    class_avg = sum(averages) / len(averages)

    print("\n" + "=" * 50)
    print("          CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students: {num_students}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max(averages):.1f} ({student_names[averages.index(max(averages))]})")
    print(f"Lowest Average: {min(averages):.1f} ({student_names[averages.index(min(averages))]})")

    # Extra features
    search_student(student_names, student_results)
    save_results(student_names, student_results)

    print("\nResults saved to results_sample.txt")
    print("Thank you for using the Grade Calculator!")


if __name__ == "__main__":
    main()
