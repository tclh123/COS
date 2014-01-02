# coding=utf-8

from cos.ext import db


class Menu(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, nullable=False, unique=True)
    sale_price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=0)
    buying_amount = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Menu(meal_id=%r, sale_price=%r)>'
                % (self.meal_id, self.sale_price))
