import streamlit as st

st.title("🎥 Microteaching Video Gallery")
st.write("This application provides curated microteaching video samples to support your growth as future English educators. You can watch real teaching demonstrations, observe different classroom strategies, and reflect on various teaching styles. Use the dropdown menus on the top left ( < ) to explore lessons.")
st.caption("This site is under construction as of June 9, 2025.")

url1 = "https://github.com/MK316/GNUEED/raw/main/images/MThome.png"
url2 = "https://github.com/MK316/GNUEED/raw/main/images/gnu.png"
url3 = "https://github.com/MK316/GNUEED/raw/main/images/qr.png"
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        f"<div style='text-align: center;'><img src='{url1}' width='250'></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='text-align: center;'><img src='{url2}' width='100'></div>",
        unsafe_allow_html=True
    )
with col2:

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(url3, width=100, use_container_width=False, caption="📱 Scan to access this page")
    st.markdown("</div>", unsafe_allow_html=True)

