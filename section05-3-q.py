# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q1.keys():
    if v == "가을":
        print(q1[v])

for k, v in q1.items():
    if k == "가을":
        print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k, v in q2.items():
    if k == "사과":
        print(" 키에서 사과 찾았다. ")
        break
    if v == "사과":
        print(" 값에서 사과 찾았다. ")
        break
else:
    print("사과를 찾지 못했다.")

for k, v in q2.items():
    if v == "사과":
        print(k, v)
        break
else:
    print("사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
a = 77
if a > 80 and a < 101:
    print("A")
elif a > 60:
    print("B")
elif a > 40:
    print("C")
elif a > 20:
    print("D")
else:
    print("E")      

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

if int(s[7]) % 2 == 1:
    print("남자")
else:
    print("여자")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for a in q3:
    if a == "정":
        continue
    print(a)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1, 101):
    if (n % 2) == 0:
        continue
    print(n, end="")

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
# print(len(q4[0]))
for a in q4:
    if len(a) >= 5:
        print(a)

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for s in q5:
    if s.islower():
        print(s)

print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a in q6:
    if a.islower():
        print(a.upper())
    if a.isupper():
        print(a.lower())


# for n in range(1, 10):
#     if (n % 3) == 0:
#         continue
#     print("*" * n)

# for n in range(0,12):
#     print(n,end=" ")