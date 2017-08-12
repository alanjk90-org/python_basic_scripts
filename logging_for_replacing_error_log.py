#!/usr/bin/env python

from cStringIO import StringIO
import re

vhost_start = re.compile(r'(<VirtualHost\s+)(.*?:\d+)>')
vhost_end = re.compile(r'</VirtualHost>')
error_log_re = re.compile(r'(ErrorLog\s+)(\S+)')
#er = error_log.search('ErrorLog /var/log/apache2/error2.log')


def change_error_log(file, vhost, now_doc_root):
    conf_file = StringIO(logfile)
    inhost = False
    cur_vhost = None
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            cur_vhost = vhost_start_match.groups()[1]
            inhost = True
        if inhost and (cur_vhost == vhost):
            errlog_match = error_log_re.search(line)
            if errlog_match:
                sub_line = error_log_re.sub(r'\1%s' % new_doc_root, line)
                line = sub_line
        vhost_end_match = vhost_end.search(line)
        if vhost_end_match:
            inhost = False
    yield line

    if __name__ == '__main__':
        import sys
        conf_file = sys.argv[1]
        vhost = sys.argv[2]
        docroot = sys.argv[3]
        conf_string = open(conf_file).read()
        for line in change_error_log(conf_string, vhost, docroot):
            print line
