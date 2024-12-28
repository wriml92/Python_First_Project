import random

def play_game():
    # 1부터 10 사이의 랜덤한 숫자를 생성합니다.
    number_to_guess = random.randint(1, 10)
    print("\n1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")

    while True:
        try:
            # 플레이어로부터 숫자를 입력받습니다.
            guess = int(input("예상 숫자: "))
            
            # 입력값 범위 체크
            if guess < 1 or guess > 10:
                print("1부터 10 사이의 숫자를 입력해주세요.")
                continue
            
            # 입력한 숫자가 정답보다 큰지 작은지 확인합니다.
            if guess < number_to_guess:
                print("너무 작습니다. 다시 입력하세요.")
            elif guess > number_to_guess:
                print("너무 큽니다. 다시 입력하세요.")
            else:
                print("정답입니다!")
                break
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

def main():
    while True:
        # 게임 실행
        play_game()
        
        # 게임 재시작 여부 확인
        while True:
            restart = input("게임을 다시 하시겠습니까? (y/n): ").lower()
            if restart in ['y', 'n']:
                break
            print("'y' 또는 'n'을 입력해주세요.")
        
        if restart == 'n':
            print("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
            break

# 게임 시작
if __name__ == "__main__":
    main() 