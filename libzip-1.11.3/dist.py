import sys
import os
from os.path import join
from subprocess import Popen, PIPE, STDOUT


def run(args):
    """Run a command and return the output."""
    process = Popen(args, stdout=PIPE, stderr=STDOUT)
    output, _ = process.communicate()
    return output


target = os.environ.get('BUILDROOT', '')
os.chdir(os.environ.get('CURRENT'))
archive_name = sys.argv[1]
run(['git', 'config', 'tar.tar.xz.command', 'xz -c'])
run(['git', 'archive', f'--prefix={archive_name}/', '-o', f'{target}/{archive_name}.tar.gz', 'HEAD'])
run(['git', 'archive', f'--prefix={archive_name}/', '-o', f'{target}/{archive_name}.tar.xz', 'HEAD'])
