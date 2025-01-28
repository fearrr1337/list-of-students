#bookList = ["история", "математика", "русский язык"]
#print(bookList[1])
import cmath

studentList = ["Вася", "Петя", "Игорь", "Леша"]
ratingList = ["2", "3", "4", "5"]

while True:
    answer = int(input('Выберите действие:\n'
                       '1 - добавить студента\n'
                       '2 - удалить студента по индексу\n'
                       '3 - посмотреть весь список студентов\n'
                       '4 - удалить студента по имени\n'
                       '0 - выйти из программы\n'))
    if answer not in [1,2,3,4,0]:
        print('Такой команды нет')
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        studentList.append(newStudent)
    elif answer == 2:
        deleteStudent = int(input('Введите номер студента для удаления: '))
        studentList.pop(deleteStudent)
    elif answer == 3:
        print(studentList)
    elif answer == 4:
        deleteStudent = input('Введите имя студента которого хотите удалить: ')
        studentList.remove(deleteStudent)
    elif answer == 0:
        break



