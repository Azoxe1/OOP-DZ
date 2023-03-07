class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lest(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.rating[course] = grade
            
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {(sum(self.grades.values())) / (len(self.grades.keys()))} \n Курсы в процессе изучения: {(','.join(self.courses_in_progress))} \n Завершенные курсы: {(','.join(self.finished_courses))} "
        
    def __lt__(self, which):
        if not isinstance (which, Student):
            print('Ошибка')
            return
        return (sum(self.grades.values())) / (len(self.grades.keys())) < (sum(which.grades.values())) / (len(which.grades.keys()))
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = grade
        else:
            return 'Ошибка'
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rating = {}
    
    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {(sum(self.rating.values())) / (len(self.rating.keys()))}"
    
    def __lt__(self, which):
        if not isinstance (which, Lecturer):
            print('Ошибка')
            return
        return (sum(self.rating.values())) / (len(self.rating.keys())) < (sum(self.rating.values())) / (len(self.rating.keys()))
        
 
       
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)
    
    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname}"

def average_grade_stud (stud_list, course):
    counter = []
    for i in stud_list:
        if isinstance (i, Student) and course in i.courses_in_progress:
            counter.append((sum(i.grades.values())) / (len(i.grades.keys())))
        else:
            return "Ошибка"
    av_counter = ((sum(counter)/ len(counter)))
    # print(av_counter)
    return av_counter

def average_grade_lect (lect_list, course):
    counter = []
    for i in lect_list:
        if isinstance (i, Lecturer) and course in i.courses_attached:
            counter.append((sum(i.rating.values())) / (len(i.rating.keys())))
        else:
            return "Ошибка"
    av_counter = ((sum(counter)/ len(counter)))
    # print(av_counter)
    return av_counter


first_stud = Student('Nikita', 'Gorshenov', 'male')
second_stud = Student('Youra', 'Hoi', 'male')

first_lecturer = Lecturer('Sponge', 'Bob')
second_lecturer = Lecturer ('Zele', 'Boba')

first_reviever = Reviewer('2', 'Pac')
second_reviever = Reviewer ('Amog', 'Us')

first_stud.courses_in_progress += ['Python']
second_stud.courses_in_progress += ['Python']
first_stud.finished_courses += ['Dish washing']
second_stud.finished_courses += ['Ice cubing']

first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Python']

first_reviever.courses_attached += ['Python']
second_reviever.courses_attached += ['Python']

first_stud.rate_lest (first_lecturer, 'Python', 10) 
second_stud.rate_lest (first_lecturer, 'Python', 5)
first_stud.rate_lest (second_lecturer, 'Python', 8) 
second_stud.rate_lest (second_lecturer, 'Python', 8)

first_reviever.rate_hw (first_stud, 'Python', 10)
second_reviever.rate_hw (first_stud, 'Python', 5)
first_reviever.rate_hw (second_stud, 'Python', 6)
second_reviever.rate_hw (second_stud, 'Python', 9)

python_studs = [first_stud, second_stud]
python_lect = [first_lecturer, second_lecturer]

# average_grade_stud (python_studs, 'Python')      
# average_grade_lect (python_lect, 'Python')  
# print(first_lecturer)
# print(first_stud)
# print(second_lecturer)
# print(second_stud)
# print(first_stud < second_stud)
# print(first_lecturer < second_lecturer)