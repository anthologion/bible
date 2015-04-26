
for f in ./txt/*.txt
do
# This bit does several things.
# * Converts Windows newlines to Unix style
# * Removes extraneous whitespaces
# * Special Psalm sauce
# * Creates the chapter array markers
# * Creates verse entries
# * Unwraps bracketed words
# * Adds book marker and title
# * Tidies up the array ending markers

# With more tweaking, this might be able to recover Psalm notes. For right now
# I'm not going to worry about that.
#| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s]*)\s+/{$1:0}$2/g' \
cat $f \
| perl -0777pe 's/\r\n/ /g' \
| perl -0777pe 's/[ \t][ \t]+/ /g' \
| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s,.;\[\]]*)//g' \
| perl -0777pe 's/(\{(\d+):[01]\}) /\]\n\n[[Chapter]] #$2\nverses=\[\n$1 /g' \
| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \
| perl -0777pe '$sq="\047"; s/({\d+:\d+})([\w\s,;."():\[\]$sq]+)(?={\d+:\d+}|\n])/"$2", #$1\n/g' \
| perl -0777pe 's/([\s,.])\[([:,.;\w\s]+)\]([\s,.])/$1$2$3/g' \
| perl -0777pe 's/\s([\w ]+)\s+]/[Book]\ntitle="$1"/sg' \
| perl -0777pe 's/[\s\n]+\]/\n\]/sg' \
> ./toml/`basename ${f%.*}`.toml
done
