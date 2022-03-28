from ntpath import join
import config


def count_lines(file_list):
    file_dict = {}
    for item in file_list:
        with open(join(config.BASE_PATH, config.FILE_DIR, item), 'r', encoding='utf-8')as file:
            file_dict[item] = sum(1 for _ in file)
    return file_dict


def new_lines(file_dict):
    lines_list = []
    for item in sorted(file_dict.items(), key=lambda x: x[1]):
        lines_list.append(str(item[0])+'\n')
        lines_list.append(str(item[1])+'\n')
        with open(join(config.BASE_PATH, config.FILE_DIR, item[0]), 'r', encoding='utf-8')as file:
            for line in file:
                lines_list.append(line)
    return lines_list


def write_lines(lines):
    with open(join(config.BASE_PATH, config.RESULT_DIR, config.FILE_RESULT), 'w', encoding='utf-8')as file:
        file.writelines(lines)


if __name__ == '__main__':
    write_lines(new_lines(count_lines(config.FILE_IN_DIR)))
