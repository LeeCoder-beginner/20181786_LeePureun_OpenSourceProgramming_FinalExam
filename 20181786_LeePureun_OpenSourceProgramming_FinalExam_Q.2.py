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