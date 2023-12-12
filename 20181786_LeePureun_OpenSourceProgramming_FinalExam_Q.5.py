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