def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

def main():
    print("--- 🎓 Student Grade Analyzer ---")
    
    sub1 = float(input("Enter marks for Subject 1: "))
    sub2 = float(input("Enter marks for Subject 2: "))
    sub3 = float(input("Enter marks for Subject 3: "))
    
    total = sub1 + sub2 + sub3
    percentage = (total / 300) * 100
    
    grade = calculate_grade(percentage)
    
    print("\n--- Results ---")
    print(f"Total Marks: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Final Grade: {grade}")

if __name__ == "__main__":
    main()
