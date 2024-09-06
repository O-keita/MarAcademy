from flask import Flask, render_template
from form import LoginForm, RegisterForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dasboard.html')

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    return render_template('courses.html')


if __name__ == "__main__":
    app.run(debug=True)