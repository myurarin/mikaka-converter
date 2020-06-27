

class MikakaConverter:
    # みかか変換
    def __init__(self):
        # コンストラクタ
        self.mkk_jp_list = ["ぬ", "ふ", "あ", "う", "え",
                            "お", "や", "ゆ", "よ", "わ",
                            "ほ", "へ", "た", "て", "い",
                            "す", "か", "ん", "な", "に",
                            "ら", "せ", "ち", "と", "し",
                            "は", "き", "く", "ま", "の",
                            "り", "れ", "け", "む", "つ",
                            "さ", "そ", "ひ", "こ", "み",
                            "も", "ね", "る", "め", "ろ"]
        self.mkk_en_list = ["1", "2", "3", "4", "5",
                            "6", "7", "8", "9", "0",
                            "-", "^", "q", "w", "e",
                            "r", "t", "y", "u", "i",
                            "o", "p", "a", "s", "d",
                            "f", "g", "h", "j", "k",
                            "l", ";", ":", "]", "z",
                            "x", "c", "v", "b", "n",
                            "m", ",", ".", "/", "\\"]

    def jp_to_en(self, jp_char):
        # ひらがなから英語に変換
        try:
            return self.mkk_en_list[self.mkk_jp_list.index(jp_char)]
        except ValueError:
            return None

    def en_to_jp(self, en_char):
        # 英語からひらがなに変換
        try:
            return self.mkk_jp_list[self.mkk_en_list.index(en_char)]
        except ValueError:
            return None

    def str_conv(self, str_data, lang_opt):
        # 文字列を変換する
        pass


def main():
    mikaka = MikakaConverter()
    print(mikaka.jp_to_en("ろ"))
