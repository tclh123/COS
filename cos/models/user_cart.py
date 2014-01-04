# coding=utf-8

from cos.models.menu import Menu
from cos.ext import db


class UserCart(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, nullable=False)
    menu_id = db.Column(db.Integer, nullable=False)  # 指向不存在则表示已经下架
    amount = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'menu_id', name='uk_user_id_menu_id'),
    )

    def __repr__(self):
        return ('<UserCart(id=%r, user_id=%r, meal_id=%r, amount=%r)>'
                % (self.id, self.user_id, self.meal_id, self.amount))

    def commit(self):
        cart = UserCart.query.filter_by(user_id=self.user_id,
                                        menu_id=self.menu_id).first()
        if cart:
            cart.amount += self.amount or 1
            db.session.add(cart)
        else:
            db.session.add(self)
        db.session.commit()

    @property
    def menu(self):
        return Menu.query.get(self.menu_id)
