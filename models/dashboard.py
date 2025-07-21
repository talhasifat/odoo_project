from odoo import models, fields, api

class SchoolDashboard(models.TransientModel):
    _name = 'school.dashboard'
    _description = 'School Dashboard'

    total_students = fields.Integer(string='Total Students', readonly=True)
    total_teachers = fields.Integer(string='Total Teachers', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['total_students'] = self.env['school.student'].search_count([])
        res['total_teachers'] = self.env['school.teacher'].search_count([])
        return res
