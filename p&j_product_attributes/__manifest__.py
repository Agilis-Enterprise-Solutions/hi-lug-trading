# -*- coding: utf-8 -*-
{
    'name': "P&J Product Attributes",
    'summary': """Product Attribute and Labeling of Products specific for P&J""",
    'description': """
        Sales module for P&J:
            - Generates Product Name based only on the Attribute fields of the product
    """,
    'author': "Earvin Clyde Gatdula - Agilis Enterprise Solutions, Inc.",
    'website': "http://www.agilis-solutions.com/",
    'category': 'Sales',
    'version': '0.1',

    'depends': [
        'sale_management', 'product_brand', 'product_attributes'
        ],

    'data': [
        # 'views/product_template.xml',
    ],

    'demo': [

    ],
    "application": False,
    "installable": True,
}
