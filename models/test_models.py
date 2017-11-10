# -*- coding: utf-8 -*-
from odoo import models, fields, api

class test_creation_asmt(models.Model):
    _name = 'assessment.test_creation_asmt'

    name = fields.Char()
    description = fields.Text()
    date = fields.Date()
    test_duration = fields.Integer()
    question_type = fields.Selection(
        [
            ('Multiple Choice Single Answer', 1),
            ('Multiple Choice Multiple Answer', 2),
        ]
    )
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain')
    domain = fields.Many2one('assessment.domain_asmt', 'Domain') 

class test_paper_asmt(models.Model):
    _name = 'assessment.test_paper_asmt'

    test_creation = fields.Many2one('assessment.test_creation_asmt')

class rubrics_asmt(models.Model):
    _name = 'assessment.rubric_asmt'

    grade_a = fields.Char()
    grade_b = fields.Char()
    grade_c = fields.Char()
    grade_d = fields.Char()
    grade_e = fields.Char()

    objective = fields.Many2one('assessment.objective_asmt', 'Objective')
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain')
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
