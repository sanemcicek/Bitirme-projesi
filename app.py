import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sanem Çiçek - Veri Görselleştirme", layout="wide")

st.title("Sanem Çiçek İçin Hazırlanmış Veri Görselleştirme")

data = pd.read_csv('Ödev 2/50_Startups.csv')

st.divider()

st.subheader("GÖREV 1: Ar-Ge Harcaması ve Kâr Arasındaki İlişki")
col1, col2 = st.columns(2)
with col1:
    st.write("Dağılım grafiği (Scatter Plot) ile Ar-Ge harcamaları ile kâr arasındaki ilişki")
    fig1 = px.scatter(data, x='R&D Spend', y='Profit', color='State', 
                      title='',
                      labels={'R&D Spend': 'Ar-Ge Harcaması ($)', 'Profit': 'Kâr ($)'})
    st.plotly_chart(fig1, use_container_width=True)

st.divider()

st.subheader("GÖREV 2: Yönetim Harcamaları ve Kâr Arasındaki İlişki")
col1, col2 = st.columns(2)
with col1:
    st.write("Dağılım grafiği (Scatter Plot) ile Yönetim harcamaları ile kâr arasındaki ilişki")
    fig2 = px.scatter(data, x='Administration', y='Profit', color='State',
                      title='',
                      labels={'Administration': 'Yönetim Harcaması ($)', 'Profit': 'Kâr ($)'})
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("GÖREV 3: Eyaletlere Göre Ortalama Kâr")
col1, col2 = st.columns(2)
with col1:
    st.write("Çubuk grafik (Bar Chart) ile farklı eyaletlerdeki startup'ların ortalama kârlarının karşılaştırması")
    avg_profit_by_state = data.groupby('State')['Profit'].mean().reset_index()
    fig3 = px.bar(avg_profit_by_state, x='State', y='Profit', color='State',
                  title='',
                  labels={'State': 'Eyalet', 'Profit': 'Ortalama Kâr ($)'})
    fig3.update_traces(text='Profit', textposition='outside')
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("GÖREV 4: Harcama Türlerinin Karşılaştırması")
col1, col2 = st.columns(2)
with col1:
    st.write("Kutu grafik (Boxplot) ile Ar-Ge, Yönetim ve Pazarlama harcamalarının dağılımı")
    spend_data = data[['R&D Spend', 'Administration', 'Marketing Spend']].melt(
        var_name='Harcama Türü', value_name='Miktar'
    )
    fig4 = px.box(spend_data, x='Harcama Türü', y='Miktar', color='Harcama Türü',
                  title='',
                  labels={'Harcama Türü': 'Harcama Türü', 'Miktar': 'Miktar ($)'})
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("""
    <div align='center'>
    <small>Hazırlayan: Sanem Çiçek | Tarih: 11 Aralık 2025</small><br><br>
    <a href='https://github.com/sanemcicek' target='_blank'>
    <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='30' height='30' style='margin: 0 auto;'>
    </a>
    </div>
    """, unsafe_allow_html=True)