'''
This module contains utility functions.
'''


import os
import subprocess
import sys
import re


def read_file(file_name):
    file = None
    data = None
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except IOError as ex:
        print ('Incorrect file name ' + file_name + ' ' + '\n' + str(ex))
    finally:
        if file:
            file.close()
        return data


def write_into_file(file_name, data):
    file = None
    try:
        with open(file_name, 'w') as file:
            data = file.write(data)
    except IOError as ex:
        print ('Incorrect file name ' + file_name + ' ' + '\n' + str(ex))
    finally:
        if file:
            file.close()


def append_into_file(file_name, data):
    file = None
    try:
        with open(file_name, 'a') as file:
            file.write(data)
    except IOError as ex:
        print ('Incorrect file name ' + file_name + ' ' + '\n' + str(ex))
    finally:
        if file:
            file.close()


def run_command(command):
    print('\n', command)
    subprocess.call(command, shell=True)


def set_build_status(aggregate_report_total):
    for key, value in aggregate_report_total.items():
        if key == "error_rate" and value != 0.00:
            error_msg = 'Build step "Execute shell" marked build as failure due to {error_rate}% errors.'
            print(error_msg.format(error_rate=value))
            sys.exit(-1)


def replace_content(content, replaced_dict):
    '''
    This function replaces content of a given string
    by using a given dictionary.
    '''

    for old, new in replaced_dict.items():
        content = content.replace(old, new)
    return content


def extract_text(pattern, content):
    '''
    This function extracts value from given content
    by using given pattern.
    '''

    summary = re.search(pattern, content, re.IGNORECASE)
    found_sting = summary.group(1)
    return found_sting


def change_field_position(given_list, old_index, new_index):
    ''' This function changes a field position in a given list. '''

    desired_value = given_list[old_index]
    given_list.pop(old_index)
    given_list.insert(new_index, desired_value)
    return given_list


def get_env_name(properties):
    '''
    This function cuts & returns environment name from given properties name.
    '''

    env_name = re.search('/(.*)/(.*).properties', properties, re.IGNORECASE)
    groups = env_name.groups()
    return groups[0]
