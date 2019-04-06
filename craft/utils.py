'''
This module contains utility functions.
'''


import os
import subprocess
import sys
import re
from lxml import etree
from jinja2 import Environment, FileSystemLoader


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


def string_to_xml(string):
    try:
        xml = etree.fromstring(string)
        return xml
    except etree.XMLSyntaxError as ex:
        print ('The provided string is not xml: ' + str(ex))
        return None


def run_command(command):
    print('\n', command)
    subprocess.call(command, shell=True)


def set_build_status(aggregate_report_total):
    for key, value in aggregate_report_total.items():
        if key == "error_rate" and value != 0.00:
            error_msg = 'Build step "Execute shell" marked build as failure due to {error_rate}% errors.'
            print(error_msg.format(error_rate=value))
            sys.exit(-1)


def create_render_template(tmpl_path):
    tmpl_dir = os.path.dirname(tmpl_path)
    tmpl_file = os.path.basename(tmpl_path)
    j2_env = Environment(loader=FileSystemLoader(tmpl_dir), trim_blocks=True)
    return j2_env.get_template(tmpl_file)


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


def get_test_pure_name(test_path):
    '''
    This function cuts & returns only test name from given test path.
    '''

    path_prefix = 'tests/'
    test_name = None
    if path_prefix in test_path:
        exp = path_prefix + '(.*).jmx'
        test = re.search(exp, test_path, re.IGNORECASE)
        test_name = test.groups()[0]
    else:
        exp = '(.*).jmx'
        test = re.search(exp, test_path, re.IGNORECASE)
        test_name = test.groups()[0]
    return test_name


def get_service_name(test_name, test_type):
    '''
    This function cuts & returns service name from given test name.
    '''

    service = None
    service_prefix = {
        "ordinary": '(.*)_service_',
        "benchmarking": 'benchmarking__(.*)_service'
    }

    try:
        service_name = re.search(
            service_prefix[test_type], test_name, re.IGNORECASE)
        groups = service_name.groups()
        service = groups[0]
    except Exception:
        pass
    return service


def get_test_type(test_name):
    '''
    This function detects & returns test type from given test name.
    '''

    test_type = None
    test_type_prefix = {
        'ordinary': '_service__',
        'complex': 'complex__',
        'benchmarking': 'benchmarking__'
    }

    for key, prefix in test_type_prefix.items():
        if prefix in test_name:
            test_type = key
            break
    return test_type


def files_clean_up(env, amount, destination):
    '''
    This function removes redundant/unused files after them usage.
    '''

    data_path = 'data'
    for i in range(1, amount + 1):
        file_path = os.path.join(data_path,
                                 env,
                                 destination + '_' + str(i) + '.csv')
        if os.path.exists(file_path):
            os.remove(file_path)
    return
