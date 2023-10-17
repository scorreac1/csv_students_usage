from classes.my_class import Course, Student
import matplotlib.pyplot as plt

def input_data(message):
    try:
        needed_data = float(input(message))
        return needed_data
    except ValueError:
        print('ValueError, try again.')
        return input_data(message)
    
def input_string(message):
    needed_data = input(message)
    return needed_data
    # funcion por complementar

def type_conversion(convert_to, data):
    if convert_to.lower() == 'float':
        try:
            return float(data)
        except ValueError:
            return 0.0
    elif convert_to.lower() == 'integer':
        try:
            return int(data)
        except ValueError:
            return 0
    elif convert_to.lower() == 'string':
        try:
            return str(data)
        except ValueError:
            return '0'

def display_students(student_list):
    for i in student_list:
        print(f'The student {i[0]} with id {i[1]} is currently in the {i[2]} program and has a GPA {i[3]}.')

def search_id(student_list):
    look_for_this_id = input_data('Input the id of the student you want to look for: ')
    for i in student_list:
        if i[1] == look_for_this_id:
            print(f"The id {look_for_this_id} matches with {i[0]}'s id. He is currently in the {i[2]} program and has a GPA of {i[3]}")

def index_error_input(string, start, end):
    index = input_data(string)
    while index < start or index > end:
        index = input_data(string)
    return index

def import_excel():
    a = input_string('Enter the file with the .csv extension: ')
    file = open('/Users/scorrea/dev/riwi_practicing/review/usage_csv/'+ a, 'r')
    line_list = file.readlines()
    return line_list

def create_students_csv():
    student_list = []
    line_list = import_excel()
    lista = line_list[1:]                       # I dont want to take the headers
    for linea in lista:
        student_information = linea.split(',')
        new_student = Student(student_information[0], type_conversion('integer',student_information[1]), type_conversion('float',student_information[2].split('\n')[0]))
        student_list.append(new_student)
    return student_list

def create_students():
    new_student = Student(name=input_string('Enter the student\'s name: '), id=input_data('Enter the student\'s id: '), gpa=input_data('Enter the student\'s gpa: '))
    return [new_student]

def assign_course(courses, string):
    what_course = input_string(string)
    for course in courses:
        if course.name == what_course:
            return(course)

def bar_plot(x_axis, y_label):    
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot
    plt.bar(x_axis, y_label, color ='maroon', width = 0.4)
    plt.xlabel("Students")
    plt.ylim(0,5.0)
    plt.ylabel("Score")
    plt.title("Students - Score")
    plt.show()

def bar_plot_students(course):
    names = []
    grades = []
    for student in course.students:
        names.append(student.name)
        grades.append(student.gpa)
    bar_plot(names, grades)


def write_csv(course, file_name):
    file = open(file_name, 'a+')
    for student in course.students:
        file.write(f'{student.name},{student.id},{student.gpa}\n')

def summary(course):
    print(f'The ammount of students in the {course.name} course is {len(course.students)}') 
    print(f'The average grade in the {course.name} {course.average_score()}')
    course.higher_score()
    course.lower_score()  