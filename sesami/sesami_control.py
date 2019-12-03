# 【前提】
# クーロンを使ってこの実行ファイルを定期的に実行する
# （周期は負荷等を考慮し、検討する）
# 【処理フロー】
# １．リードスイッチが「ON」になっているか判断
# ２．「ON」になっていたら、オプションを読み取る
# 　－１．有効／無効
# 　－２．タイマー値（ONになってから何secでカギを閉めるか）

# ３．タイマー値分ディレイした後、カギを閉める


from io import open
import dir_path

if __name__ == '__main__':

    path = dir_path.etc_path()

    with open(path) as f:
        list = f.readlines()

    length = len(list)
    for i in range(length):
        

    s_enable
    i_timer
    


