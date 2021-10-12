#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import json

metadata = json.load(open('/autograder/submission_metadata.json', 'r'))
sid = int(metadata['users'][0]['sid'])
grades = pd.read_csv('/autograder/source/grades.csv', index_col=1).loc[sid]

gs_output = {'tests': []}

def output_postlecture_question_score(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Post-Lecture Questions', 
		'score': float(grades.loc['Post-Lec Qs']),
		'max_score': 15,
		'output': f"All students are automatically given all Post-Lecture Question points."
		})
	
def output_project_scores(grades, gs_output):
	project_outputs = [f"Your Project 1 score without lateness deductions is {grades.loc['P1 Actual']}.",
					   f"Project 1 used {grades.loc['P1 Slip Days']} slip day(s) and was {grades.loc['P1 Days Late']} day(s) late.",
					   f"Your Project 2 score without lateness deductions is {grades.loc['P2 Actual']}."],
					   f"Project 2 used {grades.loc['P2 Slip Days']} slip day(s) and was {grades.loc['P2 Days Late']} day(s) late."]
	gs_output['tests'].append({
        'name': 'Projects',
        'score': float(grades.loc['P1 Actual'] + grades.loc['P2 Actual']),
        'max_score': 225, 
        'output': '\n'.join(project _outputs)
    })
	
def output_survey_scores(grades, gs_output):
	gs_output['tests'].append({
		'name': 'Weekly Surveys', 
		'score': float(grades.loc['Surveys Actual']),
		'max_score': 10,
		'output': f"You have submitted {int(grades.loc['Weekly Surveys'])} survey(s)."
		})
		
	
def output_lab_scores(grades, gs_output):
	labs = [f'Lab {i}' for i in range(1, 18 + 1)]
    lab_outputs = [f'Your {lab} score is {grades.loc[lab]}.' for lab in labs]
	lab_outputs = np.append(lab_outputs, [f"Your overall lab score, not counting dropped labs or lateness, is {grades.loc['Lab Actual']}."])
	gs_output['tests'].append({
		'name': 'Labs',
		'score': float(grades.loc['Lab Actual']), 
		'max_score': 40, 
		'output': '\n'.join(lab_outputs)
	})
	
def output_quiz_scores(grades, gs_output):
	quizzes = [f'Week {i} RQ' for i in [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]] # these are the weeks we have RQs this semester
	quiz_outputs = [f'Your {quiz} score is {grades.loc[quiz]}.' for quiz in quizzes]
	quiz_outputs = np.append(quiz_outputs, [f"Your overall reading quizzes score, not counting dropped quizzes or lateness, is {grades.loc['RQ Actual']}."])
	gs_output['tests'].append({
		'name': 'Reading Quizzes',
		'score': float(grades.loc['RQ Actual'] *1.25), # each rq is worth 1.25 pts
		'max_score': 10, 
		'output': '\n'.join(quiz_outputs)
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
		'max_score': 500, 
		'output': f"Your overall score is {grades.loc['Overall Score']}."
		})


output_overall_score(grades, gs_output)
output_quest_score(grades, gs_output)
output_project_scores(grades, gs_output)
output_lab_scores(grades, gs_output)
output_quiz_scores(grades, gs_output)
output_survey_scores(grades, gs_output)
output_postlecture_question_score(grades, gs_output)

out_path = '/autograder/results/results.json'
with open(out_path, 'w') as f:
    f.write(json.dumps(gs_output))
