# -*- coding: utf-8 -*-
from odoo import models, fields


class DymKecamatan(models.Model):
    _name = 'dym.kecamatan'

    id = fields.Integer("ID")
    create_uid = fields.Many2one('res.users', 'Created by', index=True, readonly=True)
    code = fields.Char("Code", size=128)
    create_date = fields.Datetime('Created on', index=True, readonly=True)
    name = fields.Char("Name", size=128)
    city_id = fields.Char("City")
    write_uid = fields.Many2one('res.users', 'Last Updated by', index=True, readonly=True)
    write_date = fields.Datetime('Last Updated on', index=True, readonly=True)