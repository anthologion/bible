#The Bible in TOML


The goal of this project is to provide a text store that is convient to to access
programatically.


##Format
The format of a Bible toml file is as follows.

```
[Book]
title="The Book of Psalms"

[[Chapter]] #134
verses=[
" Behold, bless ye the LORD, all ye servants of the LORD, which by night stand in the house of the LORD. ", #{134:1}
" Lift up your hands in the sanctuary, and bless the LORD. ", #{134:2}
" The LORD that made heaven and earth bless thee out of Zion.", #{134:3}
]

```
The verse numbers in the comments are not in a strictly regulated format, but the
the following conventions are preferred:
`{<chapter>:<verse>}`

`{<verse>}`


This KJV version will use `{<chapter>:<verse>}` exclusively. This will allow
for easier searching, citation, and correction if mistakes are found.

#Acknowledgments

Thank you to @toml-lang for a sane format for simple machine parsing, and still being easy on the eye.

Thank you to http://ebible.org/kjv/ for providing a textual KJV with Apocrypha!

