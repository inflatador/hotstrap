def configurate():
    file_list = ['opt/stack/os-config-refresh/configure.d/20-os-apply-config',
                 'opt/stack/os-config-refresh/configure.d/55-heat-config',
                 'usr/bin/heat-config-notify',
                 'var/lib/heat-config/hooks/ansible',
                 'var/lib/heat-config/hooks/script',
                 'var/lib/heat-config/hooks/puppet',
                 'etc/os-collect-config.conf',
                 'usr/libexec/os-apply-config/templates/var/run/heat-config/heat-config',
                 'usr/libexec/os-apply-config/templates/etc/os-collect-config.conf']
    print('Moving configuration files to the proper locations\n\n')
    for i in range(3):
        print('/' + file_list[i])
    for i in range(3, 6):
        print '2'
        print('/' + file_list[i])

configurate()
