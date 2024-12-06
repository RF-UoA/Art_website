import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    scaled_folder = os.path.join(app.static_folder, 'assets/scaled')
    images = ['/'.join(['assets/scaled', filename]) for filename in os.listdir(scaled_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('available-works.html', title='Available Works', images=images)

# @app.route('/posts')
# def posts():
#     return render_template('posts.html', title='Posts')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/portfolio')
def portfolio():
    works_folder = os.path.join(app.static_folder, 'assets/works')
    images = ['/'.join(['assets/works', filename]) for filename in os.listdir(works_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('portfolio.html', title='Portfolio', images=images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the contact form submission here
        pass
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
