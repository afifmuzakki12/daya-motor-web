# -*- coding: utf-8 -*-
from odoo import models, fields

class SparepartCard(models.Model):
    _name = 'sparepart.card'

    card_title = fields.Char("Card Title", required=True)
    card_text = fields.Char("Card Text", required=True)