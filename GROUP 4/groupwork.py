from collections import deque
from datetime import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.assignments = []

    def add_assignment(self, assignment_name, submission_time):
        self.assignments.append((assignment_name, submission_time))

class SubmissionTracker:
    def __init__(self):
        self.students = []
        self.submission_queue = deque()
        self.undo_stack = []

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)
        print(f"Added student: {name} (ID: {student_id})")

    def submit_assignment(self, student_id, assignment_name):
        submission_time = datetime.now().strftime("%I:%M %p")
        student = self.find_student(student_id)

        if student:
            
            if any(a[0] == assignment_name for a in student.assignments):
                print(f"Assignment '{assignment_name}' has already been submitted by {student.name}.")
                return

            student.add_assignment(assignment_name, submission_time)
            self.submission_queue.append((student_id, student.name, assignment_name, submission_time))
            self.undo_stack.append((student_id, assignment_name, submission_time))
            print(f"Submitted: {assignment_name} by {student.name} at {submission_time}")
        else:
            print("Student not found.")

    def undo_submission(self):
        if self.undo_stack:
            student_id, assignment_name, submission_time = self.undo_stack.pop()
            self.remove_submission(student_id, assignment_name)
            print(f"Undid submission: {assignment_name} by Student ID: {student_id}")
        else:
            print("No submissions to undo.")

    def remove_submission(self, student_id, assignment_name):
        student = self.find_student(student_id)
        if student:
            student.assignments = [a for a in student.assignments if a[0] != assignment_name]
            self.submission_queue = deque(
                (sid, sname, aname, stime) for sid, sname, aname, stime in self.submission_queue if aname != assignment_name
            )

    def remove_last_submission(self, student_id):
        
        for i in range(len(self.submission_queue) - 1, -1, -1):
            if self.submission_queue[i][0] == student_id:
            
                submission = self.submission_queue[i]
                self.submission_queue.remove(submission)

                
                student = self.find_student(student_id)
                if student:
                    student.assignments = [
                        a for a in student.assignments if a[0] != submission[2]
                    ]
                
                print(f"Removed last submission: {submission[2]} by Student ID: {student_id}")
                return
        
        print("No submissions found for this student ID.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_submissions(self):
        print("\nCurrent Submission Queue:")
        print(f"{'Student ID':<12} {'Student Name':<20} {'Assignment':<25} {'Submission Time'}")
        print("-" * 80)

        for student_id, student_name, assignment_name, submission_time in self.submission_queue:
            print(f"{student_id:<12} {student_name:<20} {assignment_name:<25} {submission_time}")

def main():
    tracker = SubmissionTracker()

    while True:
        print("\nOptions:")
        print("1.  push operation for Add Student in list" )
        print("2. Enqueue operation for  Submit Assignment accord to student id in Queue")
        print("3. pop operation access Last Submission  in stack ")
        print("4. Display all  Submission using queue")
        print("5. Dequeue operation by removing Submission reference to student id  using queue")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                tracker.add_student(student_id, name)
            except ValueError:
                print("Invalid input for Student ID. Please enter a number.")

        elif choice == '2':
            try:
                student_id = int(input("Enter Student ID: "))
                assignment_name = input("Enter Assignment Name: ")
                tracker.submit_assignment(student_id, assignment_name)
            except ValueError:
                print("Invalid input for Student ID. Please enter a number.")

        elif choice == '3':
            tracker.undo_submission()

        elif choice == '4':
            tracker.display_submissions()

        elif choice == '5':
            try:
                student_id = int(input("Enter Student ID to remove last submission: "))
                tracker.remove_last_submission(student_id)
            except ValueError:
                print("Invalid input for Student ID. Please enter a number.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
