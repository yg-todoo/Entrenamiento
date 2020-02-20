# -*- coding: utf-8 -*-

from odoo import models, fields


class caritoM(models.Model):
     _name = 'caritoM.caritoM'
     _description = 'caritoM.caritoM'

     Nombre = fields.Char()
     Edad = fields.Integer()
     Costo = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
