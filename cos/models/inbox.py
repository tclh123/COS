# coding=utf-8

from cos.ext import db


class Inbox(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    is_read = db.Column(db.TinyInteger, nullable=False, default=0)
    content = db.Column(db.Unicode(1024), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Inbox(id=%r, user_id=%r, is_read=%r, content=%r)>'
                % (self.id, self.user_id, self.is_read, self.content))
