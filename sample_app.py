import streamlit as st
import folium

def main():
    st.title("大阪府高槻市のマーカーをセットするアプリ")

    # 地図の初期設定（中心とズームレベル）
    map_center = [34.8567, 135.6174]  # 高槻市の緯度と経度
    zoom_level = 13
    m = folium.Map(location=map_center, zoom_start=zoom_level)

    # マーカーの追加
    st.subheader("マーカーの追加")
    location_text = st.text_input("マーカーのタイトルを入力してください", "高槻市役所")  # マーカーのタイトルを入力
    if st.button("マーカーを追加"):
        add_marker(m, 34.8462, 135.6189, location_text)  # 高槻市役所の緯度と経度を指定してマーカーを追加

    # 地図を表示
    folium_static(m)

    # HTMLファイルとしてエクスポート
    if st.button("地図をエクスポート"):
        export_map(m, "map_export.html")

def add_marker(map_obj, lat, lon, title):
    folium.Marker(location=[lat, lon], popup=title).add_to(map_obj)

def folium_static(map_obj):
    folium_static_html = map_obj._repr_html_()
    st.write(folium_static_html, unsafe_allow_html=True)

def export_map(map_obj, filename):
    map_obj.save(filename)
    st.success(f"地図を {filename} としてエクスポートしました。")

if __name__ == "__main__":
    main()
