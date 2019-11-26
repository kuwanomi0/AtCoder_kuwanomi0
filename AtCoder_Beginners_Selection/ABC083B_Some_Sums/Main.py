# AtCoder Beginners Selection
# ABC083B - Some Sums
# https://atcoder.jp/contsts/abs/tasks/abc083_b
# encode : utf-8
N, A, B = map(int, input().split())
res = 0
for i in range(N+1) :
    if A <= sum([int(s) for s in str(i)]) <= B :
        res += i
print(res)