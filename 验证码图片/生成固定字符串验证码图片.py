from PIL import Image
from PIL import ImageFile
from PIL import ImageDraw
from PIL import ImageFont
import random
font_path = 'c:\windows\Fonts\simfang.ttf'
def getRandomColor():
    """获取一个随机颜色（r,g,b）格式的"""
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    return (c1, c2, c3)

# 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
image = Image.new('RGB',(150,30), getRandomColor())
# 获取一个画笔对象，将图片对象传过去
draw = ImageDraw.Draw(image)
# 获取一个font字体对象参数是ttf的字体文件的目录以，及字体的大小
# font = ImageFont.truetype('微软雅黑.ttf',size=32)
font=ImageFont.truetype(font_path,size=32)
# 在图片上写东西，参数是：定位，字符串，颜色，字体
draw.text((20,0),'fuyong',getRandomColor(), font=font)
# 保存到硬盘，名为test.png格式为png的图片
image.save(open('text.png','wb'),'png')