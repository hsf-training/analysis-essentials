#!/usr/bin/env bash
# lychee --preprocess helper: check the cell sources of notebooks instead of
# their raw JSON, where escaped "\n" and "\"" get glued onto URLs.
case "$1" in
*.ipynb)
    exec jq -r '.cells[].source | if type == "array" then join("") else . end' "$1"
    ;;
*)
    exec cat "$1"
    ;;
esac
