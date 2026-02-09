from odoo import models, fields, api


class CloudpepperOrder(models.Model):
    _name = 'cloudpepper.order'
    _description = 'Cloudpepper Order'
    _order = 'create_date desc'

    name = fields.Char(string='Referens', required=True, copy=False, default='Ny')
    cloudpepper_order_id = fields.Char(string='Cloudpepper Order-ID', index=True)
    sale_order_id = fields.Many2one('sale.order', string='Försäljningsorder')
    cloudpepper_status = fields.Selection([
        ('draft', 'Utkast'),
        ('pending', 'Väntar'),
        ('synced', 'Synkad'),
        ('error', 'Fel'),
    ], string='Synkstatus', default='draft')
    last_sync_date = fields.Datetime(string='Senaste synk')
    notes = fields.Text(string='Anteckningar')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Ny') == 'Ny':
                vals['name'] = self.env['ir.sequence'].next_by_code('cloudpepper.order') or 'Ny'
        return super().create(vals_list)
