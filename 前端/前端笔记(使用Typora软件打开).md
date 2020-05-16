表单：
form
属性：action最终数据提交的位置
<label> 用于激活输入文字，没有使用label标签时输入内容只能点击输入框后输入内容，当使用了label标签后就可以点击leabel范围内就可以直接在输入框内输入内容
<input type="" name="">
type：text   password   radio


html内嵌框架
<iframe>标签创建包含另外一个html文件的内联框架（及行内框架）
	src属性来定义另一个HTML文件的引用地址
	frameborder属性定义边框0为没有边框
	scrolling属性定义是否有滚动条
	name属性：用于绑定超链接地址，例如：当a链接的网页需要显示在内联框架中时就需要使用name属性进行绑定具体代码如下：
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Document</title>
		</head>
		<body>
			<a href="http://www.taobao.com" target="myfrom">淘宝网</a>
			<br>
			<iframe src="表单.html" width="600" height="500" frameborder="1"></iframe>
			<br>
			<iframe src="http://www.baidu.com" width="600" height="500" frameborder="1" name="myfrom"></iframe>
		</body>
		</html>

​		
表格标签：
​	table常用标签
​		1、table标签：声明一个表格
​		2、tr标签：定义表格中的一行
​		3、td和th标签：定义一行中的一个单元，td代表普通单元格，th表示表头单元格
​	
​	table常用属性：
​		border-collapse:collapse  设置边框合并。制作一像素宽的边线的表格
​		1、border定义表格的边框
​		2、cellpadding定义单元格内类容与边框的距离
​		3、cellspacing定义单元格与单元格之间的距离
​		4、align设置单元格中内容的水平对齐方式，设置值有：left|center|right
​		5、valign设置单元格中内容的垂直对齐方式top|middle|bottom（middle默认值垂直居中）
​		6、colspan设置单元格水平合并
​		7、rowspan设置单元格垂直合并
​	
	传统布局：
		传统的布局方式就是使用table来做整体页面的布局，布局的技巧归纳为如下几点：
			1、定义表格宽高，将border、cellpadding、cellspacing全部设置为0
			2、单元格里面嵌套表格
			3、单元格中的元素和嵌套的表格用align和valign设置对齐方式
			4、通过属性或者css样式设置单元格中元素的样式
	传统布局目前应用：
		1、快速执着用于演示的html页面
		2、商业推广EDM制作（广告邮件）


​		
​		

CSS：
	为了让页面元素的样式更加丰富，也为了让页面的内容样式能才分开，css由此思想而诞生,css是
	Cascading Style Sheets的首字母缩写，意思是层叠样式表。有了css，HTML中大部分表现样式的标签就废
	弃不用了，HTML只负责文档的结构和内容，表现形式完全交给css，HTML文档变得更加简洁。




css页面引入方法：
	1/外联
	通过link标签，链接到外部央视表到页面中（优先级最低，但用的最多）

	2/嵌入式
	通过style标签，在网页上创建嵌入的样式表（优先级第二高，如果想样式加载的比较快一些，页面代码看起来比较规范的情况下使用这种方式）
	
	3/内联式
	用过style属性，在标签上直接写样式（优先级最高，很少使用）


css文本设置
常用的应用文本的css样式：
	color               设置文字的颜色
	font-size           设置文字的大小
	font-family         设置文字的字体
	font-style          设置字体是否倾斜，如：font-style:normal;设置不倾斜，font-style:italic设置文字倾斜
	font-weight         设置字体时否加粗，如：佛那他-weight:bole;设置加粗，font-weight:normal设置不加粗
	font                同时设置文字的几个属性，写的顺序有兼容问题，建议按照如下顺序写：font:是否加粗字号/行高字体;如：font:normal 12px/36px '微软雅黑';
	line-height         设置文字行高
	text-decoration     设置文字的下划线
	text-indent         设置文字首行缩进
	text-align          设置文字水平对齐方式


