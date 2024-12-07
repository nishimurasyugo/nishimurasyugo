# 必要なライブラリをインポート
import streamlit as st

# 拡張ユークリッドの互除法アルゴリズム
def extended_euclidean_algorithm(a, b):
    # 初期値を設定
    x0, x1, y0, y1 = 1, 0, 0, 1
    steps = []  # 計算の手順を記録するリスト
    
    # ユークリッドの互除法を拡張したアルゴリズム
    while b != 0:
        # 商と余りを求める
        q = a // b
        r = a % b
        # 更新式に基づき x と y の係数を更新
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
        # 手順を記録
        steps.append(f"{a} = {b} * {q} + {r}")
        
        # 次のステップへ
        a, b = b, r
        
    # 最後に残ったaが最大公約数、x0とy0がその解
    return a, x0, y0, steps

# Streamlitのインターフェース
st.title("拡張ユークリッドの互除法による最大公約数と不定方程式の解")

# ユーザーから2つの整数を入力してもらう
a = st.number_input("整数aを入力してください", min_value=1, value=48)
b = st.number_input("整数bを入力してください", min_value=1, value=18)

# 計算ボタンを押したときの処理
if st.button("最大公約数と不定方程式の解を計算"):
    if a > 0 and b > 0:
        # 拡張ユークリッドの互除法で最大公約数と解を計算
        gcd, x, y, steps = extended_euclidean_algorithm(a, b)
        
        # 結果を表示
        st.subheader(f"最大公約数: {gcd}")
        st.write("不定方程式の解 (x, y):")
        st.write(f"x = {x}, y = {y}")
        st.write("計算手順:")
        
        # 計算手順を表示
        for step in steps:
            st.write(step)
    else:
        # 入力が不正な場合のエラーメッセージ
        st.error("整数aとbは1以上の値を入力してください。")
