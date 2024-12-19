from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)