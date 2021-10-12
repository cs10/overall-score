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
	
# def output_project_grades(grades, gs_output):
# 	project_outputs = [f"Your Project 1 score is {grades.loc['P1 Actual']}.",
# 					   f"Your Project 2 score is {grades.loc['Project 2']}.", 
# 					   f"Your Project 2 score is {grades.loc['Project 2']}."]
	
# 	    project_outputs = [f"Your Project 1 score is {grades.loc['Project 1']}.",                        
# 		f"Your Project 2 score is {grades.loc['Project 2']}.",                        
# 		f"Your overall project score is {np.mean([grades.loc['Project 1'], grades.loc['Project 2']])}."]

# def output_survey_grades(grades, gs_output):
# 	# dropped surveys
# 	gs_output['tests'].append({
# 		'name': 'Weekly Surveys', 
# 		'score': float(grades.loc['Surveys Actual']),
# 		'max_score': 10,
# 		'output': f"You have submitted {int(grades.loc['Surveys Actual'])} survey(s)."
# 		})
		
	
def output_lab_grades(grades, gs_output):
	# potentially do per-lab outputs if time
	# dropped labs
	gs_output['tests'].append({
		'name': 'Labs',
		'score': float((grades.loc['Labs'] + 1) * 2), # to account for no lab1 checkoff
		'max_score': 40,
		'output': f"You have submitted {int(1 + grades.loc['Labs'])} lab(s)." # to account for  no lab1 checkoff
	})


def output_overall_score(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Overall Score',
		'score': 0,
		'max_score': 0,
		'output': f"Your overall score is {grades.loc['Overall Score']}."
		})


output_overall_score(grades, gs_output)
output_postlecture_question_grade(grades, gs_output)
output_lab_grades(grades, gs_output)

out_path = '/autograder/results/results.json'
with open(out_path, 'w') as f:
    f.write(json.dumps(gs_output))
