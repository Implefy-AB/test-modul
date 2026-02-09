{
    'name': 'Test Modul - Cloudpepper Order',
    'version': '19.0.1.1.0',
    'summary': 'Integration med Cloudpepper för orderhantering',
    'description': """
        Modul för att koppla Odoo-ordrar till Cloudpepper.
        - Synkronisera ordrar med Cloudpepper
        - Spåra orderstatus
    """,
    'author': 'juliabengtsson00',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/cloudpepper_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
