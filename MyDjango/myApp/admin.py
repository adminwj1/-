from django.contrib import admin

# Register your models here.
# 引入数据表
from .models import Grades,Students
class StudentsInfo(admin.TabularInline):
    model = Students    # 引用类名
    extra = 2   # 添加几条数据
# 注册
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]    # 引用类
    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']  # 显示字段
    list_filter = ['gname']    # 过滤字段，以某个字段为条件进行过滤
    search_fields = ['gname']   # 搜索框，搜索字段
    list_per_page = 5    # 分页，以5条为分页

    # # 添加、修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']   # 规定属性的先后顺序
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),   # 先分组，然后使用fields方法规定属性的顺序
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]   # 给属性分组，fields和fieldsets不能同时使用，在页面的增加功能中进行分组
admin.site.register(Grades, GradesAdmin)    # 注册时必须要继承GradesAdmin这个类才有用


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"   # 简单的描述，让页面列显示为中文
    
    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']    # 传入刚才封装的函数但是不调用，只是传入
    list_per_page = 10


    # 执行动作位置
    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Students, StudentsAdmin)