​	
​	
css选择器：
​	1、标签选择器：此种选择器影响范围大，建议尽量应用在层级选择器中。
​	*：表示匹配所有标签（相当于核武器级别）
​	2、id选择器：通过id名来选择元素，元素的id名称不能复用，id名一般给程序使用，所以不推荐使用id作为选择器。
​	3、类选择器：通过类名来选择元素，一类可应用于多个元素，一个元素上也可以使用多个类，应用灵活，可复用，是css中应用最多的一种选择器。
​	4、层级选择器：主要应用在选择父元素的子元素，或者子元素下面的子元素，可与标签元素结合使用，减少命名，同时也可以通过层级，放置命名冲突。
​	5、组选择器：多个选择器，如果有同样的设置，可以使用组选择器。
​		语句：.类选择器1,.类选择器2,...,类选择器n{}
​	6、伪类及伪元素选择器：常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after，它们可以通过样式在元素中插入内容。
​		before语句：.类选择器:before{content:"插入内容"}，在文本前插入
​			例子：
​				    <style type="text/css">
​					   .box1:before,.box2:before,.box3:before{
​						   font-size: 17px;
​						   color: brown;
​							content: "在前的文字 ";
​					   }
​					</style>
​				<body>
​					<div class="box1">文字001</div>
​					<div class="box2">文字002</div>
​					<div class="box3">文字003</div>
​				</body>
​		after语句：.类选择器:before{content:"插入内容"}，在文本后插入
​			例子：
​					<style type="text/css">
​						.box1:after,.box2:after,.box3:after{
​						font-size: 17px;
​						color: green;
​						content: " 在后的文字 ";
​						}
​					</style>
​				<body>
​					<div class="box1">文字001</div>
​					<div class="box2">文字002</div>
​					<div class="box3">文字003</div>
​				</body>
​	块元素、内联元素、内联块元素
​	块元素：
​	也可以称为行元素，不居中常用的标签如：div/p/ul/li/h1~h6/dl/dt/dd等都是块元素，它在布局中的行为：
​		.支持全部样式
​		.如果没有设置宽度，默认的宽度为父级宽度100%
​		.盒字占据一行、即使设置了宽度
​	
​	内联元素：
​	也可以称为行内元素，布局中常用的标签如：a/span/em/b.strong/i等都是内联元素，它们在布局中的行为：
​		.支持部分样式（不支持宽、高、margin上下、padding上下）
​		.宽度由内容决定
​		.盒子并在一行
​		.代码换行，盒子之间会产生间距
​		.子元素是内联元素，父元素可以同text-align属性设置子元素水平对齐方式，用line-height属性值设置垂直对齐方式
​	
	解决内联元素间隙的方法：
		1、去掉内联元素之间的换行（将代码写在一行）
		2、将内联元素的父级设置font-size为0，内联元素自身在设置font-siez
		具体代码如下：
			html：
				<!-- 内联元素 -->
				<div class="con">
					<a href="#">这是一个a标签</a>
					<a href="#">这是第二个a标签</a>
				</div>
			
			css：
			    .con{
					background-color: darkmagenta;
					width: 500px;
					height: 300px;
					border: 1px solid #333;
					margin: 50px auto 0;
					font-size: 0;
				}
				.con a{
					background-color: gold;
					text-decoration: none;
					/* width: 500px; //没有效果
					height: 300px; */
					/* margin-left: 30px;
					margin-right: 30px; */
					font-size: 20px;
				}
		
	内联块元素：
		内联块元素，也叫行内块元素，是新增的元素类型，现有元素没有归于此类别的，img和input元素的行尾类
		似这种元素，但是也归类于内联元素，我们可以用display属性将块元素或者内联元素转化成这种元素。他们在不居中表现的行为：
			.支持全部样式
			.如果没有设置宽高，宽高有内容决定
			.盒子并在一行
			.代码换行，盒子会产生间距
			.子元素是内联元素，父元素可以同text-align属性设置子元素水平对齐方式，用line-height属性设置子元素垂直对齐方式
		这三种元素，可以通过display属性来相互转化，不过实际开发中，块元素用的比较多，所以我们经常把内联
		元素转化为块元素，少量转化为内联块，而要使用内联元素时，直接使用内联元素，而不用块元素转化了。
	
	display属性：
		display属性使用来设置元素的类型及隐藏的，常用的属性有：
		1、none元素隐藏且不占位置
		2、block元素以块元素显示
		3、inline元素以内联元素显示
		4、inline-block元素以内联块元素显示


CSS盒子模型：

​	盒子模型解释：
​			元素在页面中显示成一个方块，类似一个盒子，CSS盒子模型就是使用现实中盒子来做比喻，帮助我们设置元素对应的样式。

​	![image-20200424233614016](C:\Users\admiw\AppData\Roaming\Typora\typora-user-images\image-20200424233614016.png)
​	
​		把元素叫做盒子，设置对应的样式分别为：盒子的边框(border)、盒子内的内容和边距之间的间距(padding)、盒子与盒子之间的间距(margin)。

​	盒子模型的样式：

​		border-top-width		设置边框顶部的粗细

​		border-top-color		设置边框顶部的颜色

​		border-top-style		设置边框样式{实线：solid，虚线：dashed，点线：dotted}
​		可以简写成一句：border: 10px solid red;(四个边设置相同，也可以单独设置单边)

	设内间距：padding
