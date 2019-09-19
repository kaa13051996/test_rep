class BeautifulSoupIterator:
    def __init__(self, obj):
        self.iter = iter(obj)

    def __iter__(self):
        return self

    def __next__(self):
        next(self.iter)
        return next(self.iter)


if __name__ == '__main__':
    example = [1, 2, 3, 4, 5]

    for student in BeautifulSoupIterator(example):
        print(student)
