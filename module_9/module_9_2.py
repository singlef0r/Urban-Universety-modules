first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) >= 5]
second_result = [(one, two) for one in first_strings for two in second_strings if len(one) == len(two)]
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
