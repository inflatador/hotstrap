#!/usr/bin/env python

import sys
import os
import subprocess
import shutil


# Install required packages via yum
def install_packages():
    package_list = ['python-pip',
                    'gcc',
                    'git',
                    'python-devel',
                    'libyaml-devel',
                    'openssl-devel',
                    'libffi-devel',
                    'libxml2-devel',
                    'libxslt-devel',
                    'puppet']
    print('Installing packages')
    try:
        for package in package_list:
            print('Installing + ' + package)
            os.system('yum install -y ' + package + '>/dev/null')
            print('Successful\n')
    except:
        print('Unsuccessful')


# Install required packages via pip
def pip_down():
    print('\nInstalling OpenStack HEAT requirements via pip')
    os_list = [ 'os-collect-config',
                'os-apply-config',
                'os-refresh-config',
                'dib-utils',
                'gitpython' ]
    try:
        print('Installing decorator')
        os.system('pip install -U decorator >/dev/null')
        for package in os_list:
            print('Installing ' + package)
            os.system('pip install ' + package + '>/dev/null')
            print('Successful')
        print('Installing ansible')
        os.system('pip install ansible==2.4.3.0 > /dev/null')
    except:
        print('Unsuccessful')


# Remove git repo if it exist & clone it down again
def git_configuration():
    import git
    try:
        shutil.rmtree('hotstrap/')
    except OSError:
        pass
    print('\nCloning down configuration files')
    git.Git('./').clone('git://github.com/kmcjunk/hotstrap.git')


# Move configuration files to the proper location on the OS
def configurate():
    file_list = ['etc/os-collect-config.conf',
                  'opt/stack/os-config-refresh/configure.d/20-os-apply-config',
                  'opt/stack/os-config-refresh/configure.d/55-heat-config',
                  'usr/bin/heat-config-notify',
                  'usr/libexec/os-apply-config/templates/etc/os-collect-config.conf',
                  'usr/libexec/os-apply-config/templates/var/run/heat-config/heat-config',
                  'var/lib/heat-config/hooks/ansible',
                  'var/lib/heat-config/hooks/script' ]
    print('Moving configuration files to the proper locations\n\n')
    for file in file_list:
        directory = os.path.dirname('/' + file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        print('hotstrap/' + file + '\t->\t' + '/' + file)
        shutil.move('hotstrap/' + file, '/' + file)


# Run os-collect to propagate the config & run it again
# Then run start_config to ensure everything is enabled properly
def jiggle_some_things():
    print('\nRunning os-collect-config & ensuring os-collect-config-exist')
    os.system('os-collect-config --one-time --debug')
    os.system('cat /etc/os-collect-config.conf')
    os.system('os-collect-config --one-time --debug')
    print('\nEnsuring everything is running & enabled on boot')
    subprocess.call('hotstrap/start_config_agent.sh')
    print('\nCleaning up git folder')
    shutil.rmtree('hotstrap/')


# Ensure we don't get rekt by cloud-init next boot
def delete_some_other_things():
    print('Ensuring no cloud-init references exist')
    os.system('rm -rf /var/lib/cloud/instance')
    os.system('rm -rf /var/lib/cloud/instances/*')
    os.system('rm -rf /var/lib/cloud/data/*')
    os.system('rm -rf /var/lib/cloud/sem/config_scripts_per_once.once')
    os.system('rm -rf /var/log/cloud-init.log')
    os.system('rm -rf /var/log/cloud-init-output.log')
    print('\n\n\nDone!')

install_packages()
pip_down()
git_configuration()
configurate()
jiggle_some_things()
delete_some_other_things()
