T = int(input()) # 테스트 케이스 개수

for test_case in range(1, T+1):
    
    numbers = list(map(int, input().split())) # 숫자 입력
    
    sum = 0
    
    for i in range(len(numbers)): # 입력 받은 숫자 개수만큼 반복
        if numbers[i] % 2 == 1: # 입력 받은 숫자를 2로 나눈 나머지로 구분
            sum += numbers[i] # 입력 받은 숫자가 조건문 만족하면 sum에 더하기

    print(f"#{test_case} {sum}")
