from odoo import models, fields, api

class SchoolExam(models.Model):
    _name = 'school.exam'
    _description = 'Student Exam'


    name = fields.Char(string='Exam Name', required=True)
    student_id = fields.Many2one('school.student', string='Student', required=True)

    # Related Fields — auto-filled based on selected student
    class_id = fields.Many2one('school.class', string='Class', related='student_id.class_id', store=True, readonly=False)
    section_id = fields.Many2one('school.section', string='Section', related='student_id.section_id', store=True, readonly=False)
    subject_id = fields.Many2one('school.subject', string='Subject', related='student_id.subject_id', store=True, readonly=False)
    institution_id = fields.Many2one('school.institution', string='Institution', related='student_id.institution_id', store=True, readonly=False)

    date = fields.Date(string='Exam Date')
    marks_obtained = fields.Float(string='Marks Obtained')
    total_marks = fields.Float(string='Total Marks', default=100)
    grade = fields.Char(string='Grade')

    @api.onchange('marks_obtained', 'total_marks')
    def _compute_grade(self):
        for rec in self:
            if rec.marks_obtained:
                grade_rec = self.env['school.grade'].search([
                    ('mark_from', '<=', rec.marks_obtained),
                    ('mark_to', '>=', rec.marks_obtained)
                ], limit=1)
                rec.grade = grade_rec.name if grade_rec else 'N/A'
