#!/bin/bash

ROOT="$(cd "${0%/*/*}"; pwd)"
TO="$ROOT/tmp/out.txt"

DIRS=(
  cos
  databases
  tools
)

EXTRA_FILES=(
  Makefile
  pip-req.txt
  serve.py
)

cat /dev/null > $TO

for sub in "${DIRS[@]}"; do
  echo $sub
  for f in `find $ROOT/$sub`; do
    if [[ $f =~ .py$ || $f =~ .sql$ || $f =~ .plim$ || $f =~ .sh$ ]]; then
      echo >> $TO
      echo "================================================================================" >> $TO
      echo "SOURCE: ${f#/*/*/*/}" >> $TO
      echo "================================================================================" >> $TO
      echo >> $TO
      cat $f >> $TO
    fi
  done
done

for file in "${EXTRA_FILES[@]}"; do
  for f in `find $ROOT/$file`; do
    echo >> $TO
    echo "================================================================================" >> $TO
    echo "SOURCE: ${f#/*/*/*/}" >> $TO
    echo "================================================================================" >> $TO
    echo >> $TO
    cat $f >> $TO
  done
done

less $TO
