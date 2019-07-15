#!/bin/bash
set -eux

# if there is no system unit file, install a local unit
if [ ! -f /usr/lib/systemd/system/os-collect-config.service ]; then

    cat <<EOF >/etc/systemd/system/os-collect-config.service
[Unit]
Description=Collect metadata and run hook commands.

[Service]
ExecStart=/usr/bin/os-collect-config
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

cat <<EOF >/etc/os-collect-config.conf
[DEFAULT]
command=os-refresh-config
EOF
    fi

# enable and start service to poll for deployment changes
systemctl enable os-collect-config
systemctl start --no-block os-collect-config
