
from odoo import models, fields, api
class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunt')
    date_fin = fields.Date('Date Retour')
    today = fields.Date.today()
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')
    state = fields.Selection(
        [
        ('lancee',' Emprunté'),
        ('fini','Retourné'),
        ('expiree','Expiré'),
        ],
        string='Statut', readonly=True,default='lancee')

    def action_done(self):
        for rec in self:
            rec.state = 'fini'
            rec.livre_id.nbExamplaire = rec.livre_id.nbExamplaire + 1

    @api.one
    @api.constrains('date_fin','today')
    def change_state_to_expired(self):
        if self.today >= self.date_fin:
            self.state = 'expiree'

    def _create(self, data_list):
        return super()._create(data_list)

    # def _create(self, data_list):
   #      for data in data_list:
   #          print(data)
   #          for x in data :
   #              if(x=="stored"):
   #                  print("clé" + x)
   #                  print(data[x])
   #                  for element in data[x]:
   #                      if element=="livre_id":
   #                         # self.livre_id=data[x][element]
   #                          print(self.livre_id.nbExamplaire)

        #return super()._create(data_list)




    def name_get(self):
        result = []
        for emprunt in self:
            name = '[' + emprunt.livre_id.titre + ']' + emprunt.adherent_id.nom + ' ' + emprunt.adherent_id.prenom
            result.append((emprunt.id, name))
            return result

    @api.one
    @api.constrains('adherent_id', 'livre_id', 'date_debut', 'date_fin')
    def checknbLivreEmprunté(self):
        if self.date_fin < self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')
        elif self.livre_id.nbExamplaire <= 1:
            raise ValueError("Nb d'examplaire insuffisant ")
        elif self.adherent_id.num_emprunt > 3:
            raise ValueError("Nb livre emprunté egale 3")
