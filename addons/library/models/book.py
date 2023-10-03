from odoo import fields, models


class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    currency_id = fields.Many2one('res.currency', string='Currency')

    name = fields.Char()
    active = fields.Boolean(default=True)
    isbn = fields.Char()
    genre = fields.Char()
    summary = fields.Text()
    author = fields.Char()
    format = fields.Selection(selection=[
        ("paperback", "Paperback"),
        ("hardcover", "Hardcover"),
        ("audiobook", "Audiobook"),
        ("ebook", "E-Book"),
    ])
    language = fields.Selection(selection=[
        ("en", "Inglés"),
        ("es", "Español"),
        ("fr", "Francés"),
        ("de", "Alemán"),
    ])
    edition = fields.Integer()
    publisher = fields.Char()
    publish_date = fields.Date()
    price = fields.Monetary(string="Book price", currency_field="currency_id")
