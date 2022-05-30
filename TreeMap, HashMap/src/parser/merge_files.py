""""merging file"""
import shutil


def merge(path1, path2, res_path):
    """Объединение двух файлов в один"""
    with open(res_path, 'w', encoding='utf-8') as file_rez:
        with open(path1, 'r', encoding='utf-8') as file1:
            with open(path2, 'r', encoding='utf-8') as file2:
                line1 = file1.readline()
                line2 = file2.readline()
                while True:
                    if len(line1.split(': ')) == 2:
                        words1, count1 = map(str, line1.split(': '))
                    if len(line2.split(': ')) == 2:
                        words2, count2 = map(str, line2.split(': '))
                    print('----------------------------')
                    print(line1, words1, count1)
                    print(line2, words2, count2)
                    print('----------------------------')
                    if line1 == '' and line2 == '':
                        return
                    elif line1 == '' and line2 != '':
                        while line2 != '':
                            file_rez.write(line2)
                            line2 = file2.readline()
                        return
                    elif line1 != '' and line2 == '':
                        while line1 != '':
                            file_rez.write(line1)
                            line1 = file1.readline()
                        return
                    else:
                        if words1 < words2:
                            file_rez.write(line1)
                            line1 = file1.readline()
                        elif words1 > words2:
                            file_rez.write(line2)
                            line2 = file2.readline()
                        else:
                            words1, count1 = map(str, line1.split(': '))
                            words2, count2 = map(str, line2.split(': '))
                            new_count = int(count1) + int(count2)
                            new_word = words1
                            new_line = f'{new_word}: {new_count}\n'
                            file_rez.write(new_line)
                            line2 = file2.readline()
                            line1 = file1.readline()


# Можно было считать 2 файла в массив-> обработать его -> записать в новый файл
def multi_merge(*paths, help_file='help.txt', result_file='result.txt'):
    """Объеденить много файлов в один"""
    # перд всем что снизу, надо еще отсортировать файлы, которые мерджить будем
    prev_paths = paths[0]
    for path in paths[1:]:
        merge(path, prev_paths, result_file)
        # копируем result_file в prev_paths
        prev_paths = help_file
        shutil.copyfile(result_file, prev_paths)


multi_merge('data/1 июля.txt', 'data/1972 год.txt', 'data/Амберг.txt')
