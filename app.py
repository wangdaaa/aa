from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('sdfasdf')
    print('这是更新程序vvv的sssss')
    print('sssssfd')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
