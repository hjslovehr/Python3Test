
with open('test.txt', 'w', encoding='utf-8') as f:
    for i in range(0, 128000000):
        f.write(str(i) + "\n")

