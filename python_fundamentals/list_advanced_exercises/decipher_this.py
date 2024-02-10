words = input().split()
result = []

for word in words:
    cur_word = list(word)

    char_code = []
    while cur_word[0].isdigit():
        char_code.append(cur_word.pop(0))

    cur_word.insert(0, chr(int("".join(char_code))))
    cur_word[1], cur_word[-1] = cur_word[-1], cur_word[1]

    result.append("".join(cur_word))

print(" ".join(result))



# message = input().split()
#
# words, numbers = [], []
# for word in message:
#     num, let = "", ""
#     for symbol in word:
#         if symbol.isdigit():
#             num += symbol
#         else:
#             let += symbol
#     numbers.append(int(num))
#     if len(let) != 1:
#         let = f"{let[-1]}{let[1:-1]}{let[0]}"
#     words.append(let)
#
# for n, w in zip(numbers, words):
#     print(f"{chr(n)}{w}", end=" ")