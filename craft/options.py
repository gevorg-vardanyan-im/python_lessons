'''
This module collect the parameters
which should be used to execute API tests.
'''


import os
import sys
import argparse
import datetime
import colorlog
import json


# The following variables were made as argparser parameters help
__help_case = 'Specific case name from the given suite.'
__help_loops = 'How many times a suite should be executed.'
__help_delay = 'Explicit / additional delay in ms between resuests.'
__help_result = 'Directory where all the result files should be stored.'
__help_template = 'HTML template that should be used '\
                  'to generate a report.'
__help_email = 'Necessity of an email notification sending '\
               'after test execution.'
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

# define logger
__logger = colorlog.getLogger()
__logger.setLevel(colorlog.colorlog.logging.DEBUG)
__handler = colorlog.StreamHandler()
__handler.setFormatter(colorlog.ColoredFormatter())
__logger.addHandler(__handler)


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
    group_run.add_argument("--case",
                           type=str,
                           help=__help_case)
    group_run.add_argument("--loops",
                           type=int,
                           help=__help_loops)
    group_run.add_argument("--delay",
                           type=int,
                           help=__help_delay)

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
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir,
                                            'envs',
                                            env_file_path))
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
    # args_dict = args.__dict__
    # get env path
    env = get_env_file_path(args.environment, args.tenant)
    args.environment = env
    check_suite_file_path(args.suite)
    check_report_folder(args.result_folder)
    # print(json.dumps(args, indent=4))
    print(json.dumps(vars(args), indent=4))
    return args


gago = 'GGGGGGGGGG jhdjhfvbl lg kbd g dhfgv '
# print(gago.title())
template = '''newman run \\
            $suite \\
            -e $environment \\
            -r json,xml,html                        --folder get_message \\
            --reporter-html-template $html_template \\
            --reporter-json-export $result_folder \\
            --reporter-xml-export $result_folder \\
            --reporter-html-export $result_folder \\
            --export-collection $result_folder \\
            --verbose'''

template += ' \\' + '\n\t\t\t' + gago
template += ' \\' + '\n\t\t\t' + gago
# print(template)


extra = 'newman run suites/chat_service.postman_collection.json '\
        '-e envs/qa_pivotus.postman_environment.json '\
        '-r htmlextra '\
        '--reporter-htmlextra-export results    '\
        '--reporter-htmlextra-testPaging '\
        '--reporter-htmlextra-title "Engage API testing"'
