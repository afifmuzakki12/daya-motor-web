# -*- coding: utf-8 -*-
from odoo import models, fields


class FormUnitOrder(models.Model):
    _name = 'form.unit.order'

    time_stamp = fields.Datetime('Timestamp', required=False,
                                 readonly=False, select=True, default=lambda self: fields.datetime.now())
    product_category = fields.Char("Kategori Produk")
    product_name = fields.Char("Nama Produk")
    product_varian = fields.Char("Varian Produk")
    otr_price = fields.Char("Harga OTR")
    down_payment = fields.Char("Down Payment")
    tenor = fields.Char("Jangka Waktu")
    angsuran_per_bulan = fields.Char("Angsuran Per Bulan")
    name = fields.Char("Nama")
    email = fields.Char("Alamat Email")
    telphone = fields.Char("No Telphone")
    gender = fields.Char("Gender")
    kota = fields.Char("Kota")
    kecamatan = fields.Char("Kecamatan")
    kelurahan = fields.Char("Kelurahan")
    # tulis_pesan = fields.Text("Tulis Pesan")
