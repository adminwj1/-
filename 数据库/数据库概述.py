'''
declmal(5,2)表示一个包含五位数，小数包含2为
一般删除数据都是逻辑删除，在表中添加一条名为isDelete的字段类型为bit，默认值为0，如果默认值变为1就说明删除了记录，虽然删除了但记录还是在表中



查看版本：
select version();

显示当前时间：
select now();


一、数据层操作：
1、创建数据库
格式：create database 数据库名 charset=utf8;
示例：create database wj charset=utf8;


2、删除数据库
drop database 数据库名;
示例：drop database wj;
	

3、切换数据库
use 数据库名;
示例：use wjnice;


4、查看当前选择的数据库
select 数据库名();
示例：select database();




二、表操作
1、查看当前数据库中所有表
show tables;


2、创建表
create table 表名(列,类型);
auto_increment  表明自增长
primary key	主键
not null	不为空
default	默认值
示例：create table student(id int auto_increment primary key,name varchar(20) not null,age int not null,gender bit default 1,address varchar(20),isDelete bit default 0);

3、删除表
drop table 表名;
drop table student;


4、查看表结构
desc 表名
desc student;


5、查看建表语句
show create table 表名;
show create table student\G;  格式化输出

6、重命名表
rename table 原表明 to 新表名;
rename table student to students;

7、修改表结构
alter table 表名 add|chang|drop 列名 类型;
新增：在students表中新增一个班级的字段
alter table students add class varchar(20);

改名：
三、数据操作：
1、增
a、全列插入
insert into 表名 values(....);
说明：主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功以后以实际数据为准
insert into student values(0,"tom",1,"四川",0,"四年级五班");
b、缺省插入
insert into 表名(列1,列2,...) values(值1,值2,...)
insert into student(name,address,class) values("lilei","上海","网络安全二班");




c、同时插入多条数据
insert into 表名 values(...),(...)
insert into student values(0,'岳鹏飞',0,'北京',0,'动漫设计一班'),(0,'海王',1,'武汉',0,'物流管理一班');

2、删
delete from 表名 where 条件;
delete from student where id=3;
注意：没有条件是全部删除

3、改
update 表名 set 列1=值1, 列2=值2,... where 条件
update student set age=16 where id =3;
注意：没有条件是全部列都修改

4、查
查询表中的所有数据
select * from 表名;
select * from student;

1、基本查询
select * from 表名;
select * from student;
说明：
a、from关键字后面是表名，表示数据来源于这张表
b、select后面写表中的列名，如果是*表示在结果集中显示表中的所有列
c、在select后面的列名部分，可以使用as为列名起别名，这个别名显示在结果集中
d、如果要查询多个列，之间使用逗号分隔

示例：
（1）只查看姓名和年龄：
select name, age from student;
（2）为name列取别名：
select name as na, age from student;


2、消除重复行
在select后面列前面使用distinct可以消除重复的行
示例：消除age列重复的数据
select distinct age from student;


3、条件查询
a、语法
select * from 表名 where 条件
* 表示所有，可以指定列名

b、比较运算符
等于          =
大于          >
小于          <
大于等于       >=
小于等于       <=
不等于         !=或<>

示例：
（2）查询id值大于8的所有数据
select * from student where id > 2;

c、逻辑运算符
and         并且
or          或者
not         非

示例：
（1）查询id值大于2的女同学
select * from student where id >2 and gender = 1;


d、模糊查询
like
%表示任意多个任意字符
_表示一个任意字符
示例：
（1）查询姓韩的同学
select * from student where name like '韩%';匹配多个
select * from student where name like '韩_';匹配一个

e、范围查询
in 表示在一个非连续的范围内
between...and.. 表示在一个连续的范围内
示例：
（1）查询编号为：1,4,6的学生
select * from student where id in (1,4,6);
（2）查询编号为6到8的学生
select * from student where id between 6 and 8;

f、空判断
注意：null与""是不同，""是有数据的，null是没有数据的
判断空：is null
判断非空 is not null
示例：
（1）查询没有地址的同学
select * from student where address id null;
（2）查询填写地址的同学
select * from student where address is not null;

g、优先级
小括号，not，比较运算符，逻辑运算符，
andbior优先级高，如果同时出现并希望先选or，需要结合()来使用


4、聚合
为了快速得到统计的数据，提供了5个聚合函数
a、count(*)       表示计算总行数，括号中可以写*和列名
b、max(列)        表示求此列的最大值
c、min(列)        表示求此列的最小值
d、sum(列)        表示求此列的和
e、avg(列)        表示求此列的平均值
示例：查询学生总数：
select count(*) from student;
示例：查询女生的编号最大值
select max(id) from student where gender=1;

示例：查询女生的编号最小值
select min(id) from student where gender=1;

示例：查询女生的年龄和
select sum(age) from student where gender=1;

示例：查询所有学生的平均年龄
select avg(age) from student;


5、分组
a、按照字段分组，表示此字段相同的数据会被放到一个集合中。分组后，只能查询出相同数据列，对于有差异的数据列无法显示在结果集中。可以对分组后的数据进行统计，做聚合运算
语法：select 列1,列2,聚合…… from 表名 group by列1,列2,……;
示例：
（1）查询男女生总数
select gender,count(*) from student group by gender;
select gender from student group by gender;

（2）按年龄分组（可能有问题）
select gender,age ,count(*) from student group by gender,age;

b、分组后的数据筛选
语法：select 列1,列2,聚合…… from 表名 group by列1,列2,…… having 列1,列2,……,聚合……;
示例：
（1）查询男女总数，只显示女生总数
select gender,count(*) from student group by gender having gender;
主意：having默认值为1，修改默认值：having gender=0;

（2）查询男女总数，只显示男生总数
select gender,count(*) from student group by gender having gender=0;

where与having的区别：
where是对from后制定的表进行筛选属于对原始数据的筛选
having是对group by的结果进行筛选

6、排序
语法：select * from 表名 order by 列1 asc|desc, 列2 asc|desc,……;
说明：
a、将数据按照列1进行排序，如果某些列1的值相同，则按到列2进行排序
b、默认按照从小到大的顺序排序
c、asc升序
d、desc降序
示例：
（1）按年龄排序
select * from student order by age;
升序显示
select * from student order by age asc;
降序显示
select * from student order by age desc;

(2)将没有被删除的数据按年龄排序（删除字段是isDelete，0表示没有被删除，1表示被删除）
select * from student where isDelete=0 order by age;

（3）将重复的数据通过id进行降序查询
select * from student order by age desc, id desc;

7、分页
语法：select * from 表名 limit start,count;
说明：start索引从0开始
示例：
（1）查询student前3条记录
select * from student limit 0,3;
（2）查询前3条记录中gender为男的信息
select * from student where gender=0 limit 0,3;
四、关联
建表语句：
1、create table class(id int auto_increment primary key, name varchar(20) not null, stuNum int not null);
2、create table students(id int auto_increment primary key, name varchar(20) not null, gender bit default 1, classid int not null, foreign key(classid)references class(id));
插入一些数据：
班级表：
insert into class values(0,"python01",55),(0,"python02",60),(0,"python03",40),(0,"python04",80);
学生表：
    insert into students values(0, "tom", 1, 1);
关联查询示例：
（1）显示学生姓名和班级名
说明：
students.name                       表示：学生姓名字段
class.name                          表示：班级名称字段
from class                          表示：从那张表里面进行查询
inner join students                 表示：关联某张表
on class.id=students.classid        表示：表中的id字段必须与students.classid相等才能拿出两张表中的数据

select students.name,class.name from class inner join students on class.id=students.classid;

分类：
1、表A inner join 表B;
表A与表B匹配的行会出现在结果集中

2、表A left join 表B;
表A与表B匹配的行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充
select students.name,class.name from class left join students on class.id=students.classid;

3、表A right join 表B
表A与表B匹配的行会出现在结果集中，外加表B中独有的数据，未对应的数据使用null填充
select students.name,class.name from class right join students on class.id=students.classid;
'''