# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class librairie_app(models.Model):
#     _name = 'librairie_app.librairie_app'
#     _description = 'librairie_app.librairie_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
# hhh
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
