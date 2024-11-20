from flask import Flask, render_template, request
from utils.dummy_data import data
from utils.categories import blog_categories

app = Flask(__name__)

names = [
    'Vilhelm',
    'Carina',
    'Carlos',
    'Lwanyo',
    'Eir',
    'Lisandro'
]


blog = [item for item in data if item['id'] == 4]

url = 'https://cats-paradise-f994f218e0ee.herokuapp.com/api/v1/cats'

def our_decorator(func):
    def wrapper_func():
        print('Pring it before')
        func()
        print('after the function')
    return wrapper_func


@our_decorator
def say_hello():
    print('hello everyone!')


say_hello()

@app.route('/')
def home():
    return render_template('index.html', year = 2024, first_name = 'Asabeneh', age = 250, names = names)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html', data = data)

@app.route('/blogs/<id>')
def blog_details(id):
    blog = [item for item in data if item['id'] == int(id)]
    return render_template('blog-details.html', blog = blog[0])

@app.route('/blogs/add', methods = ['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        subtitle = form.get('subtitle')
        content = form.get('content')
        category = form.get('category')
        tags = form.get('tags')
        file = request.files.get('cover_img')
        print(title, subtitle, content, category, tags, file)
        print('this is the post route of adding')
        return 'posted'
        
    return render_template('add-blog.html', categories = blog_categories)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 5000)


'''
CRUD:
Create: POST
Read: GET
Update: PUT/PATCH
Delete: DELETE



'''