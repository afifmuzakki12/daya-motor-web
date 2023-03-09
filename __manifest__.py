# -*- coding: utf-8 -*-
{
    'name': "DYM Custom Website",

    'summary': """
        Daya Motor Website Custom Module Odoo""",

    'description': """
        This module is Daya Motor Website for B2C purpose
    """,

    'author': "Muhammad Afif Muzakki",
    'website': "http://www.daya-motor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website', 'website_sale', 'website_blog', 'website_sale_wishlist', 'auth_signup'],

    # always loaded
    'data': [
        'views/templates.xml',
        'views/product.xml',
        'views/product_detail.xml',
        'views/product_item.xml',
        'views/apparel.xml',
        'views/apparel_detail.xml',
        'views/spare_parts.xml',
        'views/test.xml',
        'views/group.xml',

        # blog
        'views/blog/blog.xml',
        'views/blog/post_loop.xml',

        #blog home
        'views/blog_home/blog_home.xml',
        'views/blog_home/blog_readability.xml',
        'views/blog_home/blog_top_banner.xml',
        'views/blog_home/blog_cover.xml',
        'views/blog_home/blog_bar_template.xml',
        'views/blog_home/blog_bar_template.xml',
        # 'views/blog_home/blog_extra.xml',

        # page
        'views/page/after_sales.xml',
        # 'views/page/home.xml',
        'views/page/booking_service.xml',
        'views/page/nearest_dealer.xml',
        'views/page/price_list.xml',
        'views/page/estimated_price.xml',
        'views/page/maps.xml',
        'views/page/company_profile.xml',
        'views/page/dealers_branch.xml',
        'views/page/safety_riding.xml',

        # inherit
        'views/inherit/wishlist.xml',
        'views/inherit/header_wishlist.xml',
        'views/inherit/product_add_to_wishlist.xml',
        "views/inherit/header.xml",
        'views/inherit/header_shop.xml',
        'views/inherit/footer.xml',
        # 'views/inherit/portal_pager.xml',
        'views/inherit/simulasi_cicilan.xml',
        'views/inherit/product_carousel.xml',
        'views/inherit/delete_footer.xml',

        #inherit sale
        'views/inherit/sale/address_management.xml',
        'views/inherit/sale/sale_varian.xml',
        'views/inherit/sale/sale_payment.xml',
        'views/inherit/sale/sale_checkout.xml',
        'views/inherit/sale/sale_cart.xml',
        'views/inherit/sale/sale_confirmation.xml',
        'views/inherit/sale/sale_line.xml',
        'views/inherit/sale/sale_right_cart.xml',
        'views/inherit/sale/sale_address_kanban.xml',
        'views/inherit/sale/sale_total.xml',

        #inherit profile
        'views/inherit/profile/profile_portal.xml',
        'views/inherit/profile/profile_layout.xml',
        'views/inherit/profile/profile_contact.xml',
        'views/inherit/profile/profile_form_detail.xml',
        # 'views/inherit/profile/signup.xml',
        'views/inherit/profile/stnk_view.xml',

        # form
        'views/form/apparel_order.xml',
        'views/form/live_chat.xml',
        'views/form/test_ride.xml',
        'views/form/unit_order.xml',
        'views/form/service_order.xml',

        # menu
        'views/menu/menu.xml',
        'views/menu/pricelist_service.xml',
        'views/menu/pricelist_unit.xml',
        'views/menu/product_spesification_template.xml',
        'views/menu/form_livechat.xml',
        'views/menu/form_service.xml',
        'views/menu/form_apparel.xml',
        'views/menu/form_test_ride.xml',
        'views/menu/form_unit_order.xml',
        'views/menu/partner_template.xml',
        'views/menu/add_slider.xml',
        # 'views/menu/users.xml',
        # 'views/menu/partner.xml',
        'views/menu/booking_service_menu.xml',
        'views/menu/sparepart_menu.xml',
        'views/menu/estimated_service_menu.xml',
        'views/menu/booking_service_card.xml',
        'views/menu/sparepart_card.xml',

        #security
        'security/dym.city.csv',
        # 'security/dym.kecamatan.csv',
        # 'security/dym.kelurahan.csv',
        'security/ir.model.access.csv',
    ],

    # loaded css file
    'css': [
        "static/src/css/style.css"
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # "assets": {
    #     "website.assets_frontend": [
    #         "/web/static/lib/bootstrap/css/bootstrap.css",
    #         "/dym_website/static/src/css/style.css",
    #         "http://fonts.googleapis.com/css?family=Roboto",
    #     ]
    # }
}
