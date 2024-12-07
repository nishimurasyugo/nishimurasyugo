import streamlit as st
import pandas as pd

# 1回のエクササイズにかかる時間（秒）
exercise_time = 60  # 1分間

# 道具を使わずにできるエクササイズ
exercises = {
    "腕立て伏せ": 3,  # 3セット
    "スクワット": 3,
    "クランチ": 3,
    "ランジ": 3,
    "プランク": 2,  # セット数
    "サイドプランク": 2,
    "バーピー": 3,
    "マウンテンクライマー": 3
}

# 1回あたりのセット数
sets = {
    "腕立て伏せ": 12,
    "スクワット": 15,
    "クランチ": 20,
    "ランジ": 12,
    "プランク": 30,  # 秒
    "サイドプランク": 20,  # 秒
    "バーピー": 10,
    "マウンテンクライマー": 20
}

# メニューを作成する関数
def generate_daily_menu():
    menu = []
    total_time = 0
    for exercise, num_sets in exercises.items():
        set_time = sets[exercise] * exercise_time  # 1セットにかかる時間
        exercise_total_time = set_time * num_sets  # エクササイズの合計時間（秒）
        total_time += exercise_total_time
        menu.append([exercise, num_sets, set_time, exercise_total_time])
    
    # 表の作成
    df = pd.DataFrame(menu, columns=["エクササイズ", "セット数", "1セットの時間（秒）", "総時間（秒）"])
    df["総時間（秒）"] = df["総時間（秒）"].apply(lambda x: f"{x / 60:.1f} 分")  # 分単位に変換
    total_time_min = total_time / 60  # 総時間（分）
    
    return df, total_time_min

# Streamlit アプリのタイトル
st.title("道具を使わずにできる筋トレメニュー")

# メニューを生成
daily_menu, total_time = generate_daily_menu()

# メニューを表示
st.subheader("1日の筋トレメニュー")
st.write(f"このメニューは約{total_time:.1f}分で完了します。")
st.table(daily_menu)

# ヒント
st.subheader("ヒント")
st.write("""
- 各エクササイズの間に30秒〜1分の休憩を取ってください。
- 適切なフォームで行うことを心がけましょう。
- トレーニングがきつい場合は、回数を減らして徐々に増やしていきましょう。
""")
