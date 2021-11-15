#!/bin/env bash
# https://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

if [ "$(basename "${SHELL}")" == "bash" ]; then
  RC_FILE="${HOME}/.bashrc"
elif [ "$(basename "${SHELL}")" == "zsh" ]; then
  RC_FILE="${HOME}/.zshrc"
else
  echo "ERROR: ${SHELL} is not supported"
  exit 1
fi

LCG_VERSION="LCG_93python3"
LCG_SETUP="/cvmfs/sft.cern.ch/lcg/views/${LCG_VERSION}/${CMTCONFIG}/setup.sh"
if [ ! -f "${LCG_SETUP}" ]; then
  echo "ERROR: Failed to find LCG view at: ${LCG_SETUP}"
  exit 1
fi

set +u
source "${LCG_SETUP}"
set -u

python3 -m pip uninstall --yes snakemake || true
python3 -m pip install --user snakemake

{
    echo ''
    echo 'function snakemake() {'
    echo '    source "/cvmfs/sft.cern.ch/lcg/views/'"${LCG_VERSION}"'/${CMTCONFIG}/setup.sh" && \'
    echo '    PYTHON3_USER_BASE=$(python3 -m site --user-base) && \'
    echo '    PYTHON3_USER_SITE=$(python3 -m site --user-site) && \'
    echo '    export PATH="${PYTHON3_USER_BASE}/bin:${PATH}" && \'
    echo '    export PYTHONPATH="${PYTHON3_USER_SITE}:${PYTHONPATH}" && \'
    echo '    "$(which snakemake)" "$@"'
    echo '}'
} >> "${RC_FILE}"
