import random

def create_boxes():
    """
    100개의 상자를 무작위로 생성합니다.
    각 상자에는 1부터 100까지의 번호가 섞여서 들어갑니다.
    - 역할: 첫 번째 사람은 이 함수를 작성합니다.
    """
    pass

def prisoner_strategy(prisoner_number, boxes):
    """
    특정 죄수가 자신의 번호를 찾기 위해 상자를 여는 전략을 실행합니다.
    - 역할: 두 번째 사람은 이 함수를 작성합니다.
    - 전략: 자신의 번호를 따라가는 루프 전략을 사용합니다.
    - 입력:
        prisoner_number: 죄수의 번호 (1부터 100까지)
        boxes: 상자 배열
    - 출력: True(성공) 또는 False(실패)
    """
    pass

def simulate_game():
    """
    100명의 죄수가 게임에 도전하는 전체 프로세스를 시뮬레이션합니다.
    - 역할: 세 번째 사람은 이 함수를 작성합니다.
    - 이 함수는 각 죄수의 성공 여부를 확인하고 전체 결과를 반환합니다.
    - 출력: True(모두 성공) 또는 False(누군가 실패)
    """
    boxes = create_boxes()
    for prisoner_number in range(1, 101):
        if not prisoner_strategy(prisoner_number, boxes):
            return False  # 누군가 실패하면 게임 종료
    return True  # 모두 성공

def main():
    """
    시뮬레이션을 여러 번 실행하고 성공 확률을 계산합니다.
    - 역할: 네 번째 사람은 이 함수를 작성합니다.
    - 이 함수는 게임을 반복 실행하여 성공 확률을 출력합니다.
    """
    pass

if __name__ == "__main__":
    main()
