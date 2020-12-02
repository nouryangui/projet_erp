# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeEditeur(models.Model):
    _name = 'bibliotheque.editeur'
    nom = fields.Char('nom')
    pays = fields.Char('pays')
    adresse = fields.Char('adresse')
    telephone=fields.Integer('telephone')


