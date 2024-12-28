class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def display(self):
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")

# 사용자로부터 정보 입력받기
age = int(input("나이: "))
name = input("이름: ")
gender = input("성별: ")

# Person 객체 생성
person = Person(name, gender, age)

# 정보 출력
person.display() 