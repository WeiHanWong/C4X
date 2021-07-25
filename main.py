"""
Author: Wong Wei Han
Date: 25/7/2021
"""


import sys
import tkinter
import pandas as pd


class User:
    def __init__(self, group, push_up, sit_up, run):
        self.group = group
        self.push_up = push_up
        self.sit_up = sit_up
        self.run = run
        self.score = 0


class Dataset:
    def __init__(self):
        self.push_up_data = pd.read_csv('Metadata/ippt_pushup.csv')
        self.sit_up_data = pd.read_csv('Metadata/ippt_situp.csv')
        self.run_data = pd.read_csv('Metadata/ippt_run.csv')


def main():
    Dataset
    prompter()
    reflector()


def prompter():
    group = input('What is your age group?')
    push_up = input('What is your max rep for pushup?')
    sit_up = input('What is your max rep for situp?')
    run = input('What is your 2.4 run time?')
    global user
    user = User(group, push_up, sit_up, run)


def reflector():
    pud = Dataset().push_up_data
    sud = Dataset().sit_up_data
    rnd = Dataset().run_data
    query_push_up = pud[pud['Rep'] == int(user.push_up)][str(user.group)].iloc[0]
    query_sit_up = sud[sud['Rep'] == int(user.sit_up)][str(user.group)].iloc[0]
    query_run = rnd[rnd['Time'] == user.run][str(user.group)].iloc[0]
    calculate_score(query_push_up, query_sit_up, query_run)


def calculate_score(query_push_up, query_sit_up, query_run):
    user.score = int(query_push_up) + int(query_sit_up) + int(query_run)


if __name__ == '__main__':
    global user
    main()
    print(user.score)
    sys.exit(0)
