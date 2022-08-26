# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': '',
    'author': 'odoo15',
    'summary': 'Hospital management System',
    'description': """Hospital management System""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'sequence': -99,
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {}

}
