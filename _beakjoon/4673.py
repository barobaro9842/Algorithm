# n과 n의 각 자리수를 더하는 함수라고 정의하자
# 75 + 7 + 5 = 87
# 이런식으로 무한 수열을 만들 때
# 39는 33의 생성자이고, 39는 51의 생성자,
# 생성자가 여러개인 경우도 있다.
# 101인 경우 91과100
# 생성자가 없는 숫자 = 셀프 넘버
# 10000보다 작거나 같은 셀프 넘버를 출력하라


numbers = [i+1 for i in range(10000)]
n = 1 
while n < 10000 :
    a = map(int, list(str(n)))
    res = n + sum(a)
    if res in numbers:
        numbers.remove(res)
    n += 1


for n in numbers :
    print(n)

# for n in numbers :
#     print(n)