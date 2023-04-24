from marshmallow import Schema, fields


class OrderResponseSchema(Schema):
    posted_on = fields.Str(required=True)
    book_title = fields.Str(required=True)
    book_author = fields.Str(required=True)
    delivery_address = fields.Str(required=True)
    price_to_pay = fields.Float(required=True)
    payment_link = fields.Str(required=False)
    quantity = fields.Integer(required=True)


class ClientOrderResponseSchema(Schema):
    posted_on = fields.Str(required=True)
    book_title = fields.Str(required=True)
    book_author = fields.Str(required=True)
    delivery_address = fields.Str(required=True)
    price_to_pay = fields.Float(required=True)
    quantity = fields.Integer(required=True)
