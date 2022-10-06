#!/bin/bash
##@file
##
## @brief Example SH
##
## @version 1.0
##
## @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
## @date 20190906 first version
##

## Example documentation
echo Hello

function bash_function {
## function bash_function
## -------
##      filter has no support for functions
##      create all text yourself
##      parameter - value
##      returns - value
    echo $1
}

## SKIP_START
## "hidden"
## SKIP_END

## @verbatim
echo "This command is shown in the documentation"
## @endverbatim


##
# end
