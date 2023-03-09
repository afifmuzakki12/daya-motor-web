# -*- coding: utf-8 -*-
from odoo import models, fields


class FormLivechat(models.Model):
    _name = 'form.service'

    time_stamp = fields.Datetime('Timestamp', required=False,
                                 readonly=False, select=True, default=lambda self: fields.datetime.now())
    name = fields.Char("Nama", size=100)
    phone = fields.Char("Phone", size=100)
    email = fields.Char("Email")
    unit_tipe = fields.Char("Jenis Motor")
    plat_no = fields.Char("Plat Nomor")
    no_mesin = fields.Char("Nomor Mesin")
