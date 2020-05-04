from django.shortcuts import render
from myApp.models import Students, Grades


# Create your views here.
from django.http import HttpResponse
def index(request):	# request请求体，就是服务器给浏览器的数据
	return HttpResponse('<h1>王剑最帅！！！<h1>')


def detail(request):
	return HttpResponse('<h1>sunck is a good man</h1>')

def grades(request):
	# 去模板里取数据
	gradesList = Grades.objects.all()
	# 将数据传递给模板，模板在渲染页面，将渲染好多页面返回给浏览器
	# {"grades": gradesList})中的grades就是HTML{%fro grade in grades%}中的grades
	return render(request, 'myApp/grades.html', {"grades": gradesList})



def students(request):
	studentsList = Students.stuObject.all()
	return render(request, 'myApp/students.html', {"students": studentsList})
# 显示前5条学生
def students1(request):
	studentsList = Students.stuObject.all()[0:5]
	return render(request, 'myApp/students.html', {"students": studentsList})



#添加学生
def addstudent(request):
	grade = Grades.objects.get(pk=1)
	stu = Students.creatStudent("刘德华", 34, True, "我叫刘德华", grade, "2017-8-10", "2017-8-11")
	stu.save()
	return HttpResponse('alfj1')



def addstudent2(request):
	grade = Grades.objects.get(pk=2)
	stu = Students.stuObject.createStudent("张学友", 54, True, "我叫张学友", grade, "2017-8-10", "2017-8-11")
	stu.save()
	return HttpResponse("**********")
# 超链接
# def gradesStudents(request, num):
# 	# 根据班级id取学生信息,num接收id值
# 	grade = Grades.objects.get(pk=num)
# 	# 获得班级下的所有学生对象列表
# 	studentsList = grade.students_set.all()
# 	return render(request, 'myApp/students.html', {"students": studentsList})