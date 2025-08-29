"""
17题:
1.手动在当前项目根目录下创建singer.txt文件，内容：沉默是金，张国荣\n少女的祈祷，杨千嬅\n暗里着迷，刘德华\n难念的经，周华健
2、定义一个singer类(歌手类)，包含初始化init方法：

实例属性:
歌曲名 歌手名字
实例方法：fans()：打印“XXX歌手的YYY歌曲持续打榜，粉丝为喜欢的歌手打call” 备注：XXX为对象的歌手名字，YYY
为对象的歌曲名

附加功能：
3、在歌手类外面完成以下功能：
1）通过程序逐行读取singer.txt文件内容，根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。
2）遍历列表，获取元素并调用对象的fans方法.
"""

class Singer:
    def __init__(self, song_name, singer_name):
        self.song_name = song_name
        self.singer_name = singer_name

    def fans(self):
        print(f"歌手：{self.singer_name}的《{self.song_name}》歌曲持续打榜，粉丝为喜欢的歌手打call")


def read_file_and_print_singers(file_path) -> list:
    singer_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        l = file.readlines()
    print(l)
    for el in l:
        # 用strip()方法去除空格/换行符
        list2 = el.strip().split("，")
        # list2 = el.replace("\n", "").split("，")
        singer_list.append(Singer(list2[0], list2[1]))
    for singer in singer_list:
        singer.fans()

with open('singer.txt','w',encoding='utf-8') as file:
    file.write("沉默是金，张国荣\n少女的祈祷，杨千嬅\n暗里着迷，刘德华\n难念的经，周华健")

read_file_and_print_singers("singer.txt")