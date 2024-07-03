from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('available-works.html', title='Available Works')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Posts')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the contact form submission here
        pass
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
