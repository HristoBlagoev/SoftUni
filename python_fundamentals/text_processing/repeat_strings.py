sequence_of_strings = input().split(" ")

repeat_text = [text * len(text) for text in sequence_of_strings]
print("".join(repeat_text))