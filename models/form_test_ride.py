# -*- coding: utf-8 -*-
from odoo import models, fields


class FormTestRide(models.Model):
    _name = 'test.ride.form'

    time_stamp = fields.Datetime('Timestamp', required=False,
                                 readonly=False, select=True, default=lambda self: fields.datetime.now())
    name = fields.Char("Nama")
    email = fields.Char("Email")
    phone = fields.Char("No Telepon")
    alamat = fields.Char("Alamat")
    provinsi = fields.Char("Provinsi")
    kota = fields.Char("Kota")
    motor_dimiliki = fields.Char("Motor yang Dimiliki")
    varian_motor = fields.Char("Varian Motor")
    tahun_pembuatan = fields.Char("Tahun Pembuatan")
    kategori_unit = fields.Char("Kategori Motor Diminati")
    varian_unit = fields.Char("Varian Motor Diminati")
    rencana_pembelian = fields.Char("Rencana Pembelian")
    provinsi_dealer = fields.Char("Provinsi Dealer")
    kota_dealer = fields.Char("Kota Dealer")
    nama_dealer = fields.Char("Nama Dealer")
    tulis_pesan = fields.Char("Tulis Pesan")
