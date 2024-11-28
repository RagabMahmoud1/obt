# -*- coding: utf-8 -*-
{
    'name': "ZK Biometric Integration",

    'summary': """
    ZK Machines Biometric Integrations
        """,
    'description': """
    """,
    'author': "CDS Solutions SRL,Ramadan Khalil",
    'website': "www.cdsegypt.com",
    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
    ],
    'price': 69,
    'currency': 'USD',
    'version': '16.1.0',
    'images': ['static/description/banner.png'],
    'category': 'hr',
    'depends': ['base', 'hr', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'data/data.xml',
        'views/hr_attendance.xml',
        'views/biometric_view.xml',
        'wizard/schedule_wizard.xml',
    ],
    'license': 'OPL-1',

}
