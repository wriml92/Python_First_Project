import random

# 1부터 10 사이의 랜덤한 숫자를 생성합니다.
number_to_guess = random.randint(1, 10)

print("1과 10 사이의 숫자를 하나 정했습니다.")

while True:
    # 플레이어로부터 숫자를 입력받습니다.
    guess = int(input("예상 숫자: "))
    
    # 입력한 숫자가 정답보다 큰지 작은지 확인합니다.
    if guess < number_to_guess:
        print("너무 작습니다. 다시 입력하세요.")
    elif guess > number_to_guess:
        print("너무 큽니다. 다시 입력하세요.")
    else:
        print("정답입니다!")
        break 