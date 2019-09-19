from tabulate import tabulate


class StudentInfo:
    def __init__(self, id, full_name, special, english, philosophy, ind_achievements, point, category, document,
                 status):
        self.id = str_to_int(id)
        self.full_name = full_name
        self.__subjects = (special, english, philosophy, ind_achievements)
        self.scores = list(map(str_to_int, self.__subjects))
        self.point = sum(self.scores) if not point.isdigit() else int(point)
        self.category = category
        self.document = document
        self.status = status
        self.ranked = None
        self.__special, self.__english, self.__philosophy, self.__ind_achievements = self.scores

    def __iter__(self):
        for value in self.get_list_attr():
            yield value

    def get_list_attr(self):
        # return list(self.__dict__.values())
        return self.ranked, self.id, self.full_name, self.__special, self.__english, self.__philosophy, self.__ind_achievements, \
               self.point, self.category, self.document, self.status


def decorator_function(func):
    def wrapper(*args):
        print('\nGet ranked...')
        for goal_student in args[1]:
            func(args[0], goal_student['id'], goal_student['full_name'])

    return wrapper


def str_to_int(string):
    if string is None:
        return None
    elif type(string) is int:
        return string
    elif type(string) is str:
        if string.isdigit():
            return int(string)
        else:
            return 0
    else:
        raise Exception('Error in fun: str_to_int!')


def get_rating_list(students, output=False):
    top = sorted(students, key=lambda student: student.point, reverse=True)
    for student, rank in zip(top, [count for count in range(1, len(top) + 1)]):
        student.ranked = rank

    print_table(top) if output else None
    return top


@decorator_function
def get_ranked(students, id=None, full_name=None):
    students = get_rating_list(students, output=False)
    if id is None and full_name is None:
        raise Exception('ID and Full name do not None!')

    id = str_to_int(id)
    for student in students:
        if student.id == id or student.full_name == full_name:
            print(f'{student.full_name} ({student.id}) has rank {student.ranked}')
            break


def print_table(students):
    headers = ['Rank', 'No', 'Full_name', 'SS', 'English', 'Philosophy', 'Achievements', 'Total_points', 'Category',
               'Document', 'Status']
    print(tabulate(students, headers=headers))


if __name__ == '__main__':
    test_data = ['1', '-']
    for item in test_data:
        temp = str_to_int(item)
