from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html',value ='Hi')
    if request.method == 'POST':
        return render_template('result.hmtml')

if __name__ == '__main__':
    app.run(debug=True)
