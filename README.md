# kjv-bible
The KJV Bible in TOML

The format of a Bible toml file is as follows

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
Verse divider(placed at the *start* of a verse!): `\\`` 
`{<chapter>:<verse>}`
`{<verse>}`

This KJV version will use `{<chapter>:<verse>}` exclusively. This will allow for easier searching if mistakes are found.

