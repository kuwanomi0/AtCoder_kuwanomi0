# AtCoder Beginners Selection
# ABC081B - Shift only
# https://atcoder.jp/contsts/abs/tasks/abc081_b
# Reference : https://qiita.com/edad811/items/f72acb09f06e5fb35e4e
# encode : utf-8
N = input()
A = list(map(int, input().split()))
cnt = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    cnt += 1
print(cnt)