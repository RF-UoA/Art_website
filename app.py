import os
from flask import Flask, render_template, request, redirect, url_for
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open(os.path.join(app.static_folder, 'assets/artwork.yaml')) as f:
        works = yaml.safe_load(f)

    works_dict = []
    for artwork in works['artwork']:
        for key, value in artwork.items():
            works_dict.append(value)
    
    filenames = [i['filename'] for i in works_dict]

    scaled_folder = os.path.join(app.static_folder, 'assets/scaled')
    images = ['/'.join(['assets/scaled', filename]) for filename in filenames]
    print(works_dict[0])
    return render_template('available-works.html', title='Available Works', images=images, works=works_dict)

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
