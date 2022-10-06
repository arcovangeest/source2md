#!/bin/sh
## ## dir2dirmd.sh
# #@file
# #
# # @brief generate autodoc.md for script directories
##
## author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
# @section Changelog
## #### Changelog
## 20201001 Ageest initial version
## 20210114 AGeest links to roles
## 20221006 AGeest disabled links to roles
##

PROJECT=$PWD
cd "$( dirname "$0" )" || exit 2
BASE=$PWD
OUTPUT=autodoc.md
# shellcheck disable=SC2034
ROLE=$( basename "${PROJECT}" )

cd "${PROJECT}" || exit 2
mkdir -p autodoc
true > "$OUTPUT"
if [ -d "./roles" ]
then
  ##
  ## Roles
  ##
  echo "### Roles" >> "$OUTPUT"
  echo "See specific directories for role documentation."
  # shellcheck disable=SC2012
  ls ./roles|sort| while read -r role
  do
    ## - Get readme from role
    if [ -e "roles/$role/README.md" ]
    then
      ## - create link in autodoc.md (disabled because it fails with submodules)
      #echo "- [${role}](roles/$role/README.md)"  >> $OUTPUT
      ## - show role name
      echo "- ${role}"  >> "$OUTPUT"
      ##
    fi
  done
  echo "### Autodoc" >> "$OUTPUT"
fi

##
## parse script files with the extensions: .yml$|.yaml$|.j2$|.sh$|.php$|.pl$|.py$|.sql$|.ps1$|.xml$|.cmd$|.js$|.pp$|.cfg$
##
## md_filter.py is used in creating the md.
##
## all md is placed in autodoc
##
## an index is created : autodoc.md
##
files="$(find . -type f|sort   | grep -E -v '^(./.git|./roles/|./group_vars|./old)' | grep -E '(.yml$|.yaml$|.j2$|.sh$|.php$|.pl$|.py$|.sql$|.ps1$|.xml$|.cmd$|.js$|.pp$|.cfg$)' )"
for file in $files
do
        if [ -e "$file" ]
        then
          OUTPUTMD="autodoc/$( echo "$file" |sed 's/^[.][/]//'|sed 's/[ /]/_/g' ).md"

#echo          python3 ${BASE}/md_filter.py "${file}"  "$OUTPUTMD"

          echo "- \[BACK\](autodoc.md)" > "$OUTPUTMD"
          python3 "${BASE}/md_filter.py" "${file}" >> "$OUTPUTMD"
          echo "___" >>  "$OUTPUTMD"
          echo "- \[${file}\](${OUTPUTMD})" >> "$OUTPUT"
        fi
done #/for file
echo >>  "$OUTPUT"

