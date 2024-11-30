from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class GameForm(FlaskForm):
    title = StringField("Назва гри", validators=[DataRequired(), Length(max=100)])
    price = FloatField("Ціна (грн)", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Додати гру")

class ReviewForm(FlaskForm):
    reviewer = StringField("Ваше ім'я", validators=[DataRequired(), Length(max=50)])
    text = TextAreaField("Ваш відгук", validators=[DataRequired(), Length(max=300)])
    submit = SubmitField("Залишити відгук")
