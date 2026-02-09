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
    order_line_ids = fields.One2many('cloudpepper.order.line', 'order_id', string='Orderrader')
    amount_total = fields.Float(string='Totalt', compute='_compute_amount_total', store=True)
    notes = fields.Text(string='Anteckningar')

    @api.depends('order_line_ids.subtotal')
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(order.order_line_ids.mapped('subtotal'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Ny') == 'Ny':
                vals['name'] = self.env['ir.sequence'].next_by_code('cloudpepper.order') or 'Ny'
        return super().create(vals_list)


class CloudpepperOrderLine(models.Model):
    _name = 'cloudpepper.order.line'
    _description = 'Cloudpepper Orderrad'

    order_id = fields.Many2one('cloudpepper.order', string='Order', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Produkt', required=True)
    quantity = fields.Float(string='Antal', default=1.0)
    price_unit = fields.Float(string='Enhetspris')
    subtotal = fields.Float(string='Delsumma', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.price_unit = self.product_id.lst_price
