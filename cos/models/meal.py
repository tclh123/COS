# coding=utf-8

import decimal

from cos.ext import db


class Meal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(200), nullable=False)
    price = db.Column(db.Integer, nullable=False, default=0)
    desc = db.Column(db.Unicode(1024), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Meal(id=%r, name=%r, price=%r, desc=%r)>'
                % (self.id, self.name, self.price, self.desc))

    @property
    def price_value(self):
        return decimal.Decimal(self.price) / 100

    @property
    def display_price(self):
        return '%.2f' % float(self.price_value)
