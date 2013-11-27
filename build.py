#!/usr/bin/python

## @package mycmd
#  easy to use my project
#
#  @author Holiday Hao <Holiday.Hao@acer.com>
#  @version

import sys
import os
import optparse
import ConfigParser

class Build:
    actions = []

    config_file = 'build.conf'
    config = ConfigParser.SafeConfigParser()
    
    mkMtk = './makeMtk -t '
    ver = '-o=TARGET_BUILD_VARIANT='
    MSG_USAGE = "build.py [ -s -v -c -n -r -k --system --sign]"

    def __init__(self, argv):
        self.config.read(self.config_file)

        self.parser = optparse.OptionParser(self.MSG_USAGE)
        self.parser.add_option('-s', action='store', type='string', dest='project', help="Project build name")
        self.parser.add_option('-v', action='store', type='string', dest='ver', help="user userdebug eng")
        self.parser.add_option('-c', action='store_true', dest='clean', help="Clean", default=False)
        self.parser.add_option('-n', action='store_true', dest='new', help="New build", default=False)
        self.parser.add_option('-r', action='store_true', dest='remake', help="Remake", default=False)
        self.parser.add_option('-k', action='store_true', dest='kernel', help="Build kernel", default=False)
        self.parser.add_option('--system', action='store_true', dest='android', help="Build kernel", default=False)
        self.parser.add_option('--sign', action='store_true', dest='sign', help="Sign image", default=False)
        self.parser.add_option('--debug', '-g', action='store_true', dest='debug', help="For debug",default=False)
        self.options, self.args = self.parser.parse_args(argv)

    def add_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        result = ''
        for i in range(len(self.actions)):
            if (i == len(self.actions) -1):
                result += self.actions[i] + ' '
            else:
                result += self.actions[i] + ','

        if result == '':
            result = 'r '

        return result

    def run(self):
        commands = []

        cmd = self.mkMtk
        flag = ''
        flag2 = ''

        if not self.config.has_section('core'):
            self.config.add_section('core')
            self.add_action('n')

        if self.options.ver != None:
            cmd += self.ver + self.options.ver + ' '
            self.config.set('core', 'version', self.options.ver)
        elif self.config.has_option('core', 'version'):
            cmd += self.ver + self.config.get('core', 'version') +  ' '

        if self.options.project != None:
            cmd += self.options.project + ' '
            self.config.set('core', 'project', self.options.project)
        elif self.config.has_option('core', 'project'):
            cmd += self.ver + self.config.get('core', 'project') + ' '

        if self.options.clean:
            self.add_action('c')

        if self.options.new:
            self.add_action('n')

        if self.options.remake:
            self.add_action('r')

        if self.options.kernel:
            flag += 'k '
            flag2 += 'bootimage'
            commands.append(cmd + self.get_actions() + flag)
            commands.append(cmd + flag2)
        elif self.options.android:
            flag += 'dr '
            flag2 += 'systemimage'
            commands.append(cmd + self.get_actions() + flag)
            commands.append(cmd + flag2)
        else:
            commands.append(cmd + self.get_actions() + flag)

        if self.options.sign:
            commands.append(cmd + 'sign-image')


        file = open(self.config_file, 'w')
        self.config.write(file)
        file.close()

        self.execute(commands)


    def execute(self, cmds):
        for cmd in cmds:
            if self.options.debug:
                print cmd
            else:
                os.system(cmd)


def main():
    build = Build(sys.argv)
    build.run()

if __name__ == '__main__':
    main()
