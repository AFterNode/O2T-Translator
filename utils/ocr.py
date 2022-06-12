import easyocr

def make_reader(lang):
    print("[OCR] Loading OCR reader...")
    reader = easyocr.Reader([lang])
    return reader

def scan(reader: easyocr.Reader,
         path: str):
    text = reader.readtext(path)
    text_lst = []
    for t in text:
        text_lst.append(t[1])
    print("[OCR] Get text: ")
    print(text_lst)
    return text_lst


if __name__ == "__main__":
    r = make_reader("ch_sim")
    scan(r, "F:\\PyProj\\O2T Translator\\prtscr.png")
