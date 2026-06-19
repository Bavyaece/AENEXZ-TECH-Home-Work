def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    # Grade decision
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {round(average, 2)}")
    print(f"Grade: {grade}")

    # Find subjects below 40
    below_40 = []
    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1}")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")


def main():
    name = "Aarav"
    roll = 101
    marks = [88.5, 35.0, 76.0, 92.5, 48.0]
    analyze_result(name, roll, marks)


if __name__ == "__main__":
    main()
