class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

class Course:
    def __init__(self, name, id, students = []):
        self.students = students
        self.name = name
        self.id = id
    
    def show_students(self):
        students_name = []
        if len(self.students) > 0:
            for student in self.students:
                students_name.append(student.name)
            return students_name
        else:
            return None

    def update_students(self, student_list):
        self.students = self.students + student_list

    def average_score(self):
        avg = 0
        for student in self.students:
            avg += student.gpa
        avg = avg/len(self.students)
        return avg

    def higher_score(self):
        high_score_students = [self.students[0]]
        for student in self.students:
            if student.gpa > high_score_students[0].gpa:
                high_score_students.clear()
                high_score_students.append(student)
            elif student.gpa == high_score_students[0].gpa and student != high_score_students[0]:
                high_score_students.append(student)
        for i in high_score_students:
            print(f'The best grade is from {i.name} with a {i.gpa}')
        return high_score_students

    def lower_score(self):
        low_score_students = [self.students[0]]
        for student in self.students:
            if student.gpa < low_score_students[0].gpa:
                low_score_students.clear()
                low_score_students.append(student)
            elif student.gpa == low_score_students[0].gpa and student != low_score_students[0]:
                low_score_students.append(student)
        for i in low_score_students:
            print(f'The worst grade is from {i.name} with a {i.gpa}')
        return low_score_students
    
    def look_for_student_grade(self, student_name):
        for student in self.students:
            if student_name.lower() == student.name.lower():
                return student.gpa
            else:
                return 'Student not found'