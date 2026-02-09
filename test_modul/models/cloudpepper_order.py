from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cloudpepper_order_id = fields.Char(string='Cloudpepper Order-ID', index=True)
    cloudpepper_status = fields.Selection([
        ('draft', 'Utkast'),
        ('pending', 'Väntar'),
        ('synced', 'Synkad'),
        ('error', 'Fel'),
    ], string='Cloudpepper-status', default='draft')
    last_sync_date = fields.Datetime(string='Senaste synk')
