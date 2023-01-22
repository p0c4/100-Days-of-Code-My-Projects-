from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all(


##WTForm
class CreateUser(FlaskForm):
    name= StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up!", )

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():    
    if request.method == "POST":
        
        form_name = request.form.get('name')
        form_email = request.form.get('email')

        with app.app_context():
            if User.query.filter_by(email=form_email).first():
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))
            
            hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=form_email, name=form_name, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            #Log in and authenticate user after adding details to database.
            login_user(new_user)
            return redirect(url_for("secrets"))
                
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        with app.app_context():
        #Find user by email entered.
            user = User.query.filter_by(email=email).first()
            if user:        
                #Check stored password hash against entered password hashed.
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('secrets'))
                else:
                    flash('Password incorrect, please try again.')
                    return render_template("login.html")
            else:
                flash("That email does not exist, please try again.")
                return render_template("login.html")

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
