from odoo import http
from odoo.addons.librairie_app.controllers.controllers import Books
class BooksExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get("available"):
            all_books = response.qcontext["books"]
            available_books = all_books.filtered("is_available")
            response.qcontext["books"] = available_books
        return response