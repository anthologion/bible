from pathlib import Path
import re
import os

pathlist = Path("./txt").glob('*.txt')
for path in pathlist:
# This bit does several things.
# * Converts Windows newlines to Unix style
# * Convert newlines to spaces
# * Removes extraneous whitespaces
# * Unwraps bracketed words
# * Special Psalm sauce
# * Creates opening chapter array marker
# * Creates closing chapter array markers
# * Creates verse entries
# * Adds book marker and title
# * Tidies up the array ending markers

# With more tweaking, this might be able to recover Psalm notes. For right now
# I'm not going to worry about that.
#| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s]*)\s+/{$1:0}$2/g' \
    p = str(path)
    with open(p, 'r') as f:
        txt = f.read()

        txt = re.sub('\r\n', '\n', txt)
        txt = re.sub('\n', ' ', txt)
        txt = re.sub('[ \t][ \t]+', ' ', txt)
        

        base = os.path.splitext(os.path.basename(p))[0]
        with open("./toml/" + str(base) + ".toml", 'w') as out:
            out.write(txt)
#| perl -0777pe 's/\[([^\[\]]+)\]/$1/sg' \
#| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s,.;\[\]]*)//g' \
#| perl -0777pe 's/(\{(\d+):[01]\}) /\]\n\n[[Chapter]] #$2\nverses=\[\n$1 /g' \
#| perl -0777pe 's/$/]\n/g' \
#| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \
#| perl -0777pe 's/({\d+:\d+})([^\n{]+)(?={\d+:\d+}|\n])/"$2", #$1\n/g' \
#| perl -0777pe 's/\s([^\n]+)\n]\n\n/[Book]\ntitle="$1"\n\n/sg' \
#| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \

#| perl -0777pe '$sq="\047"; s/({\d+:\d+})([\w\s,;."():\[\]$sq]+)(?={\d+:\d+}|\n])/"$2", #$1\n/g' \

