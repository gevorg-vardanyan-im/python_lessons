'''
This module collect the parameters
which should be used to execute API tests.
'''


import os
import sys
import re
import argparse
import datetime
import colorlog
import json
from craft.utils import read_file


# The following variables were made as argparser parameters help
__help_case = 'Specific case name from the given suite.\n' \
              'Use whitespace to separate multiple cases\' names.'
__help_loops = 'How many times a suite should be executed.'
__help_delay = 'Explicit / additional delay between requests ' \
               '(in milliseconds).'
__help_data = 'Data file path which should be used ' \
              'as an input for suite execution.'
__help_result = 'Directory where all the result files should be stored.'
__help_template = 'HTML template that should be used '\
                  'to generate a report.'
__help_email = 'Necessity of an email notification sending '\
               'after test execution.'
__help_title = 'Name of the html report page.'
# initial values
__report_title = 'Engage API testing report'
__envs = ['perf',
          'perf2',
          'qa',
          'qa2',
          'qa3',
          'sandbox'
          ]
__tenants = ['pivotus',
             'cua',
             'hills',
             'umpqua',
             'sns'
             ]
# specific cases' names will be known when the suite is known
__cases = []

# define logger
__logger = colorlog.getLogger()
__logger.setLevel(colorlog.colorlog.logging.DEBUG)
__handler = colorlog.StreamHandler()
__handler.setFormatter(colorlog.ColoredFormatter())
__logger.addHandler(__handler)


def detect_cases():

    args = sys.argv[1:]
    regex = re.compile(r'.(?<=suites/).*(?=.postman_collection.json)')
    suite = ''
    for arg in args:
        if regex.search(arg):
            suite = arg
            break
    if suite:
        suite_s = read_file(suite)
        json_dict = json.loads(suite_s)
        items = json_dict['item']
        for item in items:
            __cases.append(item['name'])
    else:
        msg = 'No suite file was given.'
        __logger.info(msg)
        return

    cases_s = "\n\t\t".join(__cases)
    cases_info = '\n\tAvailable cases are the following:'\
                 '\n\t\t{}'.format(cases_s)
    __logger.info(cases_info)


def parse_args():
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description="Execute API tests.",
                                     formatter_class=formatter)

    # mandatory arguments
    parser.add_argument("suite",
                        help="Suite that should be executed.")
    parser.add_argument("environment",
                        choices=__envs,
                        help="Environment name.")
    parser.add_argument("tenant",
                        choices=__tenants,
                        help="Tenant name.")

    group_run = parser.add_argument_group("Run parameters")
    detect_cases()
    group_run.add_argument("--case",
                           default=[],
                           nargs='*',
                           choices=__cases,
                           type=str,
                           help=__help_case)
    group_run.add_argument("--loops",
                           type=int,
                           help=__help_loops)
    group_run.add_argument("--delay",
                           type=int,
                           help=__help_delay)
    group_run.add_argument("--data",
                           type=str,
                           help=__help_data)

    group_report = parser.add_argument_group("Report parameters")
    result_folder = os.path.join("results",
                                 datetime.datetime.now().
                                 strftime("%Y_%m_%d__%H_%M_%S"))
    template_path = os.path.join('templates',
                                 'default_template_v_1.hbs')
    group_report.add_argument("--html_template",
                              type=str,
                              default=template_path,
                              help=__help_template)
    group_report.add_argument("--result_folder",
                              default=result_folder,
                              help=__help_result)
    group_report.add_argument("--report_title",
                              default=__report_title,
                              help=__help_title)

    group_email = parser.add_argument_group("Email notification parameters")
    group_email.add_argument("--send_email",
                             type=str,
                             default="yes",
                             help=__help_email)

    args = parser.parse_args()
    return args


def get_env_file_path(env, tenant):
    env_file_path = '{env}_{tenant}.postman_environment.json'.format(
        env=env, tenant=tenant)
    env_path = os.path.join('envs', env_file_path)

    if os.path.isfile(env_path):
        return env_path
    else:
        error_message = 'There is no env file under \'./envs\' folder ' \
                        'for \'{env} env and '\
                        '\'{tenant}\' tenant values.'.format(
                            env=env, tenant=tenant)
        __logger.exception(error_message)
        sys.exit(0)


def check_suite_file_path(suite):
    suite_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                              os.pardir,
                                              suite))
    if not os.path.isfile(suite_path):
        error_message = 'There is no suite file under given folder '
        __logger.exception(error_message)
        return '___suite file error___'


def check_report_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def get_args():
    args = parse_args()
    args.root_dir = os.path.dirname(os.path.abspath(__file__))
    # get env path
    env = get_env_file_path(args.environment, args.tenant)
    args.environment = env
    check_suite_file_path(args.suite)
    check_report_folder(args.result_folder)
    return args
