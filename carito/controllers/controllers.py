# -*- coding: utf-8 -*-
# from odoo import http


# class Carito(http.Controller):
#     @http.route('/carito/carito/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carito/carito/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('carito.listing', {
#             'root': '/carito/carito',
#             'objects': http.request.env['carito.carito'].search([]),
#         })

#     @http.route('/carito/carito/objects/<model("carito.carito"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carito.object', {
#             'object': obj
#         })
