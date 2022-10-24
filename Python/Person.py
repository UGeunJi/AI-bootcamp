class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        
    def greeting(self):
        print(self.hello)
        print("저는 {}입니다".format(self.name))
        print("나이는 {}살입니다.".format(self.age))