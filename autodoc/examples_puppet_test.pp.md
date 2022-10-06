- [BACK](autodoc.md)
 @ingroup examples
 @file

 @author Arco van Geest <d.a.c.vangeest@tudelft.nl>

 @brief test puppet manifest

 @version 20150330

 @date
 - 20150330 Ageest initiele versie

 Dit is een voorbeeld manifest met de volgende opties:
 - forceer file /tmp/test1
 - forceer dir /tmp/test2
 - forceer link /tmp/test3
 notify user

    notify {"I'm notifying you.":}
    notify {"So am I!":}

___
