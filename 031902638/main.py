import ChineseBreak


def main():
    try:
        with open('./requirements.txt', 'r+', encoding='utf-8') as words:
            lines = words.readlines()
            for line in lines:
                line = line.replace('\r', '').replace('\n', '')
                for each in line:
                    ChineseBreak.test(each)
    except OSError as reason:
        print('文件出错了\n错误的原因是：' + str(reason))


if __name__ == '__main__':
    main()
