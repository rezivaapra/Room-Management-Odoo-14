from odoo import models, fields, api
from odoo.exceptions import ValidationError


class pemesananRuangan(models.Model):
    _name = 'roommanagement.pemesananruangan'
    _description = 'roommanagement.pemesananruangan'

    name = fields.Char(string='Nomor Pemesanan', required=True, readonly=True, copy=False, default='New')
    tipe_pemesanan = fields.Selection([
        ('internal', 'Internal'), ('external', 'External')
    ], string='Tipe Pemesanan', required=True)
    ruangan_id = fields.Many2one('roommanagement.masterruangan', string='Ruangan', required=True)
    nama_pemesanan = fields.Char(string='Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft')
    catatan_pemesanan = fields.Text(string='Catatan Pemesan')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            ruangan = self.env['roommanagement.masterruangan'].browse(vals['ruangan_id'])
            tipe_ruangan = ruangan.tipe_ruangan or 'Unknown'
            tanggal_pemesanan = fields.Date.from_string(vals.get('tanggal_pemesanan')).strftime('%d%m%Y')
            sequence = self.env['ir.sequence'].next_by_code('roommanagement.pemesananruangan') or '0000'
            vals['name'] = f"{vals['tipe_pemesanan']}/{tipe_ruangan}/{tanggal_pemesanan}/{sequence}"
        return super(pemesananRuangan, self).create(vals)
    
    _sql_constraints = [
        ('unique_nama_pemesanan', 'unique (nama_pemesanan)', 'Nama Pemesanan sudah digunakan!'),
    ]

    @api.constrains('ruangan_id', 'tanggal_pemesanan')
    def _check_duplicate_booking(self):
        for record in self:
            existing_booking = self.search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)  # Exclude the current record
            ])
            if existing_booking:
                raise ValidationError('Ruangan ini sudah dipesan pada tanggal yang sama!')
            
    def action_proses_pemesanan(self):
        if self.status_pemesanan == 'draft':
            self.status_pemesanan = 'on_going'

    def action_selesaikan_pemesanan(self):
        if self.status_pemesanan == 'on_going':
            self.status_pemesanan = 'done'