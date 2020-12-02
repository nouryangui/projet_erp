# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeCategorie(models.Model):
    _name = 'bibliotheque.categorie'
    designation=fields.Char('designation')
    description=fields.Text('description')

