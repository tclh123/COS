# coding=utf-8

from cos.ext import db


class UserCart(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<UserCart(id=%r, user_id=%r, meal_id=%r, amount=%r)>'
                % (self.id, self.user_id, self.meal_id, self.amount))
