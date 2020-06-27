# 定数
LANG_OPT_JPN = 0        # ひらがな→英語
LANG_OPT_ENG = 0        # 英語→ひらがな


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

    def char_conv(self, char_data, lang_opt):
        # 文字を変換
        try:
            ret_val = ""        # リターン用変数
            if lang_opt is LANG_OPT_JPN:
                # ひらがなから英語に変換
                ret_val = self.mkk_en_list[self.mkk_jp_list.index(char_data)]
            elif lang_opt is LANG_OPT_ENG:
                # 英語からひらがなに変換
                ret_val = self.mkk_jp_list[self.mkk_en_list.index(char_data)]
            else:
                # それ以外はNone
                ret_val = None
            return ret_val
        except ValueError:
            # 変換できない文字列はNoneとする
            return None

    def str_conv(self, str_data, lang_opt):
        # 文字列を変換する
        ret_val = ""
        for index in range(len(str_data)):
            ret_val += self.char_conv(str_data[index], lang_opt)
        return ret_val


def main():
    mikaka = MikakaConverter()
    str_data = "みかか"
    print(str_data+" = "+mikaka.str_conv(str_data, LANG_OPT_JPN))
