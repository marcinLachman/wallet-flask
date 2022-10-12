from src import db
from sqlalchemy.sql import func

from datetime import datetime

class IncomeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_income = db.Column(db.String(100))
    value_income = db.Column(db.Float())
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return self.name_income

class OutcomeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_outcome = db.Column(db.String(100))
    value_outcome = db.Column(db.Float())
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return self.name_outcome
