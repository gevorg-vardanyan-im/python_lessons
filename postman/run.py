#!/usr/bin/python

import os
from craft.options import get_args
from craft.newman import Newman
# from harness.jmeter import JMeter
# from harness.utils import set_build_status
# from harness.report import Report
# from harness.send_email import EmailSender


def main():

    print(os.path.dirname(os.path.realpath(__file__)))
    args = get_args()
    args.root_dir = os.path.dirname(os.path.abspath(__file__))

    newman = Newman(args)
    newman.run()

    # report = Report(args, jmeter)
    # aggregate_report_total = report.create_html()

    # short_report = report.get_short_report()
    # email_sender = EmailSender(short_report)
    # email_sender.send_email_if_needed()

    # set_build_status(aggregate_report_total)
    # sys.exit(-1)


main()
