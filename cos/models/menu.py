# coding=utf-8

import decimal

from cos.models.meal import Meal
from cos.models.utils import cached_property
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

    @cached_property
    def meal(self):
        return Meal.query.get(self.meal_id)

    @property
    def is_discount(self):
        return self.meal and self.meal.price > self.sale_price

    @property
    def price_value(self):
        return decimal.Decimal(self.sale_price) / 100

    @property
    def display_price(self):
        return '%.2f' % float(self.price_value)
