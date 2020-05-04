import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "continue", "phone", "position", "pose", "game")
print(
    """
    欢迎参加猜单词游戏
    把字母组合成一个正确的单词。
    """
)
iscontinue = "y"
while iscontinue == "y" or iscontinue == "Y":
    # 从序列中随机挑出一个单词
    word = random.choice(WORDS)
    # 一个用于判断玩家是否猜对的变量
    correct = word
    # 创建乱序后单词
    jumble = ""
    """将随机的单词打乱"""
    while word:
        # 根据word长度参数word的随机位置
        position = random.randrange(len(word))  # 将word随机取的单词将其打乱
        # 将position位置的字母组合到乱序后单词
        # print(type(position))
        # 将position位置的字母组合到乱序后单词
        jumble += word[position]
        # print(jumble)
        # 通过切片将position位置的字母从原单词中删除
        word = word[:position] + word[(position+1):]
        # print("position删除后：", word)
    print("乱序后的单词：", jumble)

    guess = input("\n你猜猜看：")
    """判断用户是否猜对"""
    while guess != correct and guess != "":
        print("对不起不正确。")
        guess = input("继续猜：")
    if guess == correct:
        print("真棒，你猜对了！")
    iscontinue = input("\n是否继续（Y/N）：")

    # while guess == correct:
    #     print("真棒，你猜对了！")
    #
    #     if guess != correct and guess != "":
    #         print("对不起不正确！")
    #         guess = input("再接再厉：")