#!/bin/bash
set -eux

# if there is no system unit file, install a local unit

# enable and start service to poll for deployment changes
systemctl enable os-collect-config
systemctl start --no-block os-collect-config
systemctl restart os-collect-config
