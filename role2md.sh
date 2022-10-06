#!/bin/sh
## ## role2md.sh
##
## @brief generate autodoc.md for ansible roles
##
## @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
# @section Changelog
## @date 20201001 Ageest initiele versie
##
##

PROJECT=$PWD
cd "$( dirname "$0" )" || exit 2
BASE=$PWD
OUTPUT=autodoc.md
ROLE=$( basename "${PROJECT}" )

if [ -e "${PROJECT}/tasks" ]
then
  echo "role ${ROLE}"
else
  echo "not role directory detected"
  exit 1
fi

cd "${PROJECT}" || exit 2
true > "$OUTPUT"
##
## Files are parsed from directories: tasks handlers defaults vars tests
for dir in tasks handlers defaults vars tests
do
  if [ -d "$dir" ]
  then
    if [ -e "$dir/main.yml" ]
    then
      echo "$dir " >> $OUTPUT
      echo "=====" >> $OUTPUT
      ##
      ## parse script files with the extensions: .yml$|.yaml$|.j2$|.sh$
      files="$dir/main.yml $( find "$dir" -type f| grep -E '(.yml$|.yaml$|.j2$|.sh$)' |grep -v "${dir}/main.yml" )"
      #echo $files >> $OUTPUT
      for file in $files
      do
        if [ -e "$file" ]
        then
      #    echo "parse ${file}" >>  $OUTPUT
          ##
          ## md_filter.py is used in creating the md.
          python3 "${BASE}/md_filter.py" "${file}" >> "$OUTPUT"
        fi
      done #/for file
      ##
      ## all md is placed in autodoc.md
      echo >>  "$OUTPUT"
    fi #/main.yml
  fi #/dir
done
  

