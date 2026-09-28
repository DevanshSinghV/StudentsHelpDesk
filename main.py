
class result:
    """Small value object for reporting the outcome of an operation.

    It replaces the usual placeholder/abstract result type with a concrete
    implementation that can be used by the command-line handlers.
    """

    def __init__(self, success, value=None, message=""):
        self.success = bool(success)
        self.value = value
        self.message = str(message)

    @classmethod
    def ok(cls, value=None, message=""):
        return cls(True, value, message)

    @classmethod
    def error(cls, message, value=None):
        return cls(False, value, message)

    def __bool__(self):
        return self.success

    def __str__(self):
        if self.message:
            return self.message
        return str(self.value) if self.value is not None else ("Success" if self.success else "Failure")

    def __repr__(self):
        return (
            f"result(success={self.success!r}, value={self.value!r}, "
            f"message={self.message!r})"
        )


class students:
    """Concrete student repository used by the command-line interface."""

    def __init__(self):
        self._students = []
        self._next_id = 1

    def register_student(self, name, email, branch, year):
        """Register and return a student record."""
        name = str(name).strip()
        email = str(email).strip()
        branch = str(branch).strip()
        year = str(year).strip()

        if not name or not email or not branch:
            return "Name, email, and branch are required."
        if year not in {"1", "2", "3", "4"}:
            return "Year must be between 1 and 4."
        if any(item["email"].lower() == email.lower() for item in self._students):
            return "A student with this email is already registered."

        student = {
            "student_id": self._next_id,
            "name": name,
            "email": email,
            "branch": branch,
            "year": year,
            "skills": [],
        }
        self._students.append(student)
        self._next_id += 1
        return "Student registered successfully"

    def get_all_students(self):
        return self._students.copy()

    def add_skill(self, student_id, skill):
        student = next(
            (item for item in self._students if item["student_id"] == student_id),
            None,
        )
        skill = str(skill).strip()
        if student is None:
            return "Student not found."
        if not skill:
            return "Skill cannot be empty."
        if skill.casefold() not in {item.casefold() for item in student["skills"]}:
            student["skills"].append(skill)
        return "Skill added successfully."

    def find_matching_students(self, skill, requester_id=None):
        skill = str(skill).strip().casefold()
        return [
            item for item in self._students
            if item["student_id"] != requester_id
            and any(value.casefold() == skill for value in item["skills"])
        ]


_student_repository = students()


def get_all_students():
    return _student_repository.get_all_students()


def register_student(name, email, branch, year):
    return _student_repository.register_student(name, email, branch, year)


def add_skill(student_id, skill):
    return _student_repository.add_skill(student_id, skill)


def find_matching_students(student_list, skill, requester_id=None):
    return [
        item for item in student_list
        if item["student_id"] != requester_id
        and any(value.casefold() == skill.strip().casefold() for value in item["skills"])
    ]


def show_menu():
    print("\n" + "=" * 45)
    print("      STUDENT HELPING SYSTEM")
    print("=" * 45)
    print("1. Register Student")
    print("2. View Students")
    print("3. Add Skill")
    print("4. Create Help Request")
    print("5. Accept Help Request")
    print("6. Study Calculus")
    print("7. Find Matching Students")
    
    print("8. Exit")


def view_students():
    students = get_all_students()
    if not students:
        print("No students registered yet.")
        return

    print("\n--- Students ---")
    for student in students:
        skills = ", ".join(student["skills"]) if student["skills"] else "No skill added"
        print(
            f"ID: {student['student_id']} | {student['name']} | "
            f"{student['branch']} | Year {student['year']} | Skills: {skills}"
        )


def create_help_request():
    try:
        student_id = int(input("Enter your student ID: "))
    except ValueError:
        print("Student ID must be a number.")
        return

    skill = input("What skill do you need help with? ").strip()
    description = input("Write your problem in one line: ").strip()
    result = create_request(student_id, skill, description)
    print(result)


def find_helpers():
    skill = input("Enter the skill you need: ").strip()
    try:
        requester_id = int(input("Enter your student ID: "))
    except ValueError:
        requester_id = None

    matches = find_matching_students(get_all_students(), skill, requester_id)
    if not matches:
        print("No matching student found.")
        return

    print("\n--- Matching Students ---")
    for student in matches:
        print(f"ID: {student['student_id']} | {student['name']} | {student['branch']} | Year {student['year']}")


def accept_help():
    try:
        request_id = int(input("Enter request ID: "))
        helper_id = int(input("Enter helper student ID: "))
    except ValueError:
        print("Request ID and student ID must be numbers.")
        return

    print(accept_request(request_id, helper_id))


def complete_help():
    try:
        request_id = int(input("Enter request ID: "))
        minutes = int(input("How many minutes was the help session? "))
    except ValueError:
        print("Please enter numbers only.")
        return

    print(complete_request(request_id, minutes))


def view_history():
    history = get_history()
    if not history:
        print("No completed help sessions yet.")
        return

    print("\n--- Help History ---")
    for item in history:
        print(
            f"Request {item['request_id']} | Requester: {item['requester_id']} | "
            f"Helper: {item['helper_id']} | Skill: {item['skill']} | "
            f"Time: {item['minutes']} minutes | Date: {item['completed_on']}"
        )


def Calculus():
    print("\n--- Learn Calculus ---")
    print("1. Module_1[Partial Derivatives] ")
    print("2. Module_2[Multiple Integrals]")
    print("3. Module_3[Vector Calculus]")
    print("4. Module_4[First Order Differential Equation]")
    print("5. Module_5[Second Order Differential Equation]")

    try:
        choice = int(input("Enter choice: ").strip())
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            branch = input("Enter branch: ").strip()
            year = input("Enter year (1-4): ").strip()
            print(register_student(name, email, branch, year))

        elif choice == "2":
            view_students()

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Student ID must be a number.")
                continue
            skill = input("Enter skill: ").strip()
            print(add_skill(student_id, skill))

        elif choice == "4":
            create_help_request()

        elif choice == "5":
            find_helpers()

        elif choice == "6":
            accept_help()

        elif choice == "7":
            complete_help()

        elif choice == "8":
            view_history()

        elif choice == "9":
            modules.array_analysis.show_array_analysis(get_all_students(), get_all_requests(), get_history())

        elif choice == "10":
            math_tools_menu()

        elif choice == "11":
            print("Thank you for using the Student Help Exchange System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 11.")


if __name__ == "__main__":
    main()
