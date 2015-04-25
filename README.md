# kjv-bible
#The KJV Bible in TOML

##Editing Notes
This version does *not* attempt to stay faitful to any sort of original
typesetting. In particular, words that were bracked as words inserted by the
translators have been retained in-line with no special formatting.

The Psalms are not separated into their individual books.

The goal of this project is to provide a text store that is convient to to access
programatically.


##Format
The format of a Bible toml file is as follows.

```
[Book]
title="The First Book of the Chronicles"

[[Chapter]] #1
text="""\
{1:1} Adam, Sheth, Enosh, {1:2} Kenan, Mahalaleel, Jered, {1:3}
Henoch, Methuselah, Lamech, {1:4} Noah, Shem, Ham, and Japheth.

   {1:5} The sons of Japheth; Gomer, and Magog, and Madai, and Javan,
and Tubal, and Meshech, and Tiras. {1:6} And the sons of Gomer;
Ashchenaz, and Riphath, and Togarmah. {1:7} And the sons of Javan;
Elishah, and Tarshish, Kittim, and Dodanim.
"""
```

Several versification styles will be supported.
Verse divider(placed at the *start* of a verse!): `\\` 
`{<chapter>:<verse>}`
`{<verse>}`

This KJV version will use `{<chapter>:<verse>}` exclusively. This will allow for easier searching if mistakes are found.

#Acknowledgments

Thank you to @toml-lang for a sane format for simple machine parsing, and still being easy on the eye.

Thank you to http://ebible.org/kjv/ for providing a textual KJV with Apocrypha!

