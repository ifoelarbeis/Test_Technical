# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RegistrasiProduct(models.Model):
    _name = 'registrasi.product'
    _description = 'Registrasi Product'

    code 			= fields.Char(string="Code", required=True)
    name 			= fields.Char(string="Material Name", required=True)
    material_type 	= fields.Selection([('Fabric','Fabric'),('Jeans','Jeans'),('Cotton','Cotton')], string="Material Type",required=True)
    buy_price 		= fields.Float(string="Material buy Price", required=True)
    supplier_id 	= fields.Many2one('res.partner', string="Supplier", required=True, domain=[('supplier_rank','>=',1)])


    @api.constrains('buy_price')
    def _cek_buy_price(self):
    	for rec in self :
    		if rec.buy_price < 100 :
    			raise ValidationError("Material Buy Price tidak boleh < 100 ...!!")


