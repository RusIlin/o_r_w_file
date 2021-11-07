import os


def get_files_dict(dir_path):
    files_dict = {}
    files_list = ('1.txt', '2.txt', '3.txt')
    for file in files_list:
        with open(file, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            counter = (int(content.count('\n')) + 1)
            files_dict[file.name] = (counter, content.strip())
    return files_dict


dir_path = os.path.join(os.getcwd())
files_dict = get_files_dict(dir_path)

sorted_tuple = sorted(files_dict.items(), key=lambda x: x[1])
for i in sorted_tuple:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(i[0])
        file.write('\n')
        file.write(str(i[1][0]))
        file.write('\n')
        file.write(i[1][1])
        file.write('\n')
