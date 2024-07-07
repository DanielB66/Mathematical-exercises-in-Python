def ispanegram(txt: str) -> bool:
    lower_txt = txt.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for ch in abc:
        if ch not in lower_txt:
            return False
    return True


print(ispanegram('daniel'))