files = '1.txt', '2.txt', '3.txt'

result = []
for file in files:
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        result.append((len(data), file, data))
with open('result.txt', 'w', encoding='utf-8') as f:
    for data in sorted(result):
        f.write(data[1] + '\n')
        f.write(str(data[0]) + '\n')
        f.writelines(data[2])
        f.write('\n')