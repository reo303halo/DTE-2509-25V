from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    year = IntegerField("Year", validators=[DataRequired(), NumberRange(min=1800, max=2025)])
    country = StringField('Country', validators=[DataRequired(), Length(max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(max=50)])
    age_rating = IntegerField('Age Rating', validators=[DataRequired(), NumberRange(min=0, max=18)])
    duration = IntegerField('Duration (minutes)', validators=[DataRequired(), NumberRange(min=1)])
    price = FloatField('Price (NOK)', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Add")