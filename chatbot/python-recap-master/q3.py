'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

if number % 2 == 0 :
    print("Even")
else: 
    print("Odd")


# 아래에 코드를 작성해 주세요.

#ans = number % 2 == 0 and "Even" or "Odd"

print("Even") if number % 2 == 0 else print("Odd")

#print(ans)