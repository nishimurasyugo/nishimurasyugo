# 必要なライブラリをインポート
import streamlit as st
import random
from datetime import datetime

# 運勢をランダムに生成する関数
def get_daily_fortune():
    # 運勢のリストを定義
    fortunes = [
        "今日はとても良い日です！新しいことにチャレンジしてみましょう。",
        "少し注意が必要な日です。慎重に行動しましょう。",
        "今日は気分が上向き！友達と楽しい時間を過ごすと良いでしょう。",
        "思わぬトラブルに巻き込まれるかもしれません。冷静に対処しましょう。",
        "今日はラッキーな日です！運が味方してくれそう。",
        "ストレスがたまりやすい日です。リラックスする時間を作りましょう。",
        "今日の運勢は中程度です。無理せず、ゆっくりと過ごすと良いでしょう。",
        "今日は少し注意が必要な日です。大事な決断は後回しにして、落ち着いて考えましょう。",
        "today is your happy day,so you shuold express your feelings"
    ]
    # ランダムに運勢を選ぶ
    return random.choice(fortunes)

# Streamlitのインターフェース
st.title("誕生日による今日の運勢")

# ユーザーから誕生日（月と日）を入力してもらう
month = st.number_input("誕生月を入力してください（1〜12）", min_value=1, max_value=12, step=1)
day = st.number_input("誕生日の日付を入力してください（1〜31）", min_value=1, max_value=31, step=1)

# 入力された誕生日に基づく運勢を表示するボタン
if st.button("運勢をチェック"):
    # 現在の日付を取得
    today = datetime.today()
    current_month = today.month
    current_day = today.day
    
    # 今日の運勢を取得
    fortune = get_daily_fortune()
    
    # 月日が一致した場合に運勢を表示
    if month == current_month and day == current_day:
        st.subheader(f"お誕生日おめでとうございます！")
        st.write(f"あなたの今日の運勢は：{fortune}")
    else:
        st.subheader(f"今日の運勢は:")
        st.write(f"あなたの誕生日は{month}月{day}日ですね。")
        st.write(f"今日の運勢は：{fortune}")
