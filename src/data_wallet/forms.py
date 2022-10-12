from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length

class WalletForm(FlaskForm):
    title = StringField('Title', render_kw={"placeholder": "Description"}, validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])
    value = DecimalField('Value', places=2, default=0.00, validators=[
        DataRequired()
    ])
    submit = SubmitField('Add')