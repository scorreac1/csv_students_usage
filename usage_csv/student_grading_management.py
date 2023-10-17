from functions.functions import write_csv, summary, bar_plot_students, input_data, input_string, index_error_input, create_students, create_students_csv, import_excel, assign_course, bar_plot
from classes.my_class import Course, Student
import os

def main():
    courses = []
    iterar = True
    while iterar:
        action = input_data('\n Enter a number depending on which option you want the program to run:\
                            \n 1. Create a new course. \n 2. Enter the students data. \
                            \n 3. Higher and lower score students. \n 4. Look for a student\'s grade. \
                            \n 6. Export to excel. \n 7. Build a bar chart of a course \
                            \n 8. Exit the program \n The chosen option is: ')
        if action == 1:
            course_name = input_string('Enter the Course\'s name: ')
            course_id = input_data('Enter the Course\'s id: ')
            new_course = Course(course_name, course_id)
            courses.append(new_course)
        elif action == 2 and len(courses) > 0:
            for course in courses:
                print(course.name)
            where_from = index_error_input('\n How do you want to input the data \n 1. From a .csv. \
                                           \n 2. Manually through this menu. \n The chosen option is: ', 1, 2)
            if where_from == 1:
                specific_course = assign_course(courses, 'To which course do you want to add new students?: ')
                csv_contents = create_students_csv()
                specific_course.update_students(csv_contents)
            elif where_from == 2:
                specific_course = assign_course(courses, 'To which course do you want to add new students?: ')
                specific_course.update_students(create_students())
        elif action == 3 and len(courses) > 0:
            for course in courses:
                print(course.name)
            specific_course = assign_course(courses, 'For which course do you want to see the best and worst students?: ')
            specific_course.higher_score()
            specific_course.lower_score()            
        elif action == 4:
            for course in courses:
                print(course.name)
            specific_course = assign_course(courses, 'From which course do you want to know the student\'s grade?: ')
            student_name = input_string('Enter the name of the student whose grade you want to know. ')
            if specific_course != None:
                grade = specific_course.look_for_student_grade(student_name)
                print(f'{student_name}\'s gpa is {grade}')
        elif action == 5:
            summary(assign_course(courses, 'Which course\'s summary would you like to see?: '))
        elif action == 6:
            file_name = input_string('Enter the name of the new file: ')
            specific_course = assign_course(courses, 'Which course do you want to add to the file?: ')
            write_csv(specific_course,file_name)
        elif action == 7:
            bar_plot_students(assign_course(courses, 'Which course would you like to plot?: '))
        elif action == 8:
            iterar = False
        else:
            print('Not valid')
            
main()

os.system('clear')