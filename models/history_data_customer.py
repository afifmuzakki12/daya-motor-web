# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
# import psycopg2

class HistoryDataCustomer(models.Model):
    _name = 'history.data.customer'
    _description = 'History Data Customer'

    history_id = fields.Integer(string="History ID")
    bpa_code = fields.Char(string="Kode BPA")
    nama_customer = fields.Char(string="Nama Customer")
    no_ktp = fields.Char(string="No KTP")
    jenis_motor = fields.Char(string="Jenis Motor")
    varian_motor = fields.Text(string="Varian Motor")
    tahun_pembuatan = fields.Char(string="Tahun Pembuatan")
    engine_number = fields.Char(string="No Mesin")
    chassis_number = fields.Char(string="No Rangka")
    no_polisi = fields.Char(string="No Polisi")


    @api.model
    def history_data_user(self):
        # conn = psycopg2.connect(
        #     host = "192.168.3.98",
        #     port = "5432",
        #     database = "DP_ODMPRODS",
        #     user = "proj80_dymsm",
        #     password = "proj80_dymsm",
        # )

        # cur = conn.cursor()

        # cur.execute(""" SELECT p.id, p.default_code, p.name as customer, no_ktp, h.name as jenis_motor, pp.name_template||' - '||g.name as variant, lot.tahun as tahun_pembuatan, lot.name as engine_number, lot.chassis_no as chassis_number, lot.no_polisi
        #                     FROM res_partner p
        #                     LEFT JOIN stock_production_lot lot ON lot.customer_id=p.id
        #                     LEFT JOIN product_product pp ON pp.id=lot.product_id
        #                     LEFT JOIN product_template x ON x.id = pp.product_tmpl_id 
        #                     LEFT JOIN product_attribute_value_product_product_rel f ON f.prod_id = lot.product_id 
        #                     LEFT JOIN product_attribute_value g ON g.id = f.att_id 
        #                     LEFT JOIN product_category h ON h.id = x.categ_id 
        #                     WHERE p.name='ADI KARUNIA' AND no_ktp='3674022809820001' """)

        # data = cur.fetchall()
        # print("Query executed successfully.")
        # print("Results: ", data)
        data = [(4160683, 'BPA/1807/215252', 'ADI KARUNIA', '3674022809820001', 'PCX', 'V1J02Q33L0 A/T - WH-WHITE', '2018', 'KF22E1023569', 'KF2210JK023447', 'D 5430 CU')]
        for record in data:
            values = {
                # 'history_id': record[0][0],
                # 'bpa_code': record[0][1],
                # 'nama_customer': record[0][2],
                # 'no_ktp': record[0][3],
                # 'jenis_motor': record[0][4],
                # 'varian_motor': record[0][5],
                # 'tahun_pembuatan': record[0][6],
                # 'engine_number': record[0][7],
                # 'chassis_number': record[0][8],
                # 'no_polisi': record[0][9],
                'history_id': record[0],
                'bpa_code': record[1],
                'nama_customer': record[2],
                'no_ktp': record[3],
                'jenis_motor': record[4],
                'varian_motor': record[5],
                'tahun_pembuatan': record[6],
                'engine_number': record[7],
                'chassis_number': record[8],
                'no_polisi': record[9],
            }
            resource = self.env['history.data.customer'].sudo().create(values)
            # return resource


        # conn.commit()

        # cur.close()
        # conn.close()