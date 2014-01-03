# coding=utf-8

from cos.ext import db


class Permission(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.BigInteger, nullable=False, unique=True)
    desc = db.Column(db.Unicode(200), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Permission(id=%r, value=%r, desc=%r)>'
                % (self.id, self.value, self.desc))
