
for f in ./txt/*.txt
do
# This bit does several things.
# 1) Converts Windows newlines to Unix style
# 2) Creates the chapter array markers
# 3) Removes extraneous whitespaces
# 4) Removes bracketed words

# With more tweaking, this might be able to recover Psalm notes. For right now
# I'm not going to worry about that.
#| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s]*)\s+/{$1:0}$2/g' \
cat $f \
| perl -0777pe 's/\r\n/\n/g' \
| perl -0777pe 's/Psalm (\d+)\s+(\w?[\w\s,.;\[\]]*)//g' \
| perl -pe 's/(\{(\d+):[01]\}) /"""\n\n[[Chapter]] #$2\ntext="""\\\n$1 /' \
| perl -pe 's/[ \t][ \t]+/ /' \
| perl -0777pe 's/([\s,.])\[([:,.;\w\s]+)\]([\s,.])/$1$2$3/g' \
| perl -0777pe 's/\s([\w ]+)\s+"""/[Book]\ntitle="$1"/sg' \
| perl -0777pe 's/[\s\n]+"""/\n"""/sg' \
> ./toml/`basename ${f%.*}`.toml
done
