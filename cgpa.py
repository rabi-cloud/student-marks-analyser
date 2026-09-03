def calculate_cgpa():
    # Grade point mapping for common letter grades
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }

    try:
        num_courses = int(input("Enter the total number of courses: "))
        if num_courses <= 0:
            print("Please enter at least 1 course.")
            return

        total_weighted_points = 0.0
        total_credits = 0.0

        for i in range(1, num_courses + 1):
            print(f"\n--- Course {i} ---")
            
            # Input and validate letter grade
            while True:
                grade = input("Enter Grade (e.g., A+, B, C-): ").strip().upper()
                if grade in grade_points:
                    points = grade_points[grade]
                    break
                else:
                    print("Invalid grade! Please enter a valid letter grade (A+, A, A-, B+, etc.).")

            # Input and validate credits
            while True:
                try:
                    credits = float(input("Enter Credit Hours for this course: "))
                    if credits > 0:
                        break
                    else:
                        print("Credit hours must be greater than 0.")
                except ValueError:
                    print("Invalid input! Please enter a numeric value for credits.")

            total_weighted_points += points * credits
            total_credits += credits

        cgpa = total_weighted_points / total_credits
        
        print("\n" + "=" * 30)
        print(f"Total Credits: {total_credits:.1f}")
        print(f"Your calculated CGPA is: {cgpa:.2f}")
        print("=" * 30)

    except ValueError:
        print("Invalid input! Please enter valid integer numbers.")

if __name__ == "__main__":
    calculate_cgpa()