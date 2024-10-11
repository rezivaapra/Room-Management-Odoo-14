from odoo import models, fields


class masterRuangan(models.Model):
    _name = 'roommanagement.masterruangan'
    _description = 'roommanagement.masterruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1a', '1A'), ('1b', '1B'), ('1c', '1C'),
        ('2a', '2A'), ('2b', '2B'), ('2c', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Image(string='Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')

    _sql_constraints = [
    ('unique_nama_ruangan', 'unique (name)', 'Nama Ruangan tidak boleh sama!')
    ]