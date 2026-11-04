{
    'name': 'Sale Order Line Internal Note',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Per-line internal notes on Sale & Purchase orders — invisible on customer PDF, toggleable column in list view.',
    'description': """
Sale Order Line Internal Note for Odoo 19 (Free / LGPL-3)
==========================================================
- Add an "Internal Note" field to every Sale Order line
- Add an "Internal Note" field to every Purchase Order line
- Notes are 100% hidden from customer-facing PDF reports (quotation, order, invoice)
- Toggleable column in the list view — show or hide without leaving the screen
- Zero configuration — install and start writing notes immediately
    """,
    'author': 'SunMesa Labs',
    'website': 'https://odoo.sunmesalabs.com',
    'support': 'randy@sunmesalabs.com',
    'license': 'LGPL-3',
    'depends': ['sale_management', 'purchase'],
    'data': [
        'views/sale-order-line-views.xml',
        'views/purchase-order-line-views.xml',
    ],
    'demo': [
        'demo/demo-data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/cover.gif', 'static/description/banner.gif'],
}
