- \[BACK\](autodoc.md)
 @file

 @brief MD filter


 @author Arco van Geest <d.a.c.vangeest@tudelft.nl>


 @date 20190906 first version

 grab marked MD lines from source and output md to stdout


 Depending on the extention a filter is used:
 ```

    'php': filter_shell,
    'cfg': filter_cfg,
    'cmd': filter_cmd,
    'Dockerfile': filter_cfg,
    'sh': filter_shell,
    'awk': filter_cfg,
    'add': filter_cfg,
    'conf': filter_cfg,
    'dox': filter_default,
    'ps1': filter_cfg,
    'pl': filter_cfg,
    'xml': filter_xml,
    'xslt': filter_xml,
    'html': filter_xml,
    'ini': filter_ini,
    'pp': filter_cfg,
    'sql': filter_sql,
    'c': filter_default,
    'h': filter_default,
    'cpp': filter_default,
    'md': filter_default,
    'py': filter_shell,
    'yaml': filter_cfg,
    'yml': filter_cfg,
    'au3': filter_cfg,
    'ipxe': filter_cfg

 ```

#### filter_shell
 filter shell to md

 lines starting with the magic '##' will be shown.

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.

 lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.


#### filter_cmd
 filter cmd to md

 lines starting with the magic '::!' will be shown.

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.

 lines between the magics '::! SKIP_START' and '::! SKIP_END' will be skipped.


#### filter_cfg
 filter cfg to md

 lines starting with the magic '##' will be shown.

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.

 lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.


#### filter_xml
 filter xml to md

 lines starting with the magic '<!---' will be shown until the first '-->'.

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.

 lines between the magics '<!--- SKIP_START' and '<!--- SKIP_END' will be skipped.


#### filter_ini
 filter ini to md

 lines starting with the magic ';;' will be shown.\n

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.\n

 lines between the magics ';; SKIP_START' and ';; SKIP_END' will be skipped.\n

 section headers [name] wil result in a section header

 section name s

#### filter_sql
 filter sql to md

 lines starting with the magic '--!' will be shown.

 lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.

 lines between the magics '--! SKIP_START' and '--! SKIP_END' will be skipped.

#### filter_default
 pass though filter

 just read and output data

___