​		padding-top				设置顶部内间距
​      	padding-left			设置左部内间距
​      	padding-right			设置右部内间距
​      	padding-bottom			设置底部内间距
	可以简写成一句话一次性同时设置四个边的内间距：
		方式一：四个值的写法（顺时针方向，上、右、下左）
		padding: 20px 100px 200px 40px;
		
		方式二：三个值的写法（上、左右、下）
		padding: 20px 100px 200px;
		
		方式三：两个值的写法（上下、左右）
		padding: 20px 100px;
		
		方式四：一个值的写法（上下左右）
		padding：100px;

	设置外间距：margin
		margin-top				设置顶部外间距
​      	margin-left				设置左部外间距
​      	margin-right			设置右部外间距
​      	margin-bottom			设置底部外间距
	可以简写成一句话一次性同时设置四个边的内间距：
		方式一：四个值的写法（顺时针方向，上、右、下左）
		margin: 20px 100px 200px 40px;
		
		方式二：三个值的写法（上、左右、下）
		margin: 20px 100px 200px;
		
		方式三：两个值的写法（上下、左右）
		margin: 20px 100px;
		
		方式四：一个值的写法（上下左右）
		margin：100px;
	外边距合并：
		外边距合并，当两个垂直外边距相遇时，它们将形成一个外边距。合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者
	解决方法：
		1、使用这种特性：如果不设置盒子的高，内容会自动撑开盒子的高度
			.con{
            width: 298px;
            height: 198px;
            background-color: gold;
            /*第一种解决塌陷的方法*/
            /* border: 1px solid gold; */
			}
			.box{
				width: 100px;
				height: 100px;
				background-color: green;
				/* magrin-top发生了塌陷，将top值给了父级元素 */
				margin-top: 50px; 
			}
		<body>
			<div class="con">
				<div class="box"></div>
			</div>
		</body>
		2、设置一边的外边距，一般设置margin-top
		3、将元素浮动或者定位
		
	
	margin-top塌陷：
		在两个盒子嵌套时候，内部的盒子设置的margin-top会加到外边盒子上，导致内部的盒子margin-top设置失败。
	解决方法如下：
		1、外部盒子设置一个边框(会暴露出设置的边框)
		2、外部盒子设置overflow:hidden
			overflow: hidden;
		3、使用伪元素类：
			<style type="text/css">
			.con{
				width: 298px;
				height: 198px;
				background-color: gold;
				/*第一种解决塌陷的方法*/
				/* border: 1px solid gold; */
				/* 方法二： */
				
			}
			.box{
				width: 100px;
				height: 100px;
				background-color: green;
				/* magrin-top发生了塌陷，将top值给了父级元素 */
				margin-top: 50px; 
			}
			.clearfix:before{
				content: "";
				display: table;
			}
		</style>
	</head>
	<body>
		<div class="con clearfix">
			<div class="box"></div>
		</div>
	</body>
	4、浮动也可以解决margin-top塌陷
	
	
	盒子尺寸大小计算：
		盒子的宽度：width + 左右padding值 + 左右border值
		盒子高度：height + 上下padding值 + 上下border值
		
	元素溢出：（父级中设置伪类overflow）
		1、visble默认值。内容不会被修剪，会呈现在元素框之外。
		2、hidden内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷点功能。
		3、scroll内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。（不管是否溢出都会产生滚动条）
		4、auto如果内容被修剪，则浏览器会显示出滚动条以便查看其余内容。（自动识别是否溢出，溢出就产生滚动条，没有溢出就不产生滚动条）
		5、inherit规定应该从父元素继承overflow属性的值。
		 
	
	浮动：
		文档流，是纸盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行内元素在一行
		之内从左到右排列，先写的先排，后写的排在后面，每个盒子都占据自己的位置。
	
	浮动特性：
		1、浮动元素有左浮动(float left)和有浮动(float right)两种
		2、浮动的元素会向左或右浮动，碰到父元素边界、浮动元素、为浮动的元素才停下来
		3、相邻的块元素可以并在一行，超出父级宽度就换行
		4、浮动让行内元素或块元素自动转化为行内块元素
		5、浮动元素后面没有浮动的元素会占据浮动元素的位置，没有浮动的元素内的文字会避开浮动的元素，形成文字饶图的效果
		6、父元素如果不给行高，父元素内整体浮动的元素无法撑开父元素，需要清除浮动
		7、浮动元素之间没有垂直margin的合并

​	清除浮动：
		.父级上增加属性overflow: hidden
		.在最后一个子元素的后面加一个空的div，给它样式属性clear:both(不推存，增加了服务没用的结构)
		.使用成熟的清浮动样式类，clearfix
​	

定位：
	关于定位：可以使用css的position属性来设置元素的定位类型，position的设置项如下：
		.relative生成相对定位元素，元素所占据的文档流的位置不变，元素本身相对文档流的位置进行偏移。
		.bsolute生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，
		相对于上一个设置了相对或者绝对或者固定定位的父级元素来进行定位，如果找不到，则相对于body元素进行定位。
		.fixed生成固定定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。
		.static默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性。
		.inherit从父元素继承position属性的值。
	定位元素特性：
		绝对定位和固定定位的块元素和行内元素会自动转化为行内块元素
		
	定位元素层级：
		定位元素是浮动的正常的文档流之上的，可以用z-index属性来设置元素的层级 
