# -*- coding: utf-8 -*-
from odoo import models, fields


class FormLivechat(models.Model):
    _name = 'form.livechat'

    name = fields.Char("Nama", size=100)
    phone = fields.Char("No Telepon", size=100)
    kota = fields.Char("Kota / Kabupaten")
    kecamatan = fields.Char("Kecamatan")
    keterangan = fields.Char("Keterangan")
    time_stamp = fields.Datetime('Timestamp', required=False,
                                 readonly=False, select=True, default=lambda self: fields.datetime.now())