from odoo import fields, models


class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name = fields.Char()
    active = fields.Boolean(default=True)
    isbn = fields.Char()
    genre = fields.Char()
    summary = fields.Text()
    author = fields.Char()
    format = fields.Selection(selection=[
        "Paperback", "Hardcover", "Audiobook", "E-Book"
    ])
    language = fields.Selection(selection=[
        "en", "es", "fr", "de"
    ])
    edition = fields.Integer()
    publisher = fields.Char()
    publish_date = fields.Date()
    price = fields.Monetary()
