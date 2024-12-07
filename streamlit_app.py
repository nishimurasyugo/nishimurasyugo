# 必要なライブラリをインポート
import streamlit as st

# ユークリッドの互除法アルゴリズムを実装する関数
def euclidean_algorithm(a, b):
    # 計算手順を記録するリスト
    steps = []  
    
    # bが0になるまで繰り返し計算
    while b != 0:
        # 商と余りを求める
        remainder = a % b
        # 計算の手順をリストに追加
        steps.append(f"{a} ÷ {b} = {a // b} 余り {remainder}")
        # a, bの値を更新（次のステップに進む）
        a, b = b, remainder
        
    # 最終的にaが最大公約数となる
    return a, steps

# Streamlitのインターフェースの設定
st.title("ユークリッドの互除法で最大公約数を計算")

# ユーザーから2つの整数を入力してもらう
# ここでmin_value=1は1以上の数値を入力させる制約をかけている
a = st.number_input("整数aを入力してください", min_value=1, value=48)
b = st.number_input("整数bを入力してください", min_value=1, value=18)

# 計算ボタンを押したときの処理
if st.button("最大公約数を計算"):
    # ユーザーが入力した値が有効かを確認
    if a > 0 and b > 0:
        # ユークリッドの互除法を使って最大公約数と計算手順を取得
        gcd, steps = euclidean_algorithm(a, b)
        
        # 結果を表示
        st.subheader(f"最大公約数: {gcd}")
        st.write("計算手順:")
        for step in steps:
            st.write(step)  # 各ステップを1行ずつ表示
    else:
        # 入力が不正な場合のエラーメッセージ
        st.error("整数aとbは1以上の値を入力してください。")
