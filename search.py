import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csvPath):
    # 検索対象取得
    try:
        df=pd.read_csv(csvPath)
    except FileNotFoundError:
        # エラーを画面に出力する
        eel.view_err_js()
    
    source=list(df["name"])

    # 検索
    msg = ""
    if word in source:
        msg = "『{}』はあります".format(word)
    else:
        msg = "『{}』はありません".format(word)
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    print(msg)

    # ログを画面に出力する
    eel.view_log_js(msg)

    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(csvPath,encoding="utf_8-sig")

    print(source)
 