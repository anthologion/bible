#!/usr/bin/python
import os, sys
import argparse
import pytoml as toml
import re
SCRIPT_DIR=os.path.dirname(os.path.abspath(sys.argv[0]))

def get_verses(book_toml, c_start, v_start, c_end, v_end):
    section = ""
    for chap in range (int(c_start), int(c_end)+1):
        if chap == c_start:
            vs_index = v_start - 1
        else:
            vs_index = 0
        if chap == c_end:
            ve_index = v_end -1 
        else:
            ve_index = len(book_toml['Chapter'][chap]['verses'])-1

        for verse in book_toml['Chapter'][chap-1]['verses'][vs_index:ve_index]:
            section += verse
    return section


def get_passage(lang, trans, start, end):
    # For the time being, we wil just hardcode things. We can get fnacy later.
    start_match = re.match(r"(\d?\s?\w+) (\d{1,3}):(\d{1,3})", 
                         start)
    end_match = re.match(r"(\d?\s?\w+) (\d{1,3}):(\d{1,3})", 
                         end)
    book = start_match.group(1)
    start_chapter = start_match.group(2)
    start_verse = start_match.group(3)
    end_chapter = end_match.group(2)
    end_verse = end_match.group(3)
    search_path = "%s/%s/%s/toml/%s.toml" % (SCRIPT_DIR, lang, trans, book)
    with open(search_path) as bookfile:
            book_toml= toml.loads(bookfile.read())
    return get_verses(book_toml, int(start_chapter), int(start_verse), 
                      int(end_chapter), int(end_verse))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given a Church, Rite, language, translation description, and time, generate HTML for a church service.')
    parser.add_argument('--language', const='l', type=str, nargs='?', default='en-us')
    parser.add_argument('--translation', const='t', type=str, nargs='?', default='kjv')
    parser.add_argument('start', metavar="START", type=str)
    parser.add_argument('end', metavar="END", type=str)

    args = parser.parse_args()
    print get_passage(args.language, args.translation, args.start, args.end)

