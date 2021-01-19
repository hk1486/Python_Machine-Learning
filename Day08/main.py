from flask import Flask, render_template, request
# Flask 서버
# - 웹서비스를 사용하게 하는 기능
# - static, templates 폴더안에 웹 문서와 리소스를 저장
# - static : 정적파일, template : 웹문서를 저장

# post : 데이터를 body에 넣어 전달하는 방법
# get : 데이터를 URL에 실어 전달하는 방법

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])  # '/'로 들어오게 되면 호출
def index():
    return render_template('index.html') # 이 코드가 실행

if __name__ == '__main__':
    app.run(debug=True)