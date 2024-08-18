
def all_variants(text):
    for i in range(len(text)):
        for g in range(len(text) - i):
            yield text[g:g + i + 1]


a = all_variants("abc")
for r in a:
    print(r)

