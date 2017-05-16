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






