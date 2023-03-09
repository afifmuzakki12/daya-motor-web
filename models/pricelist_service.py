# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PricelistService(models.Model):
    _name = 'pricelist.service'

    unit_name = fields.Char("Jenis Motor", size=100, required=True)
    
    @api.model
    def _get_default_currency(self):
        currency = self.env['res.currency'].search([('name', '=', 'IDR')], limit=1)
        return currency
    
    currency_id = fields.Many2one("res.currency", string='Currency', default=_get_default_currency, readonly=True, help='Select Currency', ondelete='restrict')
    service_price = fields.Monetary("Jasa Service Lengkap", required=True)
    promo_service_price = fields.Monetary("Promo Jasa Service")
