# coding=utf-8

from cos.ext import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    open_id_kind = db.Column(db.Integer, nullable=False)
    open_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Unicode(100), nullable=False)
    email = db.Column(db.Unicode(64), nullable=False)
    type = db.Column(db.Unicode(16), nullable=False)
    target_id = db.Column(db.Integer, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('open_id_kind', 'open_id', name='uk_open_id'),
    )

    def __repr__(self):
        return ('<User(id=%r, name=%r, type=%r)>'
                % (self.id, self.name, self.type))


class Staff(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Staff(id=%r, permissions=%r)>'
                % (self.id, self.permissions))


class DeliveryMan(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<DeliveryMan(id=%r, user_id=%r)>'
                % (self.id, self.user_id))