​	如代码：
		<style type="text/css">
			.con{
				width: 400px;
				height: 400px;
				border: 1px solid #000;
				margin: 100px auto 0;
				position: relative;
			}

			.con div{
				background-color: gold;
				width: 200px;
				height: 100px;
				margin: 20px;
				text-align: center;
				line-height: 100px;
				font-size: 20px;
				position: absolute;
			}
			body .box01{
				background-color: green;
				z-index: 10;
			}
			body .box02{
				background-color: pink;
				left: 30px;
				top: 30px;
			}
			body .box03{
				top: 60px;
				left: 60px;
				background-color: gold;
				z-index: 11;
			}
		  
		</style>
	</head>
	<body>
		<div class="con">
			<div class="box01">1</div>
			<div class="box02">2</div>
			<div class="box03">3</div>
		</div>
	</body>
​	
​背景：
	background属性：
		background-color			设置背景颜色
		background-image			设置背景图片
		background-repeat			设置背景图片如何重复平铺（x：横向，y：水平，no-repeat：不重复）
		background-position			设置背景图片的位置（可以使用数组来设置背景图的位置，可以设置负值）一共有九中排列方法（left/right/botton/top/center）
		background-attachment		设置背景图片是固定还是随着页面滚动条滚动（fixed：背景图不随滚动条滚动）
​	background：可一进行简写：
		例如：
			background: url(image/location_bg.jpg) -110px -150px no-repeat;

	background-position实际例子：
		<style>
			.men{
				width: 400px;
				height: 200px;
				background-color: gold;
				border: 1px solid black;
				background-image: url(image/bg.jpg);
				background-repeat: no-repeat;
				background-position: left center;
			}
			.box4{
				width: 100px;
				height: 100px;
				border: 5px solid #000;
				background-image: url(image/location_bg.jpg);
				background-repeat: no-repeat;
				background-position: -110px -150px;
			}
		</style>
		</head>
		<body>
			<div class="men">
			</div>
			<div class="box4">
			</div>
		</body>
		
	
HTML5/CSS3
	CSS权重：
		css权重值得是样式的优先级，有两条或多条样式作用于一个元素，权重高的那条样式对元素起作用，权重相同的，后写的样式会覆盖前面写的样式。
		
	权重法的等级
	1、!important，加这样属性值后，权重值为10000
	2、内联样式，如：stype=""，权重值为1000
	3、ID选择器，如：#content，权重值为100
	4、类，伪类和属性选择器，如： content、:hover 权重值为10
	5、标签选择器和伪元素选择器，如：div、p、:before 权重值为1
	6、通用选择器（*）、子选择器（>）、相邻选择器（+）、同胞选择器（~）、权重值为0
	
	
	CSS3选择器：
		
		
		
		
		
		
		
		
		
