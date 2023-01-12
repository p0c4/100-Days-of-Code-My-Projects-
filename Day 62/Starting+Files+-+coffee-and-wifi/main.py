from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


# list_of_rows = [['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power'], ['Lighthaus', 'https://goo.gl/maps/2EvhB4oq4gyUXKXx9', '11AM', ' 3:30PM', '☕☕☕☕️', '💪💪', '🔌🔌🔌'],
# ['Esters', 'https://goo.gl/maps/13Tjc36HuPWLELaSA', '8AM', '3PM', '☕☕☕☕', '💪💪💪', '🔌'], ['Ginger & White', 'https://goo.gl/maps/DqMx2g5LiAqv3pJQ9', '7:30AM', '5:30PM', '☕☕☕', '✘', '🔌'],
# ['Mare Street Market', 'https://goo.gl/maps/ALR8iBiNN6tVfuAA8', '8AM', '1PM', '☕☕', '💪💪💪', '🔌🔌🔌']]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    open = StringField('Open time', validators=[DataRequired()])
    close = StringField('Close time', validators=[DataRequired()])
    coffee = SelectField(u'Coffee rating', choices=[(0, '✘'), (1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️') ], validators=[DataRequired()])
    wifi = SelectField(u'Wifi rating', choices=[(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪') ], validators=[DataRequired()])
    power = SelectField(u'Power rating', choices=[(0, '✘'), (1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌') ], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=' ')
            csv_writer.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
