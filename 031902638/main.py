import pypinyin
import copy
import re
import sys
import ChineseBreak

# 枚举所有拼音、字母
AL_PY = [
    'a', 'o', 'e', 'ba', 'bo', 'bi', 'bu', 'pa', 'po', 'pi', 'pu',
    'ma', 'mo', 'me', 'mi', 'mu', 'fa', 'fo', 'fu', 'da', 'de',
    'di', 'du', 'ta', 'te', 'ti', 'tu', 'na', 'ne', 'ni', 'nu',
    'nv', 'la', 'lo', 'le', 'li', 'lu', 'lv', 'ga', 'ge', 'gu',
    'ka', 'ke', 'ku', 'ha', 'he', 'hu', 'ji', 'ju', 'qi', 'qu',
    'xi', 'xu', 'zha', 'zhe', 'zhi', 'zhu', 'cha', 'che', 'chi',
    'chu', 'sha', 'she', 'shi', 'shu', 'ra', 're', 'ri', 'ru',
    'za', 'ze', 'zi', 'zu', 'ca', 'ce', 'ci', 'cu', 'sa', 'se',
    'si', 'su', 'ya', 'yo', 'ye', 'yi', 'yu', 'wa', 'wo', 'wu',
    'ai', 'ei', 'ao', 'ou', 'er', 'bai', 'bei', 'bao', 'bie',
    'pai', 'pei', 'pao', 'pou', 'pie', 'mai', 'mei', 'mao', 'mou',
    'miu', 'mie', 'fei', 'fou', 'dai', 'dei', 'dui', 'dao', 'dou',
    'diu', 'die', 'tai', 'tei', 'tui', 'tao', 'tou', 'tie', 'nai',
    'nei', 'nao', 'nou', 'niu', 'nie', 'lai', 'lei', 'lao', 'lou',
    'liu', 'lie', 'gai', 'gei', 'gui', 'gao', 'gou', 'kai', 'kei',
    'kui', 'kao', 'kou', 'hai', 'hei', 'hui', 'hao', 'hou', 'jiu',
    'jie', 'jue', 'qiu', 'qie', 'que', 'xiu', 'xie', 'xue', 'zhai',
    'zhei', 'zhui', 'zhao', 'zhou', 'chai', 'chui', 'chao', 'chou',
    'shai', 'shei', 'shui', 'shao', 'shou', 'rui', 'rao', 'rou',
    'zai', 'zei', 'zui', 'zao', 'zou', 'cai', 'cei', 'cui', 'cao',
    'cou', 'sai', 'sui', 'sao', 'sou', 'yao', 'you', 'yue', 'wai',
    'wei', 'an', 'en', 'ang', 'eng', 'ban', 'ben', 'bin', 'bang',
    'beng', 'bing', 'pan', 'pen', 'pin', 'pang', 'peng', 'ping',
    'man', 'men', 'min', 'mang', 'meng', 'ming', 'fan', 'fen',
    'fang', 'feng', 'dan', 'den', 'dun', 'dang', 'deng', 'ding',
    'dong', 'tan', 'tun', 'tang', 'teng', 'ting', 'tong', 'nan',
    'nen', 'nin', 'nun', 'nang', 'neng', 'ning', 'nong', 'lan',
    'lin', 'lun', 'lang', 'leng', 'ling', 'long', 'gan', 'gen',
    'gun', 'gang', 'geng', 'gong', 'kan', 'ken', 'kun', 'kang',
    'keng', 'kong', 'han', 'hen', 'hun', 'hang', 'heng', 'hong',
    'jin', 'jun', 'jing', 'qin', 'qun', 'qing', 'xin', 'xun',
    'xing', 'zhan', 'zhen', 'zhun', 'zhang', 'zheng', 'zhong',
    'chan', 'chen', 'chun', 'chang', 'cheng', 'chong', 'shan',
    'shen', 'shun', 'shang', 'sheng', 'ran', 'ren', 'run', 'rang',
    'reng', 'rong', 'zan', 'zen', 'zun', 'zang', 'zeng', 'zong',
    'can', 'cen', 'cun', 'cang', 'ceng', 'cong', 'san', 'sen',
    'sun', 'sang', 'seng', 'song', 'yan', 'yin', 'yun', 'yang',
    'ying', 'yong', 'wan', 'wen', 'wang', 'weng', 'biao', 'bian',
    'piao', 'pian', 'miao', 'mian', 'dia', 'diao', 'dian', 'duo', 'duan',
    'tiao', 'tian', 'tuo', 'tuan', 'niao', 'nian', 'niang', 'nuo',
    'nuan', 'lia', 'liao', 'lian', 'liang', 'luo', 'luan', 'gua',
    'guo', 'guai', 'guan', 'guang', 'kua', 'kuo', 'kuai', 'kuan',
    'kuang', 'hua', 'huo', 'huai', 'huan', 'huang', 'jia', 'jiao',
    'jian', 'jiang', 'jiong', 'juan', 'qia', 'qiao', 'qian',
    'qiang', 'qiong', 'quan', 'xia', 'xiao', 'xian', 'xiang',
    'xiong', 'xuan', 'zhua', 'zhuo', 'zhuai', 'zhuan', 'zhuang',
    'chua', 'chuo', 'chuai', 'chuan', 'chuang', 'shua', 'shuo',
    'shuai', 'shuan', 'shuang', 'rua', 'ruo', 'ruan', 'zuo',
    'zuan', 'cuo', 'cuan', 'suo', 'suan', 'yuan', 'nve', 'lve', 'b', 'c', 'd', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

total = 0  # 统计答案个数
map_cnt = 0  # 映射值
alp_py_map = {}  # 字母、拼音映射表
division_map = {}  # 汉字拆分映射表

file_word = sys.argv[1]
file_org_add = sys.argv[2]
file_ans = sys.argv[3]


# 建立拼音、字母与数字的映射关系
def init_map():
    global map_cnt
    for letter in AL_PY:
        map_cnt += 1
        alp_py_map[letter] = map_cnt


# 生成敏感词的所有可能形式
def produce_words(word):
    global map_cnt
    word = list(word)
    for index in range(len(word)):
        character = word[index]
        # 处理汉字
        if (u'\u4e00' <= character <= u'\u9fa5') or (u'\u3400' <= character <= u'\u4db5'):
            # print("这是一个汉字")
            li = []
            py = pypinyin.lazy_pinyin(character)
            py = py[0]
            # 全拼
            li.append([py])
            # 全拼散开
            li.append(list(py))
            # 首字母
            li.append([py[0]])

            word[index] = li

            # 判断拆分
            if ChineseBreak.is_breakable(character):
                parts = ChineseBreak.get_part(character)
                division_map[parts] = character

    sensitive_word = []
    for character in word:
        # 汉字
        if isinstance(character, list):
            if len(sensitive_word) == 0:
                for each in character:
                    sensitive_word.append(each)
            else:
                pre = sensitive_word
                new_sensitive_word = []
                for each in character:
                    now = copy.deepcopy(pre)
                    for pre_each in now:
                        for one in each:
                            pre_each.append(one)
                    new_sensitive_word += now
                sensitive_word = new_sensitive_word
        # 字母
        else:
            if len(sensitive_word) == 0:
                sensitive_word.append([character])
            else:
                sensitive_word[0].append(character)
    return sensitive_word


# 用数字表征敏感词
def word2num(word):
    word_list = []
    for each in word:
        word_list.append(alp_py_map[each])
    # print(word_list)
    return word_list


# 表示树的节点
class TrieNode(object):
    def __init__(self, value=None):
        # 值
        self.value = value
        # fail指针
        self.fail = None
        # 尾标志：标志为i表示第i个模式串串尾，默认为0
        self.tail = 0
        # 子节点，{value:TrieNode}
        self.children = {}
        # 敏感词下标
        self.index = -1


# 实现AC自动机
class Trie(object):
    def __init__(self, words):
        # 根节点
        self.root = TrieNode()
        # 模式串个数
        self.count = 0
        self.words = []
        for word in words:
            self.insert(word)
        self.ac_automation()

    # 插入操作
    def insert(self, word):
        self.count += 1
        cur_node = self.root
        sequence = word[0]
        self.words.append(sequence)
        for item in sequence:
            if item not in cur_node.children:
                # 插入结点
                child = TrieNode(value=item)
                cur_node.children[item] = child
                cur_node = child
            else:
                cur_node = cur_node.children[item]
        cur_node.tail = self.count
        cur_node.index = word[1]

    # 构建失败路径
    def ac_automation(self):
        queue = [self.root]
        # BFS遍历字典树
        while len(queue):
            temp_node = queue[0]
            # 取出队首元素
            queue.remove(temp_node)
            for value in temp_node.children.values():
                # 根的子结点fail指向根自己
                if temp_node == self.root:
                    value.fail = self.root
                else:
                    # 转到fail指针
                    p = temp_node.fail
                    while p:
                        # 若结点值在该结点的子结点中，则将fail指向该结点的对应子结点
                        if value.value in p.children:
                            value.fail = p.children[value.value]
                            break
                        # 转到fail指针继续回溯
                        p = p.fail
                    # 若为None，表示当前结点值在之前都没出现过，则其fail指向根结点
                    if not p:
                        value.fail = self.root
                # 将当前结点的所有子结点加到队列中
                queue.append(value)

    # 传入待检测的某一行文本，找出该行内的所有敏感词
    def search(self, text, original_text):
        p = self.root
        # 记录匹配起始位置下标
        start_index = 0
        # 成功匹配结果集
        rst = []
        for i in range(len(text)):
            single_char = text[i]
            if single_char == '#':
                i += 1
                continue
            single_char = pypinyin.lazy_pinyin(single_char)[0]
            single_char = alp_py_map[single_char]

            while single_char not in p.children and p is not self.root:
                p = p.fail
            # 有一点瑕疵，原因在于匹配子串的时候，若字符串中部分字符由两个匹配词组成，此时后一个词的前缀下标不会更新
            # 这是由于KMP算法本身导致的，目前与下文循环寻找所有匹配词存在冲突
            # 但是问题不大，因为其标记的位置均为匹配成功的字符
            if single_char in p.children and p is self.root:
                start_index = i
            # 若找到匹配成功的字符结点，则指向那个结点，否则指向根结点
            if single_char in p.children:
                p = p.children[single_char]
            else:
                start_index = i
                p = self.root
            temp = p
            while temp is not self.root:
                # 尾标志为0不处理，但是tail需要-1从而与敏感词字典下标一致
                # 循环原因在于，有些词本身只是另一个词的后缀，也需要辨识出来
                if temp.tail:
                    pre = [-1, -1, -1]
                    if len(rst) > 0:
                        pre = rst[-1]
                    global total
                    if temp.index != pre[2] or start_index != pre[0]:
                        total += 1
                    else:
                        rst.pop()
                    if text[i] != original_text[i]:
                        rst.append([start_index, i + 2, temp.index])
                    else:
                        rst.append([start_index, i + 1, temp.index])
                    # rst[self.words[temp.tail - 1]].append((start_index, i))
                temp = temp.fail
        return rst


# 处理待检测文本
class Check:
    def __init__(self):
        # 记录读取到了多少个敏感词
        self.word_cnt = 0
        # 记录敏感词原型
        self.original_word = []
        # 记录敏感词的所有变形
        self.sensitive_word = []
        # 记录当前读取到第几行
        self.line_cnt = 0
        # 记录每行检测出的敏感词
        self.result = []

    # 读取敏感词
    def read_words(self, filename):
        try:
            with open(filename, 'r+', encoding='utf-8') as org:
                words = org.readlines()
                for word in words:
                    word = word.replace('\r', '').replace('\n', '')
                    # 保存敏感词的原型
                    self.original_word.append(word)

                    word.lower()
                    # 获取敏感词的所有可能形态
                    deformations = produce_words(word)
                    # print("deformation:",deformations)
                    # 将所有变形与数字集合建立映射关系，记录其对应第几个敏感词
                    for deformation in deformations:
                        self.sensitive_word.append([word2num(deformation), self.word_cnt])
                    self.word_cnt += 1
                # print(self.sensitive_word)
                org.close()
        except OSError as reason:
            print('敏感词文件出错了\n错误的原因是：' + str(reason))

    # 读取待检测文本
    def read_org_add(self, file_name):
        try:
            with open(file_name, 'r+', encoding='utf-8') as org:
                model = Trie(self.sensitive_word)
                lines = org.readlines()
                # 逐行处理待检测文本
                for original_line in lines:
                    self.line_cnt += 1
                    original_line = original_line.replace('\r', '').replace('\n', '')
                    line = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '#', original_line)
                    line = line.lower()

                    # 可拆分汉字
                    for index in range(len(line) - 1):
                        character = (line[index], line[index + 1])
                        if character in division_map:
                            li = list(line)
                            li[index] = division_map[character]
                            li[index + 1] = '#'
                            line = ''.join(li)
                    # tmp_result:[ [起始位置，终点位置，对应原型], [] ]
                    tmp_result = model.search(line, original_line.lower())
                    for each in tmp_result:
                        self.result.append([self.line_cnt, self.original_word[each[2]], original_line[each[0]:each[1]]])
                org.close()
        except OSError as reason:
            print('文本文件出错了\n错误的原因是：' + str(reason))

    # 将结果输入输出文件内
    def output(self, filename):
        try:
            with open(filename, 'w+', encoding='utf-8') as ans:
                print("Total: {}".format(total), file=ans)

                for i in self.result:
                    print('Line{}: <{}> {}'.format(i[0], i[1], i[2]), file=ans)

                ans.close()
        except IOError as reason:
            print('输出文件出错了\n错误的原因是：' + str(reason))


def main():
    init_map()
    checker = Check()
    checker.read_words(file_word)
    checker.read_org_add(file_org_add)
    checker.output(file_ans)


if __name__ == '__main__':
    main()
