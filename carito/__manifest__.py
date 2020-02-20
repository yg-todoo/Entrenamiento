# -*- coding: utf-8 -*-
{
    'name': "carito",

    'summary': """
        Esta es una prueba""",

    'description': """
       Este módulo se crea para aprender a utilizar los conceptos básicos de Odoo
    """,

    'author': "yenny granados",
    'website': "http://www.yenny.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
       # 'demo/demo.xml',
    ],#
}