JavaScript：
	页面行为：部分动画效果、页面与用户的交互、页面功能
	
	JavaScript嵌入页面的方式：
		1、行间时间（主要用于事件）
			<!-- onclick被点击后的事件 -->
			<input type="button" name="" value="弹框" onclick="alert('hello!')">
		
		2、页面script标签嵌入
			<script type="text/javascript">
				alert("hello world!")
			</script>
		
		3、外部引入
			<script type="text/javascript" src="../js/hell.js"></script>
	
	变量类型：
		5中基本数据类型：
		number、string、boolean、Undefined（未定义）、null（空对象）
		1中复合类型：
		object（对象）
		
	获取元素方法一：这个方法的语句如果放在代码文件的开头执行会出错，因为：程序是从上至下执行的当语句中获取的元素没有被加载会出现找不到属性的错误。解决方法，将js语句放在文档末尾执行	
		document.getElementById('')
		例如：
			<head>
				<script type="text/javascript">
					// 执行下面的语句会出现错误，因为javascript是从上而下执行语句的，当执行下面语句时会出现没有找到title属性
					document.getElementById('div1').title="我看到了！";
				</script>
			</head>
			<body>
				<div id="div1" class="div1" style="color: red;" title="这是div元素，看到了吗？">
					这是一个div元素
				</div>
			</body>
	方法二：将javascript语句放到Windows.onload触发的函数里面，获取元素的语句会在页面加载后才执行，就不会出错。
		例如：
		<head>
			<script type="text/javascript">
				// 执行下面的语句会出现错误，因为javascript是从上而下执行语句的，当执行下面语句时会出现没有找到title属性				
				//当整个文档加载玩之后再执行下面的语句
				window.onload = function(){
					document.getElementById('div1').title="我看到了！";
				}
			</script>
		</head>
		<body>
			<div id="div1" class="div1" style="color: red;" title="这是div元素，看到了吗？">
				这是一个div元素
			</div>
		</body>
	
	操作元素属性：
		获取的页面元素，就可以对也面元素的属性进行操作，属性的操作包括属性的读写。
		例如：
		<head>
			<script type="text/javascript">
				//当整个文档加载玩之后再执行下面的语句
			window.onload = function(){
					var oA  = document.getElementById('link1');
					// document.getElementById('link1').href= "http://www.baidu.com";
					// document.getElementById('link1').title="去到百度网首页"
					// 简写方法
					oA.href = "http://www.baidu.com";
					oA.title = "去到百度网";
					/*读属性*/
					alert(oA.id);
				}
				
			</script>
		</head>
		<body>
			<a href="#" id="link1">百度网</a>
		</body>
	操作属性的方法：
		1、"."操作
		2、"[]"操作
	属性写法（"."操作）不能写成变量
		1、html的属性和js里面属性写法一样
		2、"class"属性写成"className"
			例如：
				<head>
					<style>
						.box01{
							width: 200px;
							height: 200px;
							background-color: gold;
						}

						.box02{
							width: 300px;
							height: 300px;
							background-color: red;
						}
					</style>
					<script>
						window.onload = function(){
							var oDiv = document.getElementById('div1');
							oDiv.className = 'box02';
						} 
					</script>
					<title>操作class</title>
				</head>
				<body>
					<div class="box01" id="div1"></div>
					
				</body>
		
		
		3、"style"属性里面的属性，有横杠的改写成驼峰式，比如：“font-size”，改成“style.fontSize”
			例如：
				<head>
					<script type="text/javascript">
						window.onload = function(){
							var oDiv = document.getElementById('box01');
							oDiv.style.color = 'red';
							oDiv.style.background = "gold";
							oDiv.style.fontSize="30px";
						}
					</script>
				</head>
				<body>
					<div class="box01" id="box01">这是一个div元素</div>
				</body>
	属性写法（"[]"操作）：可以写成变量
		例如：
		<head>
			<title>元素操作使用[]方式</title>
			<script type="text/javascript">
				window.onload = function(){
					var oDiv = document.getElementById('div1');
					oDiv.style.color = 'black';
					var attr = 'background';
					oDiv.style[attr] = 'red';
				}
			</script>
		</head>
		<body>
			<div id="div1">这是一个div元素</div>
		</body>
		
	innerHTML：
		innerHTML可以读取或者写入标签包裹的内容
		例如：
			<head>
				<title>innerHTML</title>
				<script type="text/javascript">
					window.onload = function(){
						var oDiv = document.getElementById('div1');
						oDiv.style.color = 'black';
						var attr = 'background';
						oDiv.style[attr] = 'red';
						// innerHTML可以读取或者写入标签包裹的内容
						alert(oDiv.innerHTML);
						// 也可以写入类容
						var oDiv2 = document.getElementById('div2');
						// oDiv2.innerHTML = '这是第二个div元素';
						// 传入超链接内容
						oDiv2.innerHTML = "<a href = 'http://www.baidu.com'>百度网</a>"
					}
				</script>
			</head>
			<body>
				<body>
					<div id="div1">这是一个div元素</div>
					<div id="div2"></div>
				</body>
			</body>
	
	函数：
		函数定义与执行：
			<script type="text/javascript">
				// 函数定义
				function aa(){
					alert('hello!');
				}
				// 函数执行
				aa();
			</script>
			
		提取行间事件：
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>函数提取行间事件</title>
			<link rel="stylesheet" type="text/css" href="./css/1.css" id="links">
			<script type="text/javascript">
					window.onload = function(){
						var oBtn1 = document.getElementById('btn1');    //获取了id为btn1的input标签的属性
						oBtn1.onclick = Skin_replacement;
						function Skin_replacement() {
							var oLink = document.getElementById("links");
							oLink.href = "./css/2.css";
						}

						var oBtn1 = document.getElementById('btn2');
						oBtn1.onclick = Skin_replacement_01;
						function Skin_replacement_01() {
							var oLink = document.getElementById("links");
							oLink.href = "./css/1.css";
						}
					}
				</script>
			</head>
			<body>
				<input type="button" name="" value="skin01" id="btn1">
				<input type="button" name="" value="skin02" id="btn2">
				<div class="box01"></div>
				<div class="box02"></div>
			</body>
	
	变量与函数与解析：
		javascript解析过程分为两个阶段，显示编译阶段，然后执行阶段，
		在编译阶段会将function定义的函数提前，并且将var定义的变量声明提前，将它赋值为undefinde
		
		在js中如果调用函数是在函数的声明之前调用的话，js会与解析时直接将整个函数体提前解析
		<script type="text/javascript">    
			aa();       // 弹出 hello！
			alert(bb);  // 弹出 undefined
			function aa(){
				alert('hello!');
			}
			var bb = 123;
		</script>
		
	匿名函数：
		定义的函数可以不给名称，这个叫做匿名函数，可以将匿名函数直接复制给元素绑定的事件来完成匿名函数的调用。
		
		例如：
			<head>
				<title>匿名函数</title>
				<script>
					window.onload = function(){
						var oDiv = document.getElementById('div1');
						oDiv.onclick = function (){
							alert('hello');
						}
					}
				</script>
			</head>
			<body>
				<div id="div1">
					这是一个div
				</div>
			</body>
			
	函数传参--函数return关键字：
		传参：在给函数传参时，一次性可以传入多个形参但是形参和实参要一一对应，参数与参数之间使用逗号隔开。
		例如：
			<head>
				<title>函数传参和return关键字</title>
				<script>
					window.onload = function(){
						var oDiv = document.getElementById("div1");
						changestyle('color', 'red');
						changestyle('background', 'blue');
						changestyle('width', '300px');
						changestyle('height', '300px')
						changestyle('fontSize', '30px')
						
						function changestyle(styl, val){
							oDiv.style[styl] = val;
						}
					}
					
				</script>
			</head>
			<body>
				<div id="div1">div元素</div>
			</body>
			
	函数return关键字：
	作用：
		1、返回函数执行的结果
		2、结束函数的运行
		3、阻止默认行为
		
	例子代码：
		<head>
			<title>函数return关键字</title>
			<script>
				window.onload = function(){
					var oInput01 = document.getElementById("input01");
					var oInput02 = document.getElementById("input02");
					var oBtn = document.getElementById("btn");
					oBtn.onclick = function(){
						var a = oInput01.value;	//获取input中的value属性
						var b = oInput02.value;
						sum = add(a, b);
						alert(sum);
					}

					function add(a, b) {
						var sum = parseInt(a) + parseInt(b);	//parseInt数据类型的转化，将字符串类型转化成整形
						return sum;
					}
				}
			</script>
		</head>
		<body>
			<input type="text" name="" id="input01">
			<input type="text" name="" id="input02">
			<input type="button" name="" value="相加" id="btn">

		</body>
		
		
