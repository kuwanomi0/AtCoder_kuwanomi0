# AtCoder Beginners Selection
# ABC087B - Coins
# https://atcoder.jp/contsts/abs/tasks/abc087_b
# encode : utf-8
A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X:
                cnt +=1
print(cnt)