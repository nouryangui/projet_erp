# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeAdherent(models.Model):
    _name = 'bibliotheque.adherent'
    cin = fields.Integer('cin')
    nom=fields.Char('nom')
    prenom=fields.Char('prenom')