条件语句：
	通过条件来控制程序的走向，就需要用到条件语句。
	if...else
		例如：styl.display{block/none}显示和隐藏div盒子
			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>判断语句if_else</title>
				<style type="text/css">
					.box{
						width: 300px;
						height: 300px;
						background: gold;
					}
				</style>
				<script type="text/javascript">
					window.onload = function () {
						var oBtn = document.getElementById('btn');
						var oDiv = document.getElementById('box');
						
						oBtn.onclick = function(){
							console.log(oDiv);
							//这里第一次执行会去行间样式中找style.display，但是行间样式中没有style.display，所以if语句不成立执行else语句，在行间样式中插入style.display属性。第二次执行时就正常执行判断语句
							// if (oDiv.style.display == "block"){ 
							if (oDiv.style.display == "block" || oDiv.style.display == ""){
								oDiv.style.display = "none";
							}else{
								oDiv.style.display = "block";
							}
						}
					}
					
				</script>
			</head>
			<body>
				<input type="button" name=""  value= "切换" id="btn">
				<div class="box" id="box"></div>
			</body>
	
	if...else if...else
		例如：小名补习安排查询
			<script>
				var tday = 1;
				if (tday == 1){
					alert('语文');
				}else if (tday == 2){
					alert('数学');
				}else if (tday == 3){
					alert('英语');
				}else if (tday == 4){
					alert('美术');
				}else if (tday == 5){
					alert('舞蹈');
				}else{
					alert('不补习');
				}

			</script>
	
	switch：性能比if多分支要好
		例如：小名补习安排查询
			<script>
				var tday = 5;
				switch (tday){
					case 1:
						alert('语文');
					break;
					case 2:
						alert('数学');
					break;
					case 3:
						alert('英语');
					break;
					case 4:
						alert('美术');
					break;
					case 5:
						alert('舞蹈');
					break;
					default:
						alert('不补习');
				}
			</script>
		
	运算符：
		1、算术运算符：+(加)、-(减)、*(乘)、/(除)、%(求余)
		2、赋值运算符：=、+=、-=、*=、/=、%=
		3、条件运算符：==、===、>、>=、<、<=、!=、&&(而且)/||(或者)、!(否)
		
		
