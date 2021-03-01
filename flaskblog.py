from flask import Flask, render_template, url_for


app = Flask(__name__)


posts =[
    {
        'author': 'Ricardo Sanchez',
        'title': 'Blog Post 1',
        'content': 'First blog post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Emma Sanchez',
        'title': 'Blog Post 2',
        'content': 'Blog post from Emma content',
        'date_posted': 'March 13, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')
    

if __name__ == '__main__':
    app.run(debug=True)
