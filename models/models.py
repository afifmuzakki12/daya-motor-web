# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo import models, fields
import psycopg2

hostname = '192.168.3.89'
database = 'DP_ODMPRODS'
username = 'proj80_dymsm'
pwd = 'proj80_dymsm'
port_id = '5444'
conn = None
cur = None

# import psycopg2.extras

try:
    conn = psycopg2.connect(dbname=database, user=username,
                            password=pwd, host=hostname, port=port_id)
    cur = conn.cursor()
    cur.execute('SELECT name FROM dym_city WHERE write_uid = 1;')
    print(cur.fetchall())

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
