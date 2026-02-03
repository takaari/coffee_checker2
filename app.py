import streamlit as st

# ===== 背景色（カフェオレ色）をCSSで設定 =====
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5e6ca;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
h1, h2, h3, p, label {
    color: #5a4632 !important;
    font-family: "Segoe UI", "Cursive", sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===== タイトル =====
st.markdown(
    "<h1 style='text-align: center; font-family: cursive; color: #5a4632;'>☕ Coffee Price Checker 2</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>1gあたり・100gあたりの値段で比較します。</p>",
    unsafe_allow_html=True
)
st.write("")

# ===== Aのコーヒー =====
st.subheader("Aのコーヒー")
a_price = st.number_input("Aの値段（円）", min_value=0, value=0, key="a_price")
a_weight = st.number_input("Aのグラム数（g）", min_value=0, value=0, key="a_weight")

# ===== Bのコーヒー =====
st.subheader("Bのコーヒー")
b_price = st.number_input("Bの値段（円）", min_value=0, value=0, key="b_price")
b_weight = st.number_input("Bのグラム数（g）", min_value=0, value=0, key="b_weight")

#def reset_inputs():
#    for key in ["a_price", "a_weight", "b_price", "b_weight"]:
#        if key in st.session_state:
#            del st.session_state[key]



# ===== 結果ボタン =====
if st.button("結果を表示"):
    if a_price == 0 or b_price == 0 or a_weight == 0 or b_weight == 0:
        st.warning("⚠️ 値段・グラム数は0より大きい値を入力してください。")
    else:
        # --- 計算 ---
        a_price_per_g = a_price / a_weight
        b_price_per_g = b_price / b_weight

        a_price_per_100g = a_price_per_g * 100
        b_price_per_100g = b_price_per_g * 100

        # --- 表示 ---
        st.markdown(
            f"<p style='font-size: 20px;'>☕ A：<b>1gあたり {a_price_per_g:.2f} 円</b>"
            f"（100gあたり {a_price_per_100g:.0f} 円）</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<p style='font-size: 20px;'>☕ B：<b>1gあたり {b_price_per_g:.2f} 円</b>"
            f"（100gあたり {b_price_per_100g:.0f} 円）</p>",
            unsafe_allow_html=True
        )

        # --- 判定 ---
        if a_price_per_g < b_price_per_g:
            diff = (b_price_per_g - a_price_per_g) * 100
            st.markdown(
                "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; "
                "font-size:22px; color:#5a4632;'>"
                f"✅ Aのコーヒーの方がお得です！<br>"
                f"（100gあたり 約{diff:.0f}円お得）"
                "</div>",
                unsafe_allow_html=True
            )

        elif b_price_per_g < a_price_per_g:
            diff = (a_price_per_g - b_price_per_g) * 100
            st.markdown(
                "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; "
                "font-size:22px; color:#5a4632;'>"
                f"✅ Bのコーヒーの方がお得です！<br>"
                f"（100gあたり 約{diff:.0f}円お得）"
                "</div>",
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                "<div style='background-color:#e7d7c1; padding:12px; border-radius:8px; "
                "font-size:22px; color:#5a4632;'>"
                "🟰 同じ価格です。"
                "</div>",
                unsafe_allow_html=True
            )
          
#st.write("")
#st.button("🔄 スタートに戻る", on_click=reset_inputs)

