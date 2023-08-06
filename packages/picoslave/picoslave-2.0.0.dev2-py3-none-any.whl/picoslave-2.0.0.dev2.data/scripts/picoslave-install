#!/usr/bin/env bash

sudo /bin/bash <<EOF
    echo "Installing and reloading udev rules for PicoSlave USB device..."

    echo "    creating /etc/udev/rules.d/99-picoslave.rules"

    cat <<EOT > /etc/udev/rules.d/99-picoslave.rules
BUS!="usb", ACTION!="add", SUBSYSTEM!=="usb_device", GOTO="picoslave_rules_end"

ATTR{idVendor}=="1209", ATTR{idProduct}=="c12c", MODE="664", GROUP="plugdev", TAG+="uaccess"

LABEL="picoslave_rules_end"
EOT

    echo "    udevadm control --reload"
    udevadm control --reload

    echo "    udevadm trigger --attr-match=subsystem=usb"
    udevadm trigger --attr-match=subsystem=usb

    echo "Installation complete."
EOF
