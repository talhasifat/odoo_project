from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char(string='Subject Name', required=True)

class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'Grade Configuration'
    _order = 'mark_from ASC'

    name = fields.Char(string='Grade', required=True)  # e.g., A, B, C
    mark_from = fields.Integer(string='Mark From', required=True)
    mark_to = fields.Integer(string='Mark To', required=True)

    @api.constrains('mark_from', 'mark_to')
    def _check_mark_range(self):
        for rec in self:
            if rec.mark_from > rec.mark_to:
                raise ValidationError('Mark From cannot be greater than Mark To.')

    def get_grade_from_mark(self, mark):
        """Helper to get grade name from a mark."""
        grade = self.search([
            ('mark_from', '<=', mark),
            ('mark_to', '>=', mark)
        ], limit=1)
        return grade.name if grade else 'N/A'