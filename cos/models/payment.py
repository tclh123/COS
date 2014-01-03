# coding=utf-8

from cos.ext import db


class PaymentKind(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.Unicode(200), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<PaymentKind(id=%r, desc=%r)>'
                % (self.id, self.desc))
