<## 
 @ingroup source
 @file

 @brief Voorbeeld Powershell .ps1
 
 @version 1.0

 @author Arco van Geest <d.a.c.vangeest@tudelft.nl>

 @date 20160908 Ageest Eerste versie

 
  
  Voorbeeld documentatie 
#>

<#
 
 .SYNOPSIS 
  a brief explanation of what the script or function does.

  .DESCRIPTION 
  a more detailed explanation of what the script or function does.

 .PARAMETER name 
  an explanation of a specific parameter. 
  
  .EXAMPLE
  an example of how to use the script or function. You can have multiple .EXAMPLE sections if you want to provide more than one example.

  .NOTES
  any miscellaneous notes on using the script or function.

  .LINK 
  a cross-reference to another help topic; you can have more than one of these. If you include a URL beginning with http:// or https://, the shell will open that URL when the Help command’s –online parameter is used.

#>

# commentaar
## documentatie
echo "Hallo"


function SendHallo ([string]$naam) {
<#
 .SYNOPSIS 
  Begroet iemand

 .DESCRIPTION 
  Begroet iemand met Hallo

 .PARAMETER [string]naam 
  Te begroeten naam
  
 .EXAMPLE
  @code
  SendHallo("Gebruiker")
  @endcode

 .NOTES
  any miscellaneous notes on using the script or function.

 .LINK 
  a cross-reference to another help topic; you can have more than one of these. If you include a URL beginning with http:// or https://, the shell will open that URL when the Help command’s –online parameter is used.

#>
## ____
## of anders...
##
## [string]$naam - te begroeten naam
##
## let wel op de lege regels, anders is er geen line break
	echo "Hallo $naam `n`r"
}

SendHallo("gebruiker")