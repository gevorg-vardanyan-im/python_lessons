import os
import datetime
import time
import re
import colorlog
from craft.utils import run_command
from string import Template


class Newman:
    def __init__(self, args):
        self.args = args
        # define logger
        self.logger = colorlog.getLogger()
        self.logger.setLevel(colorlog.colorlog.logging.DEBUG)
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter())
        self.logger.addHandler(handler)

    def prepare(self):
        args = vars(self.args)
        optional_args = ['case',
                         'delay',
                         'loops'
                         ]
        for option in optional_args:
            if option in args:
                if args[option]:
                    optional = ' \\' + '\n\t\t\t' + str(args[option])
                    print(optional)
                print(option, args[option])

        # prepare env file location
        # sute location
        # report template location

        # self.start_time = datetime.datetime.now()
        # if not os.path.exists(self.args.results):
        #     os.makedirs(self.args.results)
        # if self.args.delay != 0:
        #     # Delay by minute before testing
        #     print WAITING_START_MESSAGE.format(str(self.args.delay))
        #     time.sleep(60 * float(self.args.delay))
        #     print WAITING_END_MESSAGE
        return

    def run(self):
        self.prepare()

        args_dict = self.args.__dict__
        template = '''newman run \\
            $suite \\
            -e $environment \\
            -r cli,htmlextra \\
            --reporter-htmlextra-export $result_folder \\
            --export-collection $result_folder \\
            --reporter-htmlextra-testPaging \\
            --reporter-htmlextra-title 'Engage API testing report' \\
            --color on \\
            --verbose'''

# json-summary --reporter-json-summary-export $result_folder \\
# -- newman-reporter-xml-export $result_folder \\
        command = Template(template).substitute(args_dict)
        run_command(command)
