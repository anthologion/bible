for f in ./txt/*.txt
do
# This bit does several things.
# * Converts Windows newlines to Unix style
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

cat $f \
| perl -0777pe 's/\r\n/ /g' \
| perl -0777pe 's/[ \t][ \t]+/ /g' \
| perl -0777pe 's/\[([^\[\]]+)\]/$1/sg' \
| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s,.;\[\]]*)//g' \
| perl -0777pe 's/(\{(\d+):[01]\}) /\]\n\n[[Chapter]] #$2\nverses=\[\n$1 /g' \
| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \
| perl -0777pe 's/({\d+:\d+})([^\n{]+)(?={\d+:\d+}|\n])/"$2", #$1\n/g' \
| perl -0777pe 's/\s([^\n]+)\n]\n\n/[Book]\ntitle="$1"\n\n/sg' \
| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \
> ./toml/`basename ${f%.*}`.toml
done
#| perl -0777pe '$sq="\047"; s/({\d+:\d+})([\w\s,;."():\[\]$sq]+)(?={\d+:\d+}|\n])/"$2", #$1\n/g' \
