from flask import Blueprint, render_template

from src.models import IncomeData, OutcomeData

main = Blueprint('main', __name__)

@main.route('/')
def index():

    form_inc = IncomeData.query.all()
    form_out = OutcomeData.query.all()

    total_income = 0
    for total in form_inc:
        total_income += total.value_income

    total_outcome = 0
    for total in form_out:
        total_outcome += total.value_outcome

    total = total_income - total_outcome

    return render_template('index.html',
        form_inc = form_inc,
        form_out = form_out,
        total_income = round(total_income, 2),
        total_outcome = round(total_outcome, 2),
        total = round(total, 2)
    )