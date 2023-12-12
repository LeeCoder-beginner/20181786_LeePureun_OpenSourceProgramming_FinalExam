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