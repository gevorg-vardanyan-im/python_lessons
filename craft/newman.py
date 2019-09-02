from craft.utils import run_command
from string import Template
from craft.testrail import *
import colorlog


class Newman:
    def __init__(self, args):
        self.args = args
        # define logger
        self.__logger = colorlog.getLogger()
        self.__logger.setLevel(colorlog.colorlog.logging.DEBUG)
        __handler = colorlog.StreamHandler()
        __handler.setFormatter(colorlog.ColoredFormatter())
        self.__logger.addHandler(__handler)
        # define optional arguments
        self.optional_args = {'case': 'folder',
                              'data': 'iteration-data',
                              'delay': 'delay-request',
                              'loops': 'iteration-count'
                              }

    def __check_args(self):
        '''
        This function checks for additional arguments.
        '''

        args = vars(self.args)
        # accodance between usual and newman's terms
        additional_options = ''
        options_tmpl = ' \\' + '\n\t\t --{val} ${key}'
        case_tmpl = ' \\' + '\n\t\t --{val} {case}'
        for key, val in self.optional_args.items():
            if key in args:
                if args[key]:
                    if key == 'case':
                        for case in args[key]:
                            additional_options += case_tmpl.format(val=val,
                                                                   case=case)
                        # self.args.case = opt
                    else:
                        additional_options += options_tmpl.format(val=val,
                                                                  key=key)
            else:
                warn = 'Args dictionary does not contain '\
                       '\'{}\' argument.'.format(key)
                self.__logger.warning(warn)
        return additional_options

    def run(self):
        '''
        This function initiates the newman execution
        with the given arguments.
        '''

        args_dict = self.args.__dict__
        additional_args = self.__check_args()
        main_template = '''newman run \\
            $suite \\
            -e $environment \\
            -r cli,htmlextra \\
            --reporter-htmlextra-export $result_folder \\
            --export-collection $result_folder \\
            --export-environment $result_folder \\
            --reporter-htmlextra-testPaging \\
            --reporter-htmlextra-title '$report_title' \\
            --color on \\
            --verbose'''
        full_template = main_template + additional_args

        command = Template(full_template).substitute(args_dict)
        # run_command(command)
        print(command)
