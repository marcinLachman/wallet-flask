from flask import Blueprint, render_template, redirect, url_for, flash

from src import db
from src.models import IncomeData, OutcomeData
from src.data_wallet.forms import WalletForm

data_wallet = Blueprint('data_wallet', __name__)

@data_wallet.route('/add-income', methods=['GET', 'POST'])
def add_income():
    form = WalletForm()

    if form.validate_on_submit():
        data = IncomeData (
            name_income = form.title.data,
            value_income = form.value.data
        )
        db.session.add(data)
        db.session.commit()
        
        flash('Your Income added !!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add_income.html', 
    title="Add Income",
    form=form
    )

@data_wallet.route('/add-outcome', methods=['GET', 'POST'])
def add_outcome():
    form = WalletForm()

    if form.validate_on_submit():
        data = OutcomeData (
            name_outcome = form.title.data,
            value_outcome = form.value.data
        )
        db.session.add(data)
        db.session.commit()
        
        flash('Your Outcome added !!', 'error')
        return redirect(url_for('main.index'))

    return render_template('add_outcome.html', 
        title='Add Outcoome',
        form=form
        )

@data_wallet.route('/update-data-inc/<int:id>/update', methods=['GET', 'POST'])
def update_data_inc(id):
    data_inc = IncomeData.query.get_or_404(id)
    form = WalletForm()

    if form.validate_on_submit():
        data_inc.name_income = form.title.data
        data_inc.value_income = form.value.data
        db.session.commit()
        
        flash('Your Income Updated !!', 'success')
        return redirect(url_for('main.index'))

    form.title.data = data_inc.name_income
    form.value.data = data_inc.value_income

    return render_template('update_data_inc.html', 
        title='Update incoome',
        form=form
    )

@data_wallet.route('/update-data-out/<int:id>/update', methods=['GET', 'POST'])
def update_data_out(id):
    data_out = OutcomeData.query.get_or_404(id)
    form = WalletForm()

    if form.validate_on_submit():
        data_out.name_outcome = form.title.data
        data_out.value_outcome = form.value.data
        db.session.commit()
        
        flash('Your Outcome Updated !!', 'error')
        return redirect(url_for('main.index'))

    form.title.data = data_out.name_outcome
    form.value.data = data_out.value_outcome

    return render_template('update_data_out.html',
        title='Update Outcoome',
        form=form
    )