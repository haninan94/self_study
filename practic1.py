T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = input().split(" ")
    sum = 0
    for i in range(10):
        sum += int(num[i])
    mean = sum/len(num)
    mean = round(mean, 0)
    print("#{0} {1}".format(T, mean))