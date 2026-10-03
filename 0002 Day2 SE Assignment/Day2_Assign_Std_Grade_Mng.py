# Write a complete Python program to record and display student marks with these requirements:
#
# Set MAX_STUDENTS = 5 and use the title "Social Eagle - GenAI- Student Performance".
# Read all student names and marks in one line, in the format NAME,MARK; NAME,MARK.
# Allow names containing only letters, with a maximum length of 20 characters. Allow duplicate names.
# Accept marks from 0 to 100.
# Assign grades using this scale: 90–100 = A, 80–89 = B, 70–79 = C, 60–69 = D, and below 60 = E.
# Show an error’s type and details for invalid input, without crashing.
# Sort students by mark in descending order.
# Display the title in uppercase, centered above a neatly aligned table with columns for serial number, name, mark, and grade. Display all table text in uppercase and marks to two decimal places.
# Below the student rows, show the class average, highest mark, and lowest mark.
# If no valid student records are available, display a message instead of the table.
# Include clear comments and the full code.

MAX_STUDENTS = 5
TITLE = "Social Eagle - GenAI- Student Performance"
students = []


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    return "E"


# Read all student names and marks in one line.
try:
    entries = input(
        f"Enter students as NAME,MARK; NAME,MARK (up to {MAX_STUDENTS}): "
    ).split(";")

    if len(entries) > MAX_STUDENTS:
        raise ValueError(
            f"You can enter a maximum of {MAX_STUDENTS} students."
        )

    for entry in entries:
        name, mark_text = entry.split(",", maxsplit=1)
        name = name.strip()
        mark = float(mark_text.strip())

        if not name.isalpha() or len(name) > 20:
            raise ValueError(
                "Each name must contain only letters and be at most 20 characters."
            )

        if not 0 <= mark <= 100:
            raise ValueError("Each mark must be between 0 and 100.")

        students.append({
            "name": name,
            "mark": mark,
            "grade": get_grade(mark)
        })

except (ValueError, EOFError) as error:
    print(f"ERROR TYPE: {type(error).__name__}")
    print(f"DETAILS: {error}")
    students = []


# Sort and display the table if the input was valid.
if not students:
    print("No student records to display.")
else:
    students.sort(key=lambda student: student["mark"], reverse=True)

    serial_width = 6
    name_width = 20
    mark_width = 10
    grade_width = 10
    gap = "  "

    columns_width = (
        serial_width + name_width + mark_width + grade_width + len(gap) * 3
    )
    table_width = max(columns_width, len(TITLE))

    print("\n" + "=" * table_width)
    print(TITLE.upper().center(table_width))
    print("=" * table_width)

    print(
        f"{'S.NO.':<{serial_width}}{gap}"
        f"{'NAME':<{name_width}}{gap}"
        f"{'MARK':>{mark_width}}{gap}"
        f"{'GRADE':>{grade_width}}"
    )
    print("-" * table_width)

    for serial_number, student in enumerate(students, start=1):
        print(
            f"{serial_number:<{serial_width}}{gap}"
            f"{student['name'].upper():<{name_width}}{gap}"
            f"{student['mark']:>{mark_width}.2f}{gap}"
            f"{student['grade']:>{grade_width}}"
        )

    marks = [student["mark"] for student in students]
    summary_width = serial_width + len(gap) + name_width + len(gap)

    print("-" * table_width)
    print(
        f"{'CLASS AVERAGE':<{summary_width}}"
        f"{sum(marks) / len(marks):>{mark_width}.2f}"
    )
    print(f"{'HIGHEST MARK':<{summary_width}}{max(marks):>{mark_width}.2f}")
    print(f"{'LOWEST MARK':<{summary_width}}{min(marks):>{mark_width}.2f}")
    print("=" * table_width)