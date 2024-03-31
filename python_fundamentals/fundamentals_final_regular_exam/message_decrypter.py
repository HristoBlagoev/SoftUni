import re

number_of_interactions = int(input())

for i in range(number_of_interactions):
    message = input()

    pattern = r"^(\$|%)([A-Z][a-z]{3,})\1:\s\[\d+]\|\[\d+]\|\[\d+]\|$"

    if re.match(pattern, message):
        decrypted_message = "".join(chr(int(num)) for num in re.findall(r'\d+', message))

        tag_match = re.match(r'^(\$|%)([A-Z][a-z]{3,})', message)
        if tag_match:
            tag = tag_match.group(2)
            print(f"{tag}: {decrypted_message}")
    else:
        print("Valid message not found!")