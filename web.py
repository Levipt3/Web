from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    # 自动打开文件，并返回内容
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/music')
def music():
    return render_template('/music.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/register.html')
    else:
        # 处理注册逻辑
        username = request.form.get('username')
        password = request.form.get('password')
        sex = request.form.get('sex')
        hobby = request.form.getlist('hobby')
        city = request.form.get('city')
        print(username, password, sex, hobby, city)
        # 处理注册逻辑
        return '注册成功'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/login.html')
    else:
        print(request.form.get('username'), request.form.get('password'))
        return '登录成功'


if __name__ == '__main__':
    app.run(debug=True)
