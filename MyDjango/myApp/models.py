from django.db import models

# Create your models here.
class Grades(models.Model):
    # 类中的属性就对应表中的字段
    # CharField：相当于字符串类型，max_length：最大长度
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    # NullBooleanField和BooleanField类似，只是NullBooleanField有三个字：NULL、True、False
    isDelete = models.BooleanField(default=False)       # 默认不删除
    # 重写类显示
    def __str__(self):
        return "%s-%d-%d" % (self.gname, self.ggirlnum, self.gboynum)
    class Meta:
        db_table = "grades"


class StudentsManager(models.Manager):
    """重写get_queryset方法"""
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)  # filter过滤需要的数据

# 在定义管理器中添加一个方法
    def createStudent(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        stu.isDelete = isD
        return stu







class Students(models.Model):
    # 定义一个类方法创建对象
    @classmethod
    def creatStudent(cls, name, age, grander, contend, grade, lastT, createT,
                     isD=False):  # cls代表的是Students这个类，如果写@classmethod就在方法中写students
        # 创建一个对象
        stu = cls(sname=name, sage=age, sgender=grander, scontend=contend, sgrade=grade, lastTime=lastT,
                  createTime=createT, isDelete=isD)
        # 返回对象
        return stu
    # 自定义模型管理器
    # 当自定义模型管理器，objects是就不存在了
    stuObject = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)     # 默认男生
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE,)        # 外键关联哪个类，'Grades'只对应被关联的类

    def __str__(self):
        return "%s-%d-%d" % (self.sname, self.sgender, self.sage)
        return self.sname

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "students"   # 定义数据库表名，推荐使用小写字母，数据表名默认为项目名小写下划线类名小写
        ordering = ['id']   # 对象的默认排序字段，获取对象的列表时使用






