#!/bin/bash

DIR=databases

echo "executing $DIR/schema.sql"
mysql < "$DIR/schema.sql"

for f in `ls $DIR/init_*.sql`; do
  echo "executing $f"
  mysql < $f
done
