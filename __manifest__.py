# -*- coding: utf-8 -*-
{
    'name': "dimension_based_pricing",

    'summary': "Price Based Dimension Heightand Width in sales and invoice",
    'author': "amzsys",
    'website': "https://www.amzsys.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale','account'],

    'data': [
         'security/ir.model.access.csv',
        'views/sale_order_form.xml',
        'views/sale_report_template.xml',
        'views/invoice_report_template.xml',
        'views/res_config_settings.xml',
        
    ],


}

