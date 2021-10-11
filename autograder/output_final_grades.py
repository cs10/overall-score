#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import json

metadata = json.load(open('/autograder/submission_metadata.json', 'r'))
sid = int(metadata['users'][0]['sid'])
grades = pd.read_csv('autograder/src/grades.csv', index_col=2).loc[sid] 


gs_output = {'tests': []}

def output_postlecture_question_grade(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Post-Lecture Questions', 
		'score': float(grades.loc['Post-Lec Qs']),
		'max_score': 15,
		'output': f"All students are automatically given all Post-Lecture Question points."
		})


def output_overall_score(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Overall Score',
		'score': 0,
		'max_score': 0,
		'output': f"Your overall score is {grades.loc['Overall']}."
		})


output_overall_score(grades, gs_output)
output_postlecture_question_grade(grades, gs_output)

#copied directly, idk what's happening here
out_path = '/autograder/results/results.json'
with open(out_path, 'w') as f:
    f.write(json.dumps(gs_output))
