import os, sys, argparse
import scriptures
import pytoml as toml

SCRIPT_DIR=os.path.dirname(os.path.abspath(sys.argv[0]))
if __name__ is not "__main__":
    SCRIPT_DIR = os.path.dirname(__file__)

class Bible(object):

    def __init__(self, biblepath="./"):
        self._searchpath = biblepath

    def get_passage_by_reference(self, reference):
        """
        Get a passage by reference.
        """
        ref_object = scriptures.extract(reference)[0]
        #for r in ref_object:
        return self.get_passage(*ref_object)

    def get_verses(self, book, c_start, v_start, c_end, v_end):
        raise NotImplementedError

    def get_passage(self, book, start_c, start_v, end_c, end_v):
        text = self.get_verses(book, start_c, start_v, end_c, end_v)
        reference = scriptures.reference_to_string(book, start_c, start_v,
                                                   end_c, end_v)
        return {'ref': reference, 'text': text}


    def __getitem__(self, index):
        """
        We override the [] operator on the bible to allow more natural indexing

        @return: A dict {index, text}
        """
        return self.get_passage_by_reference(index)

class TomlBible(Bible):

    def _find_book_file(self, bookname):
        book_prefix = bookname[0:4]
        if "I " in book_prefix:
            bookname = bookname.replace("I ", "1")
        elif "II " in book_prefix:
            bookname = bookname.replace("II ", "2")
        elif "III " in book_prefix:
            bookname = bookname.replace("II ", "3")
        elif "IV " in book_prefix:
            bookname = bookname.replace("IV ", "4")
        for i in range(0, len(bookname)):
            file_attempt = "%s/%s.toml"%(self._searchpath,
                                         bookname[0:len(bookname)-i])
            if os.path.isfile(file_attempt):
                return file_attempt
                


    def load_book(self, bookname):
        bookfile = self._find_book_file(bookname)
        with open(bookfile) as book_h:
            content =  book_h.read()
        return content


    def get_verses(self, book, c_start, v_start, c_end, v_end):
        book_toml = toml.loads(self.load_book(book))
        print book, c_start, v_start, c_end, v_end
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

            for verse in book_toml['Chapter'][chap-1]['verses'][vs_index:ve_index+1]:
                section += verse
        return section

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given a Church, Rite, language, translation description, and time, generate HTML for a church service.')
    parser.add_argument('--language', '-l', type=str, default='en-us')
    parser.add_argument('--translation','-t', type=str, default='kjv')
    parser.add_argument('reference', metavar="REFERENCE", type=str)

    args = parser.parse_args()
    t = TomlBible(SCRIPT_DIR + "%s/%s/toml/"%(args.language, args.translation))
    print t[args.reference]

