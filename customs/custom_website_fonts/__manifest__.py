{
    'name': 'Custom Website',
    'description': 'Custom theme for adding custom fonts',
    'category': 'Theme/Website',
    'version': '16.0.0',
    'author': 'Jort de Vreeze',
    'license': 'AGPL-3',
    'depends': ['website'],
    # 'data': [
    #     'views/assets.xml',
    # ],
    'assets': {
		'web._assets_primary_variables': [
			'custom_website_fonts/static/src/scss/primary_variables.scss',
		],
	},
    # 'assets': {
    #     "web.assets_frontend": [
    #         "custom_website_fonts/static/src/css/style.css",
    #         "custom_website_fonts/static/src/*",
    #     ],
    #     "web.assets_backend": [
    #         "custom_website_fonts/static/src/css/style.css",
    #         "custom_website_fonts/static/src/*",
    #     ],
    #     "web.assets_qweb": [
    #         "custom_website_fonts/static/src/css/style.css",
    #         "custom_website_fonts/static/src/*",
    #     ],
    #     # "web.assets_frontend": [ "custom_website_fonts/static/src/fonts/MICR 012.woff" ],
    #     # "web.assets_backend": [ "custom_website_fonts/static/src/fonts/MICR 012.woff"]
    #     # 'web.assets_backend': [
    #     #     'custom_website_fonts/static/src/css/style.css',
    #     # ],
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
}
