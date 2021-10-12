#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import json

metadata = json.load(open('/autograder/submission_metadata.json', 'r'))
sid = int(metadata['users'][0]['sid'])
grades = pd.read_csv('/autograder/source/grades.csv', index_col=1).loc[sid]

gs_output = {'tests': []}

def output_postlecture_question_grade(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Post-Lecture Questions', 
		'score': float(grades.loc['Post-Lec Qs']),
		'max_score': 15,
		'output': f"All students are automatically given all Post-Lecture Question points."
		})
	
def output_project_grades(grades, gs_output):
	project_outputs = [f"Your Project 1 score without lateness deductions is {grades.loc['P1 Actual']}.",
					   f"Project 1 used {grades.loc['P1 Slip Days']} slip day(s) and was {grades.loc['P1 Days Late']} day(s) late.",
					   f"Your Project 2 score without lateness deductions is {grades.loc['P2 Actual']}."],
					   f"Project 2 used {grades.loc['P2 Slip Days']} slip day(s) and was {grades.loc['P2 Days Late']} day(s) late."]
	gs_output['tests'].append({
        'name': 'Projects',
        'score': float(grades.loc['P1 Actual'] + grades.loc['P2 Actual']),
        'max_score': 30, #change as more projects are released and graded
        'output': '\n'.join(project _outputs)
    })
	
def output_survey_grades(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Weekly Surveys', 
		'score': float(grades.loc['Surveys Actual']),
		'max_score': 10,
		'output': f"You have submitted {int(grades.loc['Weekly Surveys'])} survey(s)."
		})
		
	
def output_lab_grades(grades, gs_output):
	labs = [f'Lab {i}' for i in range(1, 13 + 1)]
    lab_outputs = [f'Your {lab} score is {grades.loc[lab]}.' for lab in labs]
	lab_outputs = np.append(lab_outputs, [f"Your overall lab score, not counting dropped labs or lateness, is {grades.loc['Lab Actual']}."])
	gs_output['tests'].append({
		'name': 'Labs',
		'score': float(grades.loc['Lab Actual']), 
		'max_score': 25, 
		'output': '\n'.join(lab_outputs)
	})

def output_quest_score(grades, gs_output):
    quest_outputs = [f"Your raw quest score is {grades.loc['Quest Scaled']}."]
    quest_outputs = np.append(quest_outputs, [f"You received {grades.loc['Demo EXC']} extra credit point(s) from completing the quest demo on PL."])
    quest_outputs = np.append(quest_outputs, [f"Your total quest score is {grades.loc['Quest Actual']}."])
    gs_output['tests'].append({
        'name': 'Quest',
        'score': float(grades.loc['Quest Actual']),
        'max_score': 20,
        'output': "\n".join(quest_outputs)
    })

def output_overall_score(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Overall Score',
		'score': floa(grades.loc['Overall Score']),
		'max_score': 500, #do math??? cry?? update as more assignments are being released
		'output': f"Your overall score is {grades.loc['Overall Score']}."
		})


output_overall_score(grades, gs_output)
output_postlecture_question_grade(grades, gs_output)
output_lab_grades(grades, gs_output)
#call all the other ones!

out_path = '/autograder/results/results.json'
with open(out_path, 'w') as f:
    f.write(json.dumps(gs_output))
