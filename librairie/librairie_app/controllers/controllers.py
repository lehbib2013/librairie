# -*- coding: utf-8 -*-
from odoo import http


# class LibrairieApp(http.Controller):
#     @http.route('/librairie_app/librairie_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librairie_app/librairie_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('librairie_app.listing', {
#             'root': '/librairie_app/librairie_app',
#             'objects': http.request.env['librairie_app.librairie_app'].search([]),
#         })

#     @http.route('/librairie_app/librairie_app/objects/<model("librairie_app.librairie_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librairie_app.object', {
#             'object': obj
#         })
class Books(http.Controller):
    @http.route("/library/books")
    def list(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.search([])
        return http.request.render("librairie_app.book_list_template", {"book": books})