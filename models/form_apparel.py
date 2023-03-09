# -*- coding: utf-8 -*-
from odoo import models, fields


class FormApparel(models.Model):
    _name = 'form.apparel'

    time_stamp = fields.Datetime('Timestamp', required=False,
                                 readonly=False, select=True, default=lambda self: fields.datetime.now())
    subtopik = fields.Char("Subtopik", size=100)
    name = fields.Char("Nama", size=100)
    email = fields.Char("Email", size=100)
    phone = fields.Char("No Telepon", size=100)
    alamat = fields.Char("Alamat", size=100)
    provinsi = fields.Char("Provinsi", size=100)
    kota = fields.Char("Kota", size=100)
    motor_dimiliki = fields.Char("Motor yang Dimiliki", size=100)
    varian_motor = fields.Char("Varian Motor", size=100)
    tahun_pembuatan = fields.Char("Tahun Pembuatan", size=100)
    jenis_apparel = fields.Char("Jenis Apparel", size=100)
    varian_apparel = fields.Char("Varian Apparel", size=100)
    rencana_pembelian = fields.Char("Rencana Pembelian", size=100)
    tulis_pesan = fields.Char("Tulis Pesan", size=100)