数组：数组中的数据类型可以不同
	创建数组的方法：
		<script>
			// 面向对象的方式创建数组
			var aRr = new Array(1,2,3,'abc');
			// 直接创建，性能比使用面向对象的方式创建的数组性能更高
			var aRr02 = [1,2,3,'cdf'];
		</script>
	数组的基本操作：
		var aRr02 = [1,2,3,'cdf'];

        // 获取数组中有多少个元素
        alert(aRr02.length);    //弹出4

        // 获取数组中某个元素，通过下标获取，下标从0开始计数
        alert(aRr02[3]);    //弹出cdf
		
	二维数组： var aRr03 = [[],[],[],[]];
		var aRr03 = [[1,2,3],['a','b','c'],[true, false]]
        // 获取数组中有多少个元素
        alert(aRr03.length);    //弹出3

        // 获取多维数组中某个数组中的元素个数
        alert(aRr03[0].length);  //弹出3

        // 获取多维数组中某个数组中的元素
        alert(aRr03[0][0]);     //弹出1
		
	数组常用方法：
	
		.join()将数组转化成字符串
        // var sTr = aRr.join(",");
        // alert(sTr);
        
        // .push()在数组最后添加元素
        aRr.push(5);
        
        // .pop()从数组最后删除一个元素
        aRr.pop();
        

        // .unshift()从数组前面增加元素
        aRr.unshift(0);

        // .reverse()数组反转
        aRr.reverse();
        alert(aRr)
       
        // .indexOf()返回数组中元素第一次出现的索引值
        var a = aRr.indexOf(1);
        alert(a);   //弹出3

        // splice()在数组中增加或删除成员
        // 从第2个元素开始，删除1个元素，然后在此位置增加指定元素
        var aRr2 = ['a','b','c','d','a','b','c','d'];
        /*
        // 删除元素
        aRr2.splice(2,1);   
        alert(aRr2);
        //弹出'a','b','d','a','b','c','d'
        */
        
        /*
        // 删除后增加新元素
        aRr2.splice(2,1,'e');
        alert(aRr2);    //弹出'a','b','e','d','a','b','c','d'
        */

        aRr2.splice(4,4,'e','f','g','h');
        alert(aRr2);    //弹出'a','b','c','d','e','f','g','h'
		
		

	标签选择器：document.getElementsByTagName('标签');
	获取的是一个标签选择集
	基本使用：
		<script>
			window.onload = function(){
				var aLi = document.getElementsByTagName('li');
				alert(aLi.length);

				// 设置背景色
				aLi[0].style.backgroundColor = 'gold';
				aLi[1].style.backgroundColor = 'blue';
			}
		</script>
		
	解决多个相同标签选择问题：
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>通过标签获取元素</title>
			<script>
				window.onload = function(){
					// 分类选择
					var oList = document.getElementById('list01');
					var aLi = oList.getElementsByTagName('li');
					alert(aLi.length);	//弹出8
					// 设置背景色
					aLi[0].style.backgroundColor = 'gold';
				}
			</script>
		</head>
		<body>
			<ul id="list01">
				<li>1</li>
				<li>2</li>
				<li>3</li>
				<li>4</li>
				<li>5</li>
				<li>6</li>
				<li>7</li>
				<li>8</li>
			</ul>

			<ul id="list02">
				<li>9</li>
				<li>10</li>
				<li>11</li>
				<li>12</li>
			</ul>
		</body>
		
循环语句：
	for循环
	例子：一次性操作多个标签的属性：
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>for循环</title>
			<script>
				window.onload = function(){
					var oList = document.getElementById('list01');
					var aLi = oList.getElementsByTagName('li');
					for(var i=0; i< aLi.length; i++){
						aLi[i].style.backgroundColor = "gold";
					}
				}
			</script>
		</head>
		<body>
			<ul id="list01">
				<li>1</li>
				<li>2</li>
				<li>3</li>
				<li>4</li>
				<li>5</li>
				<li>6</li>
				<li>7</li>
				<li>8</li>
				<li>9</li>
			</ul>
		</body>
			
	
	例子：隔行换色
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>for循环</title>
			<script>
				window.onload = function(){
					var oList = document.getElementById('list01');
					var aLi = oList.getElementsByTagName('li');

					for(var i=0; i< aLi.length; i++){
						// aLi[i].style.backgroundColor = "gold";
						if ( i % 2 == 0) {
							// console.log(i);
							aLi[i].style.backgroundColor = 'gold';
						}
						else{
							aLi[i].style.backgroundColor = '#f40';
					   }
					}
				}
			</script>
		</head>
		<body>
			<ul id="list01">
				<li>1</li>
				<li>2</li>
				<li>3</li>
				<li>4</li>
				<li>5</li>
				<li>6</li>
				<li>7</li>
				<li>8</li>
				<li>9</li>
			</ul>
		</body>
	
	
	
	数组去重：for循环+indexOf
		<script type="text/javascript">
			var aRr = [1,2,3,4,4,5,6,7,8,4,5,4,7,9,3,4,6,8,9,2];
			var aRr2 = [];
			for (var i = 0; i< aRr.length; i++){
				if (aRr.indexOf(aRr[i]) == i){
					aRr2.push(aRr[i]);
				}
			}
			console.log(aRr2);
		</script>
		
	
	
javascript组成：
	1、ECMAscript javascript的语法（变量、函数、循环语句等语法）
	2、DOM文档对象模型操作html和css的方法
	3、BOM浏览器对象模型操作浏览器的一些方法
	
字符串处理方法：
		
    字符串拼接 +
		var name = 'Tom';
        var age = 18;
        alert('我的名字叫' + name +  '，今年' + age + '岁');
        在使用+对字符串进行拼接时注意：整形和字符串进行拼接会将整形自动转换为字符串类型然后进行拼接
        var sum01 = 12;
        var sum02 = '23';
        alert( sum01 + sum02);  // 弹出1223

    parseInt()字符串转换成整形
		var a = 12;
		var b = '23';
		var c = 5.6;
		var d = '123abc';
		var e = 4.2;
		alert(parseInt(a) + parseInt(b));
		alert(parseInt(c));
		alert(parseInt(d));

    parseFloat()转换成浮点数
		var c = 5.6;
		var e = 4.2;
		alert(parseFloat(c) + parseFloat(e));

	浮点数精度问题：
		<script>
			var f = 0.1;
			var g = 0.2;
			alert(parseFloat(f) + parseFloat(g));   // 弹出：0.30000000000000004
		</script>
	解决方法：*100然后整体/100
		<script>
			var f = 0.1;
			var g = 0.2;
			alert((parseFloat(f)*100 + parseFloat(g)*100)/100);   // 弹出：0.3
		</script>
		
	split()把一个字符串分隔成字符串组成的数组
        var sTr = '2016-12-5';
        var aRr = sTr.split('-');
        var aRr2 = sTr.split('');
        console.log(aRr);
        console.log(aRr2);
		
	charAt()获取字符串中的某一个字符
        var sTr2 = '#div1';
        var sTr3 = '.div1';
        var sTr4 = sTr2.charAt(0);
        if (sTr4 == '#'){
            alert('id选择器');
        }else{
            alert('类选择器')
        }

    indexOf()查找字符串是否含有某个字符
        var sTr5 = 'Microsoft yahei';
        // 判断字符串中是否存在Microsoft，如果存在返回索引，没有查到就返回-1
        var num = sTr5.indexOf('Microsoft');
        var num01 = sTr5.indexOf('yahei');
        var num02 = sTr5.indexOf('xihei');
        alert(num);
        alert(num01);
        alert(num02);   //没有查找到

    substring()截取字符串，用法：substring(start, end)(不包括end)
        // var sTr6 = sTr5.substring(10,15);
        var sTr6 = sTr5.substring(10);
        alert(sTr6);
    toUpperCase()字符串转大写
        var sTr7 = "sunck is a good man"
        var sTr8 = sTr7.toUpperCase()
        alert(sTr8);

    toLowerCase()字符串转小写
        alert(sTr8.toLowerCase())

    字符串翻转
        var sTr9 = '1233asb789asdjal23234';
        var sTr001 = sTr9.split('').reverse().join('');    //返回一个数组然后使用数组的reverse方法，然后再将数组转换为字符串
        console.log(sTr001);    // 弹出：43232lajdsa987bsa3321

小练习：计算器
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>计算器</title>
		<script type="text/javascript">
			window.onload = function(){
				var oInpt01 = document.getElementById('input01');
				var oInpt02 = document.getElementById('input02');
				var oSum = document.getElementById('sum');
				var oPt = document.getElementById('opt01');
				var oBtn = document.getElementById('btn')
				oBtn.onclick = function(){
					var a = oInpt01.value;
					var b = oInpt02.value;
					var opt = oPt.value;
					if (opt == '0'){
						oSum.value = parseInt(a) + parseInt(b);
					}
					else if(opt == '1'){
						oSum.value = parseInt(a) - parseInt(b);
					}
					else if(opt == '2'){
						oSum.value = parseInt(a) * parseInt(b);
					}
					else{
						oSum.value = parseInt(a) / parseInt(b);
					}
				}
			}
		</script>
	</head>
	<body>
		<h1>计算器</h1>
		<input type="text" name="" id="input01">
		<select name="" id="opt01">
			<!-- 
				value = 0表示加好
				1表示：-
				2表示：*
				3表示：/
			-->
			<option value="0">+</option>
			<option value="1">-</option>
			<option value="2">*</option>
			<option value="3">/</option>
		</select>
		<input type="text" name="" id="input02">
		<span>=</span>
		<input type="text" name="" id="sum">
		<button id="btn">计算</button>
	</body>