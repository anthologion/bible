
for f in ./txt/*.txt
do
# This bit does several things.
# 1) Converts Windows newlines to Unix style
# 2) Creates the chapter array markers
# 3) Removes extraneous whitespaces
# 4) Removes bracketed words
cat $f | perl -0777pe 's/\r\n/\n/g' \
| perl -pe 's/(\{(\d)+:1\}) /"""\n\n[[Chapter]] #$2\ntext="""\\\n$1 /' \
| perl -pe 's/[ \t][ \t]+/ /' \
| perl -0777pe 's/([\s,.])\[([:,.;\w\s]+)\]([\s,.])/$1$2$3/g' \
> `basename ${f%.*}`.toml
done
