#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : ________ 이름 : ______

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

## target과 my_string을 in 연산자를 통해 비교
## 두 개의 매개변수는 영소문자로만 이루어져 있기 때문에 영어 대문자가 포함되어있다면 lower 함수를 통해 영소문자로 바꾼다.



def solution(my_string, target):
  if target.lower() in my_string.lower(): ## if문과 in을 통해 특정 문자열 파악 / lower 함수로 영소문자로 해석
    answer = 1
  else:
    answer = 0
  return answer

result = solution('My three favourites are', 'favourites')
print(result)


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

## 미안해라는 말보다 "고마워, 힘내, 사랑해"
## (My three favourites are) "Thank you", "You did your best", and "I love you".

def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    a = letter.split() ## 모스부호로 이루어진 코드를 공백으로 split 함수 사용

    b = []
    answer = ''

    for i in range(0, len(a)):
      b.append(morse[a[i]])
      answer+= str(b[i])

    return answer

## Thank you You did your best and I love you
result = solution('- .... .- -. -.- -.-- --- ..- -.-- --- ..- -.. .. -.. -.-- --- ..- .-. -... . ... - .- -. -.. .. .-.. --- ...- . -.-- --- ..-')
print(result)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):

    answer = ''
    for i in range(0, len(str(age))):
      answer += chr(int(str(age)[i]) + 97)

    return answer

result = solution(857)
print('PROGRAMMERS'.lower() + '-' + result)


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

from math import sqrt

def solution(r1, r2):
    answer = 0

    for i in range(0, r1):
      answer += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1)) # 예외 처리
    for i in range(r1, r2):
      answer += int(sqrt(r2**2 - i**2))

    return answer * 4 # 총 4사분면의 개수

result = solution(2, 3)
print(result)

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

## numbers의 원소는 1에서 1000 사이임을 알고있다
## 이를 통해 모두 4자리의 정수형태로 만들어 비교하면 가장 큰 수를 구할 수 있고
## 이를 순서대로 배치하면 Q.5를 해결할 수 있다.

def solution(numbers):
    answer = '' # 결과를 담을 빈 문자열

 # 리스트의 합이 0이면 모든 수가 0인 경우이므로 결과로 '0'을 반환
    if sum(numbers)==0:
        return '0'

# 숫자들을 문자열로 변환하여 정렬
# 각 숫자를 문자열로 바꾼 뒤, x*3을 기준으로 정렬
# x*3 기준으로 정렬하는 이유는 numbers의 원소는 1000 이하의 수이기 때문 ( 만약 1000값이 주어졌을떄 4번 곱하면 오버플로우 나기 떄문에 3까지만 곱해서 int의 최대를 넘지않게 함 )
# 1000 이하의 수로 비교하기 위해 각 수를 문자열로 3번 반복하여 비교
# 예를 들어, 2와 30을 비교할 때 '222'와 '303030'을 비교하여 정렬
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

# 정렬된 숫자들을 문자열로 이어붙여 최종 결과 생성
    return ''.join(numbers)

# 함수 호출 및 결과 출력
result = solution([8, 30, 17, 2, 23])
print(result)