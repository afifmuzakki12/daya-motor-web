# -*- coding: utf-8 -*-
from odoo import models, fields


class EstimatedService(models.Model):
    _name = 'estimated.service'

    banner_estimated = fields.Binary("Banner Estimated Service", required=True)
    header_estimated = fields.Char("Header Estimated Service", required=True)
    text_estimated = fields.Text("Text Estimated Service", required=True)
    content_estimated = fields.Text("Content Estimated Service", required=True)