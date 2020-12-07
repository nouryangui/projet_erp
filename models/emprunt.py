# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Debut')
    date_fin = fields.Date('Date Fin')
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')




