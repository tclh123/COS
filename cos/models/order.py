# coding=utf-8

from cos.models.user_cart import UserCart
from cos.models.menu import Menu
from cos.ext import db


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status_id = db.Column(db.SmallInteger, nullable=False)
    delivery_time = db.Column(db.DateTime, default=None)
    delivery_spot = db.Column(db.Unicode(1024), default=None)
    payment_kind = db.Column(db.Integer, default=None)
    is_paid = db.Column(db.Boolean, nullable=False, default=0)
    deliveryman_id = db.Column(db.Integer, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return ('<Order(id=%r, user_id=%r, status_id=%r)>'
                % (self.id, self.user_id, self.status_id))

    @property
    def status(self):
        return OrderStatus.query.get(self.status_id)

    # FIXME: 处理下架
    @property
    def menus(self):
        order_meals = OrderMeal.query.filter_by(order_id=self.id).all()
        return [(om.menu, om.amount) for om in order_meals]

    @classmethod
    def from_user_cart(cls, user_id):
        carts = UserCart.query.filter_by(user_id=user_id).all()
        order = cls(user_id=user_id, status_id=1)
        db.session.add(order)
        db.session.commit()
        if order.id:
            for cart in carts:
                OrderMeal.add(order.id, cart)
            UserCart.query.filter_by(user_id=user_id).delete()
            db.session.commit()
            return order
        else:
            return None

    @property
    def price_sum(self):
        return sum([menu.price_value * amount for menu, amount in self.menus])

    @property
    def display_price_sum(self):
        return '%.2f' % self.price_sum

    def submit_form(self, delivery_time, delivery_spot, payment_kind):
        self.delivery_time = delivery_time
        self.delivery_spot = delivery_spot
        self.payment_kind = payment_kind
        db.session.commit()


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
    menu_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('order_id', 'menu_id', name='uk_order_id_menu_id'),
    )

    def __repr__(self):
        return ('<OrderMeal(id=%r, order_id=%r, meal_id=%r)>'
                % (self.id, self.order_id, self.meal_id))

    @property
    def menu(self):
        return Menu.query.get(self.menu_id)

    @classmethod
    def add(cls, order_id, cart):
        om = cls(order_id=order_id, meal_id=cart.meal_id,
                 menu_id=cart.menu_id, amount=cart.amount or 1)
        db.session.add(om)
        db.session.commit()
        return om
