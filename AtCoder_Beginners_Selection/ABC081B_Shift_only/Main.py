# AtCoder Beginners Selection
# ABC081B - Shift only
# https://atcoder.jp/contests/abs/tasks/abc081_b
# encode : utf-8
count = 0
find_odd = 0
num = int(input())
number_list = list(map(int, input().split()))

while (1) :
    odd_list = list(map(lambda x: int(x % 2), number_list))
    find_odd = odd_list.count(1)
    if (find_odd != 0) :
        break
    number_list = list(map(lambda x: int(x / 2), number_list))
    count = count + 1

print(count)