class Person:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_surname_initials(self):
        return f'{self.surname} {self.name[0]}. {self.patronymic[0]}.'

    def set_name(self, new_name):
        self.name = new_name


class Student(Person):
    def __init__(self, name, patronymic, surname, class_room, parents):
        Person.__init__(self, name, patronymic, surname)
        self.class_room = class_room
        self.parents = parents


class Teacher(Person):
    def __init__(self, name, patronymic, surname, teach_subject):
        Person.__init__(self, name, patronymic, surname)
        self.teach_subject = teach_subject


class Class_room:
    def __init__(self, class_room, teachers):
        self._class_room = {'class_num': int(class_room.split()[0]), 'class_char': class_room.split()[1]}
        self.teachers_dict = {t.teach_subject: t for t in teachers}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1


teachers = [Teacher('Александр', 'Александрович', 'Александров', 'информатика'),
            Teacher('Борис', 'Борисович', 'Борисов', 'математика'),
            Teacher('Виктор', 'Викторович', 'Викторенко', 'физика'),
            Teacher('Григорий', 'Григорьевич', 'Гришин', 'информатика'),
            Teacher('Дмитрий', 'Денисович', 'Данилов', 'математика'),
            Teacher('Евгений', 'Егорович', 'Егоров', 'информатика'),
            Teacher('Жанна', 'Жаковна', 'Жулебина', 'математика'),
            Teacher('Зинаида', 'Зурабовна', 'Зимова', 'физика')]

class_rooms = [Class_room('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_room('11 Б', [teachers[3], teachers[1], teachers[2]]),
               Class_room('10 А', [teachers[5], teachers[4], teachers[2]]),
               Class_room('9 А', [teachers[5], teachers[6], teachers[7]]),
               Class_room('9 Б', [teachers[0], teachers[6], teachers[7]])]

parents = [Person("Игорь", "Игоревич", "Игоренко"),
           Person("Инна", "Ивановна", "Игоренко"),
           Person("Константин", "Константинович", "Костин"),
           Person("Карина", "Константиновна", "Костина"),
           Person('Леонид', 'Леонидович', 'Леоньтев'),
           Person('Любовь', 'Леонидовна', 'Леоньтева'),
           Person('Марина', 'Матвеевна', 'Марьина')]
students = [
    Student("Иван", "Игоревич", "Игоренко", class_rooms[0], [parents[0], parents[1]]),
    Student("Илья", "Игоревич", "Игоренко", class_rooms[0], [parents[0], parents[1]]),
    Student("Ксения", "Константиновна", "Костина", class_rooms[1], [parents[2], parents[3]]),
    Student("Лера", "Леонидовна", "Леонтьева", class_rooms[2], [parents[4], parents[5]]),
    Student("Михаил", "Маратович", "Марьин", class_rooms[3], [parents[6]]),
    Student("Надежда", "Николаевна", "Набокова", class_rooms[3], []),
    Student("Ольга", "Олеговна", "Останкина", class_rooms[4], [])]
print('1. Полный список всех классов школы')
for cl in class_rooms:
    print(cl.class_room)
print()

def get_list_students(class_room):
    return [st.get_surname_initials() for st in students if st.class_room == class_room]

print('2. Список всех учеников в', class_rooms[3].class_room)
print(get_list_students(class_rooms[0]))
print()

print('3. Список всех предметов ученика', students[0].get_surname_initials())
for subject in students[0].class_room.teachers_dict.keys():
    print(subject)

print()

print('4. ФИО родителей ученика', students[0].get_surname_initials())
for parent in students[0].parents:
    print(parent.get_full_name())
print()

print('5. Список учителей в классе', class_rooms[3].class_room)
for teacher in class_rooms[0].teachers_dict.values():
    print(teacher.get_full_name())
