'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''


import csv
import random
import base64
import uuid
import datetime
import time
from constants import (QUESTIONS_FILE, ANSWERS_FILE)


def base64_decoder(data):
    '''
        Decodes the base64 question fields to readable string format.
    '''
    for row in data:
        row[4] = base64.b64decode(row[4]).decode()
        row[5] = base64.b64decode(row[5]).decode()
    return data


def base64_decoder_ans(data):
    '''
        Decodes the base64 answer fields to readable string format.
    '''
    for row in data:
        row[4] = base64.b64decode(row[4]).decode()
    return data


def base64_encoder(data):
    '''
        Encodes the question string format to base64.
    '''
    for row in data:
        row[4] = base64.b64encode(bytearray(row[4], encoding='utf-8')).decode()
        row[5] = base64.b64encode(bytearray(row[5], encoding='utf-8')).decode()
    return data


def base64_encoder_ans(data):
    '''
        Encodes the answer string format to base64.
    '''
    for row in data:
        row[4] = base64.b64encode(bytearray(row[4], encoding='utf-8')).decode()
    return data


def time_stamp_decode(data):
    '''
        Decodes the UNIX timestamp to readable string format.
    '''
    for row in data:
            row[1] = str(datetime.datetime.fromtimestamp(float(row[1])).strftime('%Y-%m-%d %H:%M:%S'))
    return data


def time_stamp_encode(data):
    '''
        Encodes the string time format to UNIX timestamp.
    '''
    for row in data:
        row[1] = str(int(datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S').strftime("%s")))
    return data


def open_question_file():
    '''
        Opens the question.csv file,
        reads it content as rows.
    '''
    filepath = QUESTIONS_FILE
    with open(filepath) as workfile:
            row = workfile.readlines()
            data = [item.replace('\n', '').split(';') for item in row]
            data = time_stamp_decode(data)
            data = base64_decoder(data)
            return data


def open_answer_file():
    '''
        Opens the answer.csv file,
        reads it content as rows.
    '''
    filepath = ANSWERS_FILE
    with open(filepath) as workfile:
        row = workfile.readlines()
        data = [item.replace('\n', '').split(';') for item in row]
        data = time_stamp_decode(data)
        data = base64_decoder_ans(data)
        return data


def write_question_to_file(data):
    '''
        Saves question to the specified file.
        Write the data as rows.
    '''
    filepath = QUESTIONS_FILE
    data = base64_encoder(data)
    data = time_stamp_encode(data)
    with open(filepath, 'w') as workfile:
        for item in data:
            row = ';'.join(item)
            workfile.write(row + '\n')


def write_answer_to_file(data):
    '''
        Saves answer to the specified file.
        Write the data as rows.
    '''
    filepath = ANSWERS_FILE
    data = base64_encoder_ans(data)
    data = time_stamp_encode(data)
    with open(filepath, 'w') as workfile:
        for item in data:
            row = ';'.join(item)
            workfile.write(row + '\n')


def data_sorting(data, rev_opt):
    '''
        Sorts the questions by time in descanding order
        Order can be reveresed with rev_opt.
    '''
    data = sorted(data, key=lambda data: data[1], reverse=rev_opt)
    return data



