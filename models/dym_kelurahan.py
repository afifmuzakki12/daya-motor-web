# -*- coding: utf-8 -*-
from odoo import models, fields


class DymKelurahan(models.Model):
    _name = 'dym.kelurahan'

    id = fields.Integer("ID")
    create_uid = fields.Many2one('res.users', 'Created by', index=True, readonly=True)
    code = fields.Char("Kode Kelurahan", size=128)
    create_date = fields.Datetime('Created on', index=True, readonly=True)
    name = fields.Char("Name", size=128)
    zip = fields.Char("Zip Code", size=10)
    kecamatan_id = fields.Char("Kecamatan")
    write_uid = fields.Many2one('res.users', 'Last Updated by', index=True, readonly=True)
    write_date = fields.Datetime('Last Updated on', index=True, readonly=True)
