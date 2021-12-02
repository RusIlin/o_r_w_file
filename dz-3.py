def result_function():
    data = {}
    files_list = ('1.txt', '2.txt', '3.txt')
    for file in files_list:
        with open(file, encoding='utf-8') as f:
            strings = len(f.readlines())
        with open(file, encoding='utf-8') as f:
            data[file] = (strings, f.read().strip())
    data = sorted(data.items(), key=lambda x: x[1])
    for i in data:
        with open('result.txt', 'a', encoding='utf-8') as doc:
            doc.write(f"{i[0]}\n")
            doc.write(f"{i[1][0]}\n")
            doc.write(f"{i[1][1]}\n")


result_function()
