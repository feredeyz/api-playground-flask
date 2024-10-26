from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class WeatherForm(FlaskForm):
    city = StringField('City: ', name='city', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Check')