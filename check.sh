#!/bin/bash
set -e
cd -- "$(dirname -- "$0")"
echo "===calculator quality gate==="
python3 -m pytest -v
echo "quality gate passed"
