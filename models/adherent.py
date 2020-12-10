from odoo import models, fields, api
class BibliothequeAdherent(models.Model):
    _name = 'bibliotheque.adherent'
    _inherit = 'mail.thread'
    cin = fields.Integer('cin')
    nom=fields.Char('nom')
    prenom=fields.Char('prenom')
    emprunt_id = fields.One2many(comodel_name='bibliotheque.emprunt', inverse_name='adherent_id')
    num_emprunt = fields.Integer("nombre des livres  emprunts", compute="comp_emprunt")
    image = fields.Binary(string= "image")


    @api.multi
    def name_get(self):
        result = []
        for adhrent in self:
            name = ''
            if adhrent.nom:
                name += adhrent.nom  + ' ' + adhrent.prenom
            result.append((adhrent.id, name))
        return result

    def comp_emprunt(self):
        self.num_emprunt  = len(self.emprunt_id)