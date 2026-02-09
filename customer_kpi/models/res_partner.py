from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    kpi_order_count = fields.Integer(
        string='Antal ordrar',
        compute='_compute_sale_kpi',
    )
    kpi_total_revenue = fields.Float(
        string='Totalt ordervärde',
        compute='_compute_sale_kpi',
    )
    kpi_average_order = fields.Float(
        string='Snittordervärde',
        compute='_compute_sale_kpi',
    )
    kpi_first_order_date = fields.Date(
        string='Första order',
        compute='_compute_sale_kpi',
    )
    kpi_last_order_date = fields.Date(
        string='Senaste order',
        compute='_compute_sale_kpi',
    )
    kpi_top_product = fields.Char(
        string='Mest köpta produkt',
        compute='_compute_sale_kpi',
    )

    @api.depends('sale_order_ids.state', 'sale_order_ids.amount_total')
    def _compute_sale_kpi(self):
        for partner in self:
            orders = self.env['sale.order'].search([
                ('partner_id', '=', partner.id),
                ('state', '=', 'sale'),
            ])

            partner.kpi_order_count = len(orders)
            partner.kpi_total_revenue = sum(orders.mapped('amount_total'))
            partner.kpi_average_order = (
                partner.kpi_total_revenue / partner.kpi_order_count
                if partner.kpi_order_count > 0 else 0.0
            )

            if orders:
                dates = orders.mapped('date_order')
                partner.kpi_first_order_date = min(dates).date()
                partner.kpi_last_order_date = max(dates).date()
            else:
                partner.kpi_first_order_date = False
                partner.kpi_last_order_date = False

            # Hitta mest köpta produkt
            if orders:
                order_lines = self.env['sale.order.line'].search([
                    ('order_id', 'in', orders.ids),
                    ('product_id', '!=', False),
                ])
                if order_lines:
                    product_qty = {}
                    for line in order_lines:
                        pid = line.product_id.id
                        product_qty[pid] = product_qty.get(pid, 0) + line.product_uom_qty
                    top_product_id = max(product_qty, key=product_qty.get)
                    top_product = self.env['product.product'].browse(top_product_id)
                    partner.kpi_top_product = top_product.name
                else:
                    partner.kpi_top_product = False
            else:
                partner.kpi_top_product = False
