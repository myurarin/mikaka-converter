class MikakaConverter:
    # みかか変換
    def __init__(self):
        # コンストラクタ
        self.mkk_jp_list = ["ぬ","ふ","あ","う","え",
                            "お","や","ゆ","よ","わ",
                            "ほ","へ","た","て","い",
                            "す","か","ん","な","に",
                            "ら","せ","ち","と","し",
                            "は","き","く","ま","の",
                            "り","れ","け","む","つ",
                            "さ","そ","ひ","こ","み",
                            "も","ね","る","め","ろ"]
        self.mkk_en_list = ["1","2","3","4","5",
                            "6","7","8","9","0",
                            "-","^","q","w","e",
                            "r","t","y","u","i",
                            "o","p","a","s","d",
                            "f","g","h","j","k",
                            "l",";",":","]","z",
                            "x","c","v","b","n",
                            "m",",",".","/","\\"]

    def m_to_n(self, m_str):
        # 平仮名から英語に変換
        try:
            return self.mkk_en_list[self.mkk_jp_list.index(m_str)]
        except ValueError:
            return None

    def n_to_m(self, n_str):
        # 英語から平仮名に変換
        try:
            return self.mkk_jp_list[self.mkk_en_list.index(m_str)]
        except ValueError:
            return None

def main():
    mikaka = MikakaConverter()
    print(mikaka.m_to_n("ぷ"))