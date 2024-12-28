class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        # 성별 유효성 검사
        if gender.lower() not in ['male', 'female']:
            raise ValueError("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
        self.gender = gender.lower()
    
    def display(self):
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")
    
    def greet(self):
        if self.age < 8:
            message = "어린이"
        elif self.age < 20:
            message = "청소년"
        else:
            message = "성인"
        print(f"안녕하세요, {self.name}! {message}이시군요!")

def get_valid_gender():
    while True:
        gender = input("성별: ")
        try:
            if gender.lower() in ['male', 'female']:
                return gender
            else:
                print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
        except AttributeError:
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")

# 사용자로부터 정보 입력받기
age = int(input("나이: "))
name = input("이름: ")
gender = get_valid_gender()

# Person 객체 생성
person = Person(name, gender, age)

# 정보 출력
person.display()
# 인사 메시지 출력
person.greet() 