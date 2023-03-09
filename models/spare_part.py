# -*- coding: utf-8 -*-
from odoo import models, fields


class Sparepart(models.Model):
    _name = 'sparepart.page'

    banner_sparepart = fields.Binary("Banner Sparepart", required=True)
    header_sparepart = fields.Char("Header Sparepart", required=True)
    text_sparepart = fields.Text("Text Sparepart", required=True)