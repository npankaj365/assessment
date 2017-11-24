# -*- coding: utf-8 -*-
import logging, random
from odoo import models, fields, api, exceptions
_logger = logging.getLogger(__name__)

class test_creation_asmt(models.Model):
    _name = 'assessment.test_creation_asmt'

    name = fields.Char()
    description = fields.Text()
    date = fields.Date()
    test_duration = fields.Integer()
    question_type = fields.Selection(
        [
            ('mcsa','Multiple Choice Single Answer'),
            ('mcma','Multiple Choice Multiple Answer'),
            ('o','Order'),
            ('fa','Free Answer')
        ], required=True
    )
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', domain="[('subdomain','=',subdomain)]")
    selected_questions_list = []


    @api.multi
    def generate(self):
        question_list = []
        #Get all questions that satisfy the question_type
        lesson = self.env['assessment.lesson_asmt'].search([])
        for objective in lesson.objective:
            for question in objective.question:
                if (question.question_type == self.question_type):
                    question_list.append(question) #Creating Dictionary with Question Statements and Answer Choices

        duration = self.test_duration
        #Generate randomized list
        while(duration > 0):
            gen = int(random.random()*len(question_list))
            selection = question_list[gen]

            if (selection.time_required <= duration):
                self.selected_questions_list.append(selection)
                duration -= selection.time_required
                question_list.remove(selection)

    def clear(self):
        del(self.selected_questions_list[:])

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
    
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', domain="[('subdomain','=',subdomain)]")
    objective = fields.Many2one('assessment.objective_asmt', 'Objective', domain="[('lesson','=',lesson)]")
    