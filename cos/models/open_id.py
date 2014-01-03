# coding=utf-8

from cos.ext import db


class OpenIdKind(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    kind_name = db.Column(db.Unicode(100), nullable=False, unique=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<OpenIdKind(id=%r, kind_name=%r)>'
                % (self.id, self.kind_name))
