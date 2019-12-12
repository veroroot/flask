from flask import Flask, escape, request, render_template
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

# @app.route 는 일종의 mapping이라고 할 수 있다.
# app.route('127.0.0.1:5000/')에 해당됨.
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# app.route('127.0.0.1:5000/hi')에 해당됨.
@app.route('/hi')
def hi():
    return 'hi'

@app.route('/veroroot')
def veroroot():
    return 'hello veroroot'

# app.route에 있는 주소값과 밑에있는 함수명과 같은것이 관례
@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

@app.route('/variable')
def variable():
    name = '해피해킹'
    return render_template('variable.html', html_name=name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name=def_name)

# /cube/3 => 3의 세제곱은 27입니다.
@app.route('/cube/<int:input_num>/')
def cube(input_num):
    output_num = input_num ** 3
    return render_template('cube.html', html_output_num=output_num, html_input_num=input_num)

'''
점심메뉴 가져오기
@app.route('/lunch')
def launch():
    url = 'https://www.google.com/search?tbm=lcl&ei=nKPxXdiCFPaLr7wP4Nu74A4&q=%EC%97%AD%EC%82%BC%EC%97%AD+%EB%A7%9B%EC%A7%91&oq=%EC%97%AD%EC%82%BC%EC%97%AD+%EB%A7%9B%EC%A7%91&gs_l=psy-ab.3...0.0.0.313969.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.01OBIJEib-o#rlfi=hd:;si:;mv:[[37.508146499999995,127.04444950000001],[37.4935666,127.0295757]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #rl_ist0 > div.rl_tile-group.r-iASVb08_KykM > div.rlfl__tls.rl_tls.r-i6cZYGLKe11w > div:nth-child(2) > div > div.uMdZh.rl-qs-crs-t.mnr-c.iXi_ecVQ_EZ0-QjYh_nvGmIg > div > a > div > div.dbg0pd > div
    key_selector = '#rl_ist0 > div.rl_tile-group.r-iASVb08_KykM > div.rlfl__tls.rl_tls.r-i6cZYGLKe11w > div > div > div > div > a > div.cXedhc.uQ4NLd > div.dbg0pd > div'
    keys = soup.select(key_selector)
    key_list = [key.text for key in keys]
    #rl_ist0 > div.rl_tile-group.r-ipz1qm6yZFLA > div.rlfl__tls.rl_tls.r-iCVWqFUEnR6s > div:nth-child(21) > div > div.uMdZh.rl-qs-crs-t.mnr-c.iSB6kHufZYJs-QjYh_nvGmIg > div > a > div > div.b9tNq
    #rlimg0_0 ~ #rling0_20
    img_selector = '#rlimg0_0'
    img_list = []
    for num in range(0,21):
        img_sel = img_selector
        img_sel.replace(img_selector[-1], str(num))
        img = soup.select_one(img_sel)
        if 'src' in img.attrs:
            image = img.attrs['src']
            img_list.append(image)
    menu=[[key, img] for (key, img) in (key_list, img_list)]
    menu_select = random.choice(menu)
    return render_template('lunch.html', a=img_sel, b=img, key=menu_select[0] ,image=menu_select[1])
'''

@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '쥬만지', '포드v페라리']
    return render_template('movies.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    #request.args => GET방식으로 데이터가 들어온다면
    #print (request.form.get('keyword'))
    # keyword = request.args.get('keyword')
    keyword = request.form.get('keyword')
    return render_template('pong.html', keyword=keyword)



if __name__== '__main__' :
    app.run(debug=True)