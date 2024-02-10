words = input().split()
filtrated_words = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filtrated_words))