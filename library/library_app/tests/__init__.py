from . import test_book
from odoo.tests.common import TransactionCase
class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Book = self.env["librairie.book"]
        self.book1 = self.Book.create({
            "name": "Odoo Development Essentials",
            "isbn": "879-1-78439-279-6"
        })
    def test_book_create(self):
        "New Books are active by default"
        self.assertEqual(
        self.book1.active, True
        )