# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PricelistUnit(models.Model):
    _name = 'pricelist.unit'

    # id_wilayah = fields.Char("Kode Wilayah")

    unit_tipe = fields.Many2one("product.public.category", required=True)
    product = fields.Many2one("product.template", required=True)
    nama_tipe = fields.Char(string="Nama Tipe Variant Product", required=True)

    @api.model
    def _get_default_currency(self):
        currency = self.env['res.currency'].search([('name', '=', 'IDR')], limit=1)
        return currency
    
    currency_id = fields.Many2one("res.currency", string='Currency', default=_get_default_currency, readonly=True, help='Select Currency', ondelete='restrict')

    unit_price = fields.Monetary("Harga", required=True)
