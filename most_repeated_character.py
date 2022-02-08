sentence = "This is a sample question that is common in interviews"
frequency = {}
for character in sentence:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1


char_frequency = (
    sorted(frequency.items(), key=lambda kv: kv[1], reverse=True))
print(char_frequency[1])
