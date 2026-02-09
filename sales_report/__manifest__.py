{
    'name': 'Kundanpassade Orderrapporter',
    'version': '19.0.1.0.0',
    'summary': 'Skapa kundanpassade PDF-rapporter för försäljningsordrar',
    'description': """
        Varje kund kan ha en egen rapportprofil med:
        - Logotyp
        - Färgschema
        - Layoutval (Modern, Klassisk, Minimalistisk)
        - Val av vilka fält som visas
    """,
    'author': 'Implefy AB',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_profile_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'report/sale_order_report.xml',
        'report/sale_order_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
