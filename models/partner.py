# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'

    no_ktp = fields.Char('No KTP', required=True)

from odoo.addons.portal.controllers.portal import CustomerPortal

CustomerPortal.OPTIONAL_BILLING_FIELDS.append('no_ktp')