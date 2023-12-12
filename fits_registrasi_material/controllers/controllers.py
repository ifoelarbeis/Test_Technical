# -*- coding: utf-8 -*-
# from odoo import http


# class FitsRegistrasiMaterial(http.Controller):
#     @http.route('/fits_registrasi_material/fits_registrasi_material', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fits_registrasi_material/fits_registrasi_material/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fits_registrasi_material.listing', {
#             'root': '/fits_registrasi_material/fits_registrasi_material',
#             'objects': http.request.env['fits_registrasi_material.fits_registrasi_material'].search([]),
#         })

#     @http.route('/fits_registrasi_material/fits_registrasi_material/objects/<model("fits_registrasi_material.fits_registrasi_material"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fits_registrasi_material.object', {
#             'object': obj
#         })
