# AtCoder Beginners Selection
# ABC088B - Card Game for Two
# https://atcoder.jp/contests/abs/tasks/abc088_b
N = input()
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)
print(sum(card_list[0::2]) - sum(card_list[1::2]))