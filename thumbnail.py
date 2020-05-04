from PIL import Image

# 输入图片路径
try:
    path = input("请输入你的路径：")
    # 打开图片
    im = Image.open(path)
    # 查看图片属性
    print(im.format, im.size, im.mode)
    # 制作缩略图
    wide = int(input("请输入设置的宽度："))
    high = int(input("请输入设置的高度："))
    # 设置图片的大小
    im.thumbnail((wide,high))
    # 保存图片
    save_path = input("请输入保存路径：")
    save_name = input("请输入保存名(请把后缀加上)：")
    im.save(save_path + save_name, "JPEG")
except:
    print("没有找到该图片，请确认图片是否存在")