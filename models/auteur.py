# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeAuteur(models.Model):
    _name = 'bibliotheque.auteur'
    nom = fields.Char('nom')
    prenom = fields.Char('prenom')
    biographie = fields.Char('bigraphie')

