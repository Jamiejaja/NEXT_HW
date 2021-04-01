# 숫자를 입력받고 홀수 구구단(3,5,7,9) 또는 짝수 구구단(2,4,6,8)을 출력하는 함수를 작성하고 실행하세요.

"""
[입력예시]
133

[출력예시]
3 * 1 = 3       
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
*****************************
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
*****************************
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
*****************************
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
"""

###################################################
# Step1. 입력값이 홀수면 홀수(3,5,7,9) 구구단을 출력한다. 짝수면 짝수(2,4,6,8) 구구단을 출력하는 함수를 작성한다.

# Step2. 숫자를 입력받고 step1에서 정의한 함수를 실행한다.

i = int(input("숫자: "))

if i % 2 == 1:
    for x in range(3, 10, 2):
        for y in range(1, 10, 1):
            print(f"{x} * {y} = {x*y}")
        print("*****************************")

else:
    for x in range(2, 10, 2):
        for y in range(1, 10, 1):
            print(f"{x} * {y} = {x*y}")
        print("*****************************")