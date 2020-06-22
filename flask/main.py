from flask import Flask, render_template, url_for

# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为工程目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)
@app.route('/')
def index():
    """定义的视图函数"""
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')





if __name__ == '__main__':
    app.run(debug=True)