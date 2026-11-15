#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
command -v python3.11 >/dev/null || { echo "Install Python 3.11";exit 2; }
exec python3.11 install.py --os linux
