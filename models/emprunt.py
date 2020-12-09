from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError


class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunt')
    date_fin = fields.Date('Date Retour')
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')

    def name_get(self):
        result = []
        for emprunt in self:
            name = '[' + emprunt.livre_id.titre + ']' + emprunt.adherent_id.nom + ' ' + emprunt.adherent_id.prenom
            result.append((emprunt.id, name))
        return result
    @api.one
    @api.constrains('adherent_id','livre_id','date_debut', 'date_fin')
    def checknbLivreEmprunté(self):
        if self.date_fin < self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')
        elif self.livre_id.nbExamplaire <= 1:
            raise ValueError("Nb d'examplaire insuffisant ")
        elif self.adherent_id.num_emprunt>3:
            raise ValueError("Nb livre emprunté egale 3")







