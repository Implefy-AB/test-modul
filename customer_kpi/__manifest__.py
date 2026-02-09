{
    'name': 'Kund Nyckeltal (KPI)',
    'version': '19.0.1.0.0',
    'summary': 'Visar försäljningsnyckeltal på kundkortet',
    'description': """
        Lägger till en flik Nyckeltal på kundkortet med:
        - Antal ordrar
        - Totalt ordervärde
        - Snittordervärde
        - Senaste och första order
        - Mest köpta produkt
    """,
    'author': 'Implefy AB',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
