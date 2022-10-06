#!/bin/sh
## ## dir2md.sh
##
## @brief generate autodoc.md for Linux
##
## @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
# @section Changelog
## @date 20201001 Ageest initial version
##
##

PROJECT=$PWD
cd "$( dirname "$0" )" || exit 2
BASE=$PWD
OUTPUT=autodoc.md
# shellcheck disable=SC2034
ROLE=$( basename "${PROJECT}" )

cd "${PROJECT}" || exit 2
true > "$OUTPUT"
## parse script files with the extensions: .yml$|.yaml$|.j2$|.sh$|.php$|.pl$|.py$|.sql$|.ps1$|.xml$|.cmd$|.js$|.pp$|.cfg$
##
## md_filter.py is used in creating the md.
##
## all md is placed in autodoc.md
##
files="README.md $(find . -type f | grep -E '(.yml$|.yaml$|.j2$|.sh$|.php$|.pl$|.py$|.sql$|.ps1$|.xml$|.cmd$|.js$|.pp$|.cfg$)' )"
for file in $files
do
	if [ -e "$file" ]
	then
	  python3 "${BASE}/md_filter.py" "${file}" >> $OUTPUT
	fi
done #/for file
echo >>  $OUTPUT

##
## If Pandoc exists a autodoc.html is created from the autodoc.md
##
if [ -e /usr/bin/pandoc ]
then
   pandoc $OUTPUT  -t html -H "${BASE}/pandoc.header" -o autodoc.html --listings --standalone
 else
  if [ -e /usr/bin/markdown ]
  then
	markdown -f fencedcode "$OUTPUT" --metadata pagetitle="autodoc ${PROJECT}" > autodoc.html
  fi
fi

  

