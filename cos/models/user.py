# coding=utf-8

from flask.ext.login import UserMixin

from cos.models.permission import Permission
from cos.models.utils import cached_property
from cos.ext import db


class User(db.Model, UserMixin):
    """UserMixin provides
        def is_active(self):
        def is_authenticated(self):
        def is_anonymous(self):
        def get_id(self):"""

    id = db.Column(db.Integer, primary_key=True)
    open_id_kind = db.Column(db.Integer, nullable=False)
    open_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Unicode(100), nullable=False)
    email = db.Column(db.Unicode(64), nullable=False)
    type = db.Column(db.Unicode(16), nullable=False)  # in ('user', 'staff')
    target_id = db.Column(db.Integer, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('open_id_kind', 'open_id', name='uk_open_id'),
    )

    def __repr__(self):
        return ('<User(id=%r, name=%r, type=%r)>'
                % (self.id, self.name, self.type))

    # def get_auth_token(self):
    #     data = (self.id, sha1(self.password).hexdigest())
    #     return login_serializer.dumps(data)

    @property
    def is_staff(self):
        return self.type == 'staff' and self.target_id is not None

    @cached_property
    def staff(self):
        return self.target_id and Staff.query.get(self.target_id)

    @property
    def permissions(self):
        return self.staff and self.staff.permissions


class Staff(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Staff(id=%r, permissions=%r)>'
                % (self.id, self.permissions))

    @cached_property
    def perms(self):
        perms = Permission.query.all()
        return filter(lambda x: self.permissions & x.value, perms)

    @property
    def permission_descs(self):
        return [p.desc for p in self.perms]


class DeliveryMan(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<DeliveryMan(id=%r, user_id=%r)>'
                % (self.id, self.user_id))
