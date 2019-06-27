#!/usr/bin/env python

import sys
import os
import requests
import subprocess
import git


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
    for package in package_list:
        print('Installing + ' + package)
        os.system('yum install -y '+ package + '> /dev/null')
        print('Successful\n')


def get_configuration():
    print('Cloning down configuration files')
    git.Git('./').clone('git://github.com/kmcjunk/hotstrap.git')


def pip_down():
    print('\nInstalling OpenStack HEAT requirements via pip')
    os_list = [ 'os-collect-config',
                'os-apply-config',
                'os-refresh-config',
                'dib-utils' ]
    os.system('pip install -U decorator')
    for package in os_list:
        print('Installing ' + package)
        os.system('pip install ' + package)
        print('Successfull')


# def configurate():


def touch_some_things():
    os.system('pip install -U decorator')
    os.system('pip install os-collect-config os-apply-config os-refresh-config dib-utils')
    os.system('yum install puppet -y')
    os.system('os-collect-config --one-time --debug')
    os.system('cat /etc/os-collect-config.conf')
    os.system('os-collect-config --one-time --debug')
    os.system('pip install ansible==2.4.3.0')


def delete_some_other_things():
    os.system('rm -rf /var/lib/cloud/instance')
    os.system('rm -rf /var/lib/cloud/instances/*')
    os.system('rm -rf /var/lib/cloud/data/*')
    os.system('rm -rf /var/lib/cloud/sem/config_scripts_per_once.once')
    os.system('rm -rf /var/log/cloud-init.log')
    os.system('rm -rf /var/log/cloud-init-output.log')


get_configuration()
