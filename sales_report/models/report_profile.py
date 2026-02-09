from odoo import models, fields


class ReportProfile(models.Model):
    _name = 'report.profile'
    _description = 'Kundanpassad rapportprofil'

    name = fields.Char(string='Profilnamn', required=True)
    partner_id = fields.Many2one('res.partner', string='Kund', ondelete='cascade')
    logo = fields.Binary(string='Logotyp')
    primary_color = fields.Char(string='Primärfärg', default='#875A7B')
    secondary_color = fields.Char(string='Sekundärfärg', default='#333333')
    layout = fields.Selection([
        ('modern', 'Modern'),
        ('classic', 'Klassisk'),
        ('minimal', 'Minimalistisk'),
    ], string='Layout', default='modern')

    # Visa/dölj fält
    show_delivery_address = fields.Boolean(string='Visa leveransadress', default=True)
    show_discount = fields.Boolean(string='Visa rabatt', default=False)
    show_payment_terms = fields.Boolean(string='Visa betalningsvillkor', default=True)
    show_notes = fields.Boolean(string='Visa anteckningar', default=True)
    show_taxes = fields.Boolean(string='Visa moms', default=True)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    report_profile_id = fields.Many2one('report.profile', string='Rapportprofil')
