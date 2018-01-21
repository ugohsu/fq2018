#!/usr/bin/env bash
mkdir unit
find csv/ -type f | while read x; do sed '2,3d' $x > unit/$(basename $x); done
