## @ingroup examples
## @file
##
## @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
## @brief test puppet manifest
##
## @version 20150330
##
## @date 
## - 20150330 Ageest initiele versie
##
# /root/examples/file-2.pp

## Dit is een voorbeeld manifest met de volgende opties:
## - forceer file /tmp/test1
    file {'/tmp/test1':
      ensure  => file,
      content => "Hi.\n",
    }

## - forceer dir /tmp/test2
    file {'/tmp/test2':
      ensure => directory,
      mode   => 0644,
    }

## - forceer link /tmp/test3

    file {'/tmp/test3':
      ensure => link,
      target => '/tmp/test1',
    }

    user {'katie':
      ensure => absent,
    }

## notify user
## @verbatim
    notify {"I'm notifying you.":}
    notify {"So am I!":}
## @endverbatim

