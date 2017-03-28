# -*- coding: utf-8 -*-
{
    'name': "Show Forecasted Quantity in Kanban View",

    'summary': """
        Odoo 10 does not show Forecasted Quantity in Kanban View. 
		This module add the functionality to show Forecasted Quantity in Kanban View under Product menu in Odoo 10
	""",

    'description': """
        Odoo 10 does not show Forecasted Quantity in Kanban View. 
		This module add the functionality to show Forecasted Quantity in Kanban View under Product menu in Odoo 10

		Developed by: Beta Uliansyah <beta@tarkiz.biz>

		Please feel free to contact to share what you think about this modul!
    """,

    'author': "Tarkiz",
    'website': "http://tarkiz.biz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock'],


    # always loaded
    'data': [
        'forecasted_in_product_view_kanban.xml',
    ],
}
