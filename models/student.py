from docutils.nodes import image

from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Information'

    # image = fields.Image(string='Profile Image', max_width=128, max_height=128)
    image = fields.Binary(string='Profile Image')

    name = fields.Char(string='Full Name', required=True)
    roll_number = fields.Char(string='Roll Number', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    class_id = fields.Many2one('school.class', string='Class', required=True)
    section_id = fields.Many2one('school.section', string='Section', required=True)
    institution_id = fields.Many2one('school.institution', string='Institution', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    address = fields.Text(string='Address')

    active = fields.Boolean(string='Active', default=True)
