from flask import Flask, render_template, url_for, redirect

#create an instance object of the flask class
app = Flask(__name__, static_url_path="/static")



# routes/links to the respective pages on our website
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/products')
def products():
    return render_template('products.html', title="Products")



if __name__=='__main__':
    app.run(debug=True)