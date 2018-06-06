import json

d = dict(name='Bob', age=20, score=88)
jsonStr = json.dumps(d)
print(jsonStr)
e = json.loads(jsonStr)
print(e)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)

print(s.__dict__)
