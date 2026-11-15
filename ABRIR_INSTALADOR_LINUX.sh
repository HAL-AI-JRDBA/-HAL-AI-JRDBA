#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
command -v python3.11 >/dev/null || { echo "Python 3.11 required"; exit 2; }
python3.11 INSTALADOR_GRAFICO.py
