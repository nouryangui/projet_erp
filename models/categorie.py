# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeCategorie(models.Model):
    _name = 'bibliotheque.categorie'
    _rec_name = 'designation'
    designation=fields.Char('designation')
    description=fields.Text('description')
    livre_id = fields.One2many(comodel_name='bibliotheque.livre', inverse_name='categorie_id')


