# Write a complete Python program for student performance tracking.
# Follow these requirements and code details:
#
# Set MAX_STUDENTS = 5.
# Set TITLE = "Social Eagle - GenAI- Student Performance".
# Set OUTPUT_FILE = "SE_Performance.txt".
# Initialize an empty list named students.
#
# Define get_grade(mark) with a docstring saying it returns a grade based on the student's mark.
# Use these grade rules:
#   90 or higher: A
#   80–89: B
#   70–79: C
#   60–69: D
#   Below 60: E
#
# Read all student records in one input line, with records separated by semicolons.
# Format each record as NAME,MARK.
# Use an f-string in the input prompt to show the current MAX_STUDENTS.
#
# Raise a ValueError if the number of entries exceeds MAX_STUDENTS.
# Use an f-string in the error message to show the maximum.
#
# For each entry, split the name and mark at the first comma.
# Strip whitespace from both values and convert the mark to a float.
#
# Accept names only if they contain letters and are no longer than 20 characters.
# Use name.isalpha() and len(name) > 20 for validation.
# Accept marks from 0 through 100 inclusive.
#
# Store each valid student as a dictionary with "name", "mark", and "grade" keys.
#
# Catch ValueError and EOFError, print the exception type and details,
# and clear the student list after an error.
#
# If there are no student records, print:
# No student records to display.
#
# Otherwise, sort students by mark in descending order.
#
# Format the report using a lines list.
# Use column widths of 6 for serial number, 20 for name, 10 for mark,
# and 10 for grade, with a two-space gap between columns.
# Calculate table width as the larger of the total column width and the title length.
#
# Center the uppercase title between lines of = characters.
# Use S.NO., NAME, MARK, and GRADE as uppercase column headings.
#
# Display each student with a serial number starting at 1,
# uppercase name and grade, and mark formatted to two decimal places.
#
# Add summary rows for class average, highest mark, and lowest mark.
# Format marks to two decimal places.
#
# Join the report lines with newline characters and print the report.
# Save it to SE_Performance.txt using UTF-8 encoding and write mode.
# Finally, print a confirmation message showing the output filename.
#
# Include the comments described above.
# Return only the complete Python code, without explanation.

MAX_STUDENTS = 5
TITLE = "Social Eagle - GenAI- Student Performance"
OUTPUT_FILE = "SE_Performance.txt"
students = []


def get_grade(mark):
    """Return a grade based on the student's mark."""
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


if not students:
    print("No student records to display.")
else:
    # Sort students by mark, from highest to lowest.
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

    # Build the report so it can be printed and saved.
    lines = [
        "=" * table_width,
        TITLE.upper().center(table_width),
        "=" * table_width,
        (
            f"{'S.NO.':<{serial_width}}{gap}"
            f"{'NAME':<{name_width}}{gap}"
            f"{'MARK':>{mark_width}}{gap}"
            f"{'GRADE':>{grade_width}}"
        ),
        "-" * table_width,
    ]

    for serial_number, student in enumerate(students, start=1):
        lines.append(
            f"{serial_number:<{serial_width}}{gap}"
            f"{student['name'].upper():<{name_width}}{gap}"
            f"{student['mark']:>{mark_width}.2f}{gap}"
            f"{student['grade']:>{grade_width}}"
        )

    # Add the class average, highest mark, and lowest mark.
    marks = [student["mark"] for student in students]
    summary_width = serial_width + len(gap) + name_width + len(gap)

    lines.extend([
        "-" * table_width,
        (
            f"{'CLASS AVERAGE':<{summary_width}}"
            f"{sum(marks) / len(marks):>{mark_width}.2f}"
        ),
        f"{'HIGHEST MARK':<{summary_width}}{max(marks):>{mark_width}.2f}",
        f"{'LOWEST MARK':<{summary_width}}{min(marks):>{mark_width}.2f}",
        "=" * table_width,
    ])

    report = "\n".join(lines)

    # Show the report in the notebook and save it to SE_Performance.txt.
    print(report)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nResults saved to: {OUTPUT_FILE}")