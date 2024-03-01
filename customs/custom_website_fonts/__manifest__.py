{
    'name': 'Custom Website',
    'version': '1.0.0',
    'category': 'Operations',
    'sequence': 1,
    'summary': 'website for Odoo v13',
    'description': """website for Odoo v13""",
    'author': '',
    'company': '',
    'maintainer': '',
    'website': '',
    'depends': ['base','web_tour', 'website'],
    # 'data': [
    #     'views/assets.xml',
    # ],
    'assets': {
        "web.assets_frontend": [
            "custom_website_fonts/static/src/css/style.css",
            "custom_website_fonts/static/src/*",
        ],
        "web.assets_backend": [
            "custom_website_fonts/static/src/css/style.css",
            "custom_website_fonts/static/src/*",
        ],
        "web.assets_qweb": [
            "custom_website_fonts/static/src/css/style.css",
            "custom_website_fonts/static/src/*",
        ],
        # "web.assets_frontend": [ "custom_website_fonts/static/src/fonts/MICR 012.woff" ],
        # "web.assets_backend": [ "custom_website_fonts/static/src/fonts/MICR 012.woff"]
        # 'web.assets_backend': [
        #     'custom_website_fonts/static/src/css/style.css',
        # ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
