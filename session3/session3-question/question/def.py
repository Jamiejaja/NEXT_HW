#입력받은 문자열의 역순을 출력하는 함수를 작성하세요.
#ex) python -> nohtyp

string = input("문자열 입력: ")

def reverse(str):
    for i in range(len(str)-1,-1,-1):
        print(str[i], end="")

reverse(string)