from odoo import models, fields, api


class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunte')
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
    @api.constrains('date_debut','date_fin')
    def checkDate(self):
        if self.date_fin<self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')



