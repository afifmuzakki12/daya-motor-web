# -*- coding: utf-8 -*-
from odoo import models, fields

class BookingServiceCard(models.Model):
    _name = 'booking.service.card'

    card_title = fields.Char("Card Title", required=True)
    card_text = fields.Char("Card Text", required=True)