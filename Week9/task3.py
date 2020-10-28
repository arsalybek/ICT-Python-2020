# 1
# s = input()
# res = s
# for i in range(len(s)):
#     if s[i] == "A" or s[i] == "a" or s[i] == "O" or s[i] == "o" or s[i] == "Y" or s[i] == "y" or s[i] == "I" or \
#             s[i] == "i" or s[i] == "E" or s[i] == "e" or s[i] == "U" or s[i] == "u":
#         res = res.replace(s[i], '')
# res_2 = res
# for i in range(len(res_2)):
#     res_2 = res_2.replace(res[i], '.' + res[i])
# print(res_2.lower())

# 2
# s = input()
# s_2 = sorted(s.replace("+", ""))
# s_3 = ""
# for i in range(len(s_2)):
#     s_3 += s_2[i] + "+"
# print(s_3[:len(s)])

# 3
# s = input()
# print(s[0].capitalize() + s[1:])

# 4
# s = input()
# if '0000000' in s or '1111111' in s:
#     print("YES")
# else:
#     print("NO")

# 5
# s = input()
# if len(set(s)) % 2 != 0:
#   print("IGNORE HIM!")
# else:
#   print("CHAT WITH HER!")

#6
# cnt_upper = 0
# cnt_lower = 0
# s = input()
# res = ""
# for i in range(0, len(s)):
#     if 97 <= ord(s[i]) <= 122:
#         cnt_lower = cnt_lower + 1
#     else:
#         cnt_upper = cnt_upper + 1
# if cnt_upper > cnt_lower:
#     res = s.upper()
# else:
#     res = s.lower()
# print(res)

#7
# n = int(input())
# s = input()
# res = len(set(s.lower()))
# if res == 26:
#   print("YES")
# else:
#   print("NO")

# 8
# s = input()
# t = input()
# s = s[::-1]
# if t == s:
#     print("YES")
# else:
#     print("NO")

# 9
# n = int(input())
# s = input()
# cnt_D = 0
# cnt_A = 0
# for i in range(n):
#   if s[i] == "A":
#     cnt_A = cnt_A + 1
#   else:
#     cnt_D = cnt_D + 1
# if cnt_A == cnt_D:
#     print("Friendship")
# elif cnt_D > cnt_A:
#    print("Danik")
# else:
#    print("Anton")

# 10
# s = input()
# if s.isupper():
#     print(s.lower())
# elif s.islower():
#     print(s.upper())
# elif s[0].lower() and s[1:].isupper():
#     print(s[0].capitalize() + s[1:].lower())
# else:
#     print(s)

# 11
# n = int(input())
# s = input()
# res = ""
# cnt_Z = 0
# cnt_E = 0
# cnt_R = 0
# cnt_O = 0
# cnt_N = 0
# for i in range(len(s)):
#     if s[i] == "z":
#         cnt_Z += 1
#     if s[i] == "e":
#         cnt_E += 1
#     if s[i] == "r":
#         cnt_R += 1
#     if s[i] == "o":
#         cnt_O += 1
#     if s[i] == "n":
#         cnt_N += 1
# while cnt_O > 0 and cnt_N > 0 and cnt_E > 0:
#     res += "1 "
#     cnt_N -= 1
#     cnt_O -= 1
#     cnt_E -= 1
# while cnt_Z > 0 and cnt_E > 0 and cnt_R > 0 and cnt_O > 0:
#     res += "0 "
#     cnt_Z -= 1
#     cnt_O -= 1
#     cnt_E -= 1
#     cnt_R -= 1
# print(res[:len(res) - 1])

# 12
# n = int(input())
# s = input()
# cnt = 0
# for i in range(0, len(s) - 2):
#     if s[i] == "x" and s[i + 1] == "x" and s[i + 2] == "x":
#         cnt += 1
# print(cnt)