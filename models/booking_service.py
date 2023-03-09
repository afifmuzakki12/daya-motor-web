# -*- coding: utf-8 -*-
from odoo import models, fields


class BookingService(models.Model):
    _name = 'booking.service'

    banner_service = fields.Binary("Banner Service", required=True)
    header_service = fields.Char("Header Service", required=True)
    text_service = fields.Text("Text Service", required=True)
    header_card = fields.Text("Header Card", required=True)