# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class Home(http.Controller):
#     @http.route('/', auth='public', website=True)
#     def index(self, **kw):
#         return http.request.render('dym_website.home_page')


class AfterSales(http.Controller):
    @http.route('/after-sales/', auth='public', website=True)
    def aftersales(self, **kw):
        return http.request.render('dym_website.after_sales')


class Apparel(http.Controller):
    @http.route('/after-sales/apparel/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.apparel_page')


class BookingService(http.Controller):
    @http.route('/after-sales/booking-service/', auth='public', website=True)
    def aftersales(self, **kw):
        booking_service_rec = request.env['booking.service'].sudo().search([],limit=1)
        booking_service_card_rec = request.env['booking.service.card'].sudo().search([])
        return http.request.render('dym_website.booking_service', {'booking_service_rec': booking_service_rec, 'booking_service_card_rec': booking_service_card_rec})

class NearestDealer(http.Controller):
    @http.route('/dealer-terdekat/', auth='public', website=True)
    def index(self, **kw):
        slider_first = request.env['add.slider'].sudo().search([],limit=1)
        slider_rec = request.env['add.slider'].sudo().search([],offset=1)
        return http.request.render('dym_website.nearest_dealer', {'slider_first': slider_first, 'slider_rec': slider_rec})

class Pricelist(http.Controller):
    @http.route('/pricelist/', auth='public', website=True)
    def index(self, **kw):
        pricelist_rec = request.env['pricelist.unit'].sudo().search([])
        return http.request.render('dym_website.pricelist_page', {'pricelist_rec': pricelist_rec})

class DealersBranch(http.Controller):
    @http.route('/dealers/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.dealers_page')


class SafetyRiding(http.Controller):
    @http.route('/safety-riding/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.safety_riding')


class EstimatedPrice(http.Controller):
    @http.route('/after-sales/estimated-price/', auth='public', website=True)
    def aftersales(self, **kw):
        pricelist_rec = request.env['pricelist.service'].sudo().search([])
        estimated_page_rec = request.env['estimated.service'].sudo().search([], limit=1)
        return http.request.render('dym_website.estimated_price', {'pricelist_rec': pricelist_rec, 'estimated_page_rec': estimated_page_rec})

class SpareParts(http.Controller):
    @http.route('/after-sales/spare-parts/', auth='public', website=True)
    def aftersales(self, **kw):
        sparepart_page_rec = request.env['sparepart.page'].sudo().search([], limit=1)
        sparepart_card_rec = request.env['sparepart.card'].sudo().search([])
        return http.request.render('dym_website.spare_parts', {'sparepart_page_rec': sparepart_page_rec, 'sparepart_card_rec': sparepart_card_rec})

class ApparelDetail(http.Controller):
    @http.route('/apparel-detail/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.apparel_detail')


class Maps(http.Controller):
    @http.route('/dealer-terdekat/maps/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.maps_page')


class CompanyProfile(http.Controller):
    @http.route('/company-profile/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.profile_page')


class TestRide(http.Controller):
    @http.route('/product-detail/test-ride/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.form_testride_order')


class Test(http.Controller):
    @http.route('/test/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.test_page')


class Test(http.Controller):
    @http.route('/blog-home/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('dym_website.blog_home')


class LiveChatForm(http.Controller):
    @http.route(['/live-chat'], type='http', auth="public", website=True)
    def survey_form_view(self, **post):
        name = post.get('name')
        phone = post.get('phone')
        kota = post.get('kota')
        kecamatan = post.get('kecamatan')
        keterangan = post.get('keterangan')
        if name and phone and kota and kecamatan and keterangan:
            request.env['form.livechat'].sudo().create({
                'name': name,
                'phone': phone,
                'kota': kota,
                'kecamatan': kecamatan,
                'keterangan': keterangan,
            })
            return request.redirect('https://api.whatsapp.com/send/?phone=6281323568585&text=' + name + ' - ' + phone + ' - ' + kota + ' - ' + kecamatan + ' - ' + keterangan)
        return request.render('dym_website.livechat_form_template',
                              {'submitted': post.get('submitted', False)})

class ServiceForm(http.Controller):
    @http.route(['/service-order'], type='http', auth="user", website=True)
    def service_form_view(self, **post):
        name = post.get('name')
        phone = post.get('phone')
        email = post.get('email')
        unit_tipe = post.get('unit_tipe')
        plat_no = post.get('plat_no')
        no_mesin = post.get('no_mesin')
        if name and email and phone and unit_tipe and plat_no and no_mesin:
            request.env['form.service'].sudo().create({
                'name': name,
                'phone': phone,
                'email': email,
                'unit_tipe': unit_tipe,
                'plat_no': plat_no,
                'no_mesin': no_mesin,
            })
            # return request.redirect('/service-order?submitted=1')
            return request.redirect('/')
        return request.render('dym_website.form_service_order',
                              {'submitted': post.get('submitted', False)})


class ApparelForm(http.Controller):
    @http.route(['/apparel-order'], type='http', auth="user", website=True)
    def apparel_form_view(self, **post):
        subtopik = post.get('subtopik')
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        alamat = post.get('alamat')
        provinsi = post.get('provinsi')
        kota = post.get('kota')
        motor_dimiliki = post.get('motor_dimiliki')
        varian_motor = post.get('varian_motor')
        tahun_pembuatan = post.get('tahun_pembuatan')
        jenis_apparel = post.get('jenis_apparel')
        varian_apparel = post.get('varian_apparel')
        rencana_pembelian = post.get('rencana_pembelian')
        tulis_pesan = post.get('tulis_pesan')
        if subtopik and name and email and phone and alamat and provinsi and kota and motor_dimiliki and varian_motor and tahun_pembuatan and jenis_apparel and varian_apparel and rencana_pembelian and tulis_pesan:
            request.env['form.apparel'].sudo().create({
                'subtopik': subtopik,
                'name': name,
                'email': email,
                'phone': phone,
                'alamat': alamat,
                'provinsi': provinsi,
                'kota': kota,
                'motor_dimiliki': motor_dimiliki,
                'varian_motor': varian_motor,
                'tahun_pembuatan': tahun_pembuatan,
                'jenis_apparel': jenis_apparel,
                'varian_apparel': varian_apparel,
                'rencana_pembelian': rencana_pembelian,
                'tulis_pesan': tulis_pesan,
            })
            return request.redirect('/')
            # return request.redirect('/apparel-order?submitted=1')
        return request.render('dym_website.form_apparel_order',
                              {'submitted': post.get('submitted', False)})


class TestRideForm(http.Controller):
    @http.route(['/test-ride'], type='http', auth="user", website=True)
    def testride_form_view(self, **post):
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        alamat = post.get('alamat')
        provinsi = post.get('provinsi')
        kota = post.get('kota')
        motor_dimiliki = post.get('motor_dimiliki')
        varian_motor = post.get('varian_motor')
        tahun_pembuatan = post.get('tahun_pembuatan')
        kategori_unit = post.get('kategori_unit')
        varian_unit = post.get('varian_unit')
        rencana_pembelian = post.get('rencana_pembelian')
        provinsi_dealer = post.get('provinsi_dealer')
        kota_dealer = post.get('kota_dealer')
        nama_dealer = post.get('nama_dealer')
        tulis_pesan = post.get('tulis_pesan')
        if name and email and phone and alamat and provinsi and kota and motor_dimiliki and varian_motor and tahun_pembuatan and kategori_unit and varian_unit and rencana_pembelian and provinsi_dealer and kota_dealer and nama_dealer and tulis_pesan:
            request.env['test.ride.form'].sudo().create({
                'name': name,
                'email': email,
                'phone': phone,
                'alamat': alamat,
                'provinsi': provinsi,
                'kota': kota,
                'motor_dimiliki': motor_dimiliki,
                'varian_motor': varian_motor,
                'tahun_pembuatan': tahun_pembuatan,
                'kategori_unit': kategori_unit,
                'varian_unit': varian_unit,
                'rencana_pembelian': rencana_pembelian,
                'provinsi_dealer': provinsi_dealer,
                'kota_dealer': kota_dealer,
                'nama_dealer': nama_dealer,
                'tulis_pesan': tulis_pesan,
            })
            return request.redirect('/')
        return request.render('dym_website.tesride_form_template',
                              {'submitted': post.get('submitted', False)})


class UnitOrderForm(http.Controller):
    @http.route(['/unit-order'], type='http', auth="user", website=True)
    def service_form_view(self, **post):
        product_category = post.get('product_category')
        product_name = post.get('product_name')
        product_varian = post.get('product_varian')
        otr_price = post.get('otr_price')
        down_payment = post.get('down_payment')
        tenor = post.get('tenor')
        angsuran_per_bulan = post.get('angsuran_per_bulan')
        name = post.get('name')
        email = post.get('email')
        telphone = post.get('telphone')
        gender = post.get('gender')
        kota = post.get('kota')
        kecamatan = post.get('kecamatan')
        kelurahan = post.get('kelurahan')
        if product_category and product_name and product_varian and otr_price and down_payment and tenor and angsuran_per_bulan and name and email and telphone and gender and kota and kecamatan and kelurahan:
            request.env['form.unit.order'].sudo().create({
                'product_category': product_category,
                'product_name': product_name,
                'product_varian': product_varian,
                'otr_price': otr_price,
                'down_payment': down_payment,
                'tenor': tenor,
                'angsuran_per_bulan': angsuran_per_bulan,
                'name': name,
                'email': email,
                'telphone': telphone,
                'gender': gender,
                'kota': kota,
                'kecamatan': kecamatan,
                'kelurahan': kelurahan,
            })
            # return request.redirect('/unit-order?submitted=1')
            return request.redirect('/')
        return request.render('dym_website.survey_unit_order_template',
                              {'submitted': post.get('submitted', False)})
