# -*- coding: utf-8 -*-
from odoo import models, fields

class AddSlider(models.Model):
    _name = 'add.slider'

    banner_slider = fields.Binary(
        "Banner Slider", help="Select image here", required=True)