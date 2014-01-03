# coding=utf-8

from cos.ext import db


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status_id = db.Column(db.SmallInteger, nullable=False)
    delivery_time = db.Column(db.DataTime, default=None)
    delivery_spot = db.Column(db.Unicode(1024), default=None)
    payment_kind = db.Column(db.Integer, default=None)
    is_paid = db.Column(db.TinyInteger, nullable=False, default=0)
    deliveryman_id = db.Column(db.Integer, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Order(id=%r, user_id=%r, status_id=%r)>'
                % (self.id, self.user_id, self.status_id))


class OrderStatus(db.Model):

    id = db.Column(db.SmallInteger, primary_key=True)
    desc = db.Column(db.Unicode(200), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<OrderStatus(id=%r, desc=%r)>'
                % (self.id, self.desc))


class OrderMeal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('order_id', 'meal_id', name='uk_order_id_meal_id'),
    )

    def __repr__(self):
        return ('<OrderMeal(id=%r, order_id=%r, meal_id=%r)>'
                % (self.id, self.order_id, self.meal_id))
