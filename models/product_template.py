# -*- coding: utf-8 -*-
from odoo import models, fields


class SpesifikasiUnit(models.Model):
    _inherit = 'product.template'
    _name = 'product.template'

    tipe_mesin = fields.Char("Tipe Mesin", size=100)
    tipe_transmisi = fields.Char("Tipe Transmisi", size=100)
    tipe_kopling = fields.Char("Tipe Kopling", size=100)
    tipe_starter = fields.Char("Tipe Starter", size=100)
    diameter_langkah = fields.Char("Diameter X Langkah", size=100)
    volume_langkah = fields.Char("Volume Langkah", size=100)
    pendingin_mesin = fields.Char("Tipe Pendingin", size=100)
    suplai_bahan_bakar = fields.Char("Sistem Suplai Bahan Bakar", size=100)
    perbandingan_kompresi = fields.Char("Perbandingan Kompresi", size=100)
    daya_maksimum = fields.Char("Daya Maksimum", size=100)
    torsi_maksimum = fields.Char("Torsi Maksimum", size=100)
    sistem_pengereman = fields.Char("Sistem Pengereman", size=100)
    kapasitas_tangki = fields.Char("Kapasitas Tangki Bahan Bakar", size=100)
    kapasitas_pelumas = fields.Char("Kapasitas Minyak Pelumas", size=100)
    pola_perpindahan_gigi = fields.Char("Pola Perpindahan Gigi", size=100)

    sistem_pengapian = fields.Char("Sistem Pengapian", size=100)
    tipe_aki = fields.Char("Tipe Baterai/Aki", size=100)
    tipe_busi = fields.Char("Tipe Busi", size=100)
    power_charger = fields.Char("Power Charger", size=100)

    dimensi_plt = fields.Char("Panjang X Lebar X Tinggi", size=100)
    sumbu_roda = fields.Char("Jarak Sumbu Roda", size=100)
    jarak_ke_tanah = fields.Char("Jarak Terendah Ke Tanah", size=100)
    tinggi_tempat_duduk = fields.Char("Tinggi Tempat Duduk", size=100)
    berat_kosong = fields.Char("Berat Kosong", size=100)

    tipe_rangka = fields.Char("Tipe Rangka", size=100)
    ban_depan = fields.Char("Ukuran Ban Depan", size=100)
    ban_belakang = fields.Char("Ukuran Ban Belakang", size=100)
    rem_depan = fields.Char("Sistem Pengereman Depan", size=100)
    rem_belakang = fields.Char("Sistem Pengereman Belakang", size=100)
    suspensi_depan = fields.Char("Tipe Suspensi Depan", size=100)
    suspensi_belakang = fields.Char("Tipe Suspensi Belakang", size=100)

    banner_image = fields.Binary(
        "Banner Image", help="Select image here")

    banner_slider_first = fields.Binary(
        "Banner Slider First", help="Select image here")
    banner_slider_second = fields.Binary(
        "Banner Slider Second", help="Select image here")
    banner_slider_third = fields.Binary(
        "Banner Slider Third", help="Select image here")
    banner_slider_fourth = fields.Binary(
        "Banner Slider Fourth", help="Select image here")

    brochure_file = fields.Binary(
        "Upload Brochure File:", help="Select file here")

    is_ready = fields.Boolean("Is Ready", default=True)

    material_description = fields.Text("Material Description")

    # varian_color_image = fields.Many2many(
    #     'ir.attachment', string="Varian Warna")

    varian_1 = fields.Binary(
        "Varian 1 Upload", help="Select file here")
    varian_2 = fields.Binary(
        "Varian 2 Upload", help="Select file here")
    varian_3 = fields.Binary(
        "Varian 3 Upload", help="Select file here")
    varian_4 = fields.Binary(
        "Varian 4 Upload", help="Select file here")
    varian_5 = fields.Binary(
        "Varian 5 Upload", help="Select file here")
    varian_6 = fields.Binary(
        "Varian 6 Upload", help="Select file here")
    varian_7 = fields.Binary(
        "Varian 7 Upload", help="Select file here")
    varian_8 = fields.Binary(
        "Varian 8 Upload", help="Select file here")
    varian_9 = fields.Binary(
        "Varian 9 Upload", help="Select file here")
    varian_10 = fields.Binary(
        "Varian 10 Upload", help="Select file here")
    varian_11 = fields.Binary(
        "Varian 11 Upload", help="Select file here")
    varian_12 = fields.Binary(
        "Varian 12 Upload", help="Select file here")

    spin_360 = fields.Binary(
        "Spin 360 Upload", help="Select file here")
