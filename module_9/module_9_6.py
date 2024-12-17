def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + 1 + i]


a = all_variants("abc")
for i in a:
    print(i)
