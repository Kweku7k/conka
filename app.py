from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ibuy')
def ibuy():
    return render_template('iBuy.html')

@app.route('/<string:brand>')
def products(brand):
    print(brand)
    return render_template('products.html')

@app.route('/description')
def description():
    return render_template('description.html')
if __name__ == '__main__':
    app.run(debug=True)