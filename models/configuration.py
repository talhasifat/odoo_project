from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)

class SchoolSection(models.Model):
    _name = 'school.section'
    _description = 'School Section'

    name = fields.Char(string='Section Name', required=True)

class SchoolInstitution(models.Model):
    _name = 'school.institution'
    _description = 'Institution'

    name = fields.Char(string='Institution Name', required=True)
