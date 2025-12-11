import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Sanem Çiçek - Veri Görselleştirme",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
    }
    .task-header {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid #667eea;
    }
    .task-header h2 {
        margin: 0;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>● Veri Görselleştirme Projesi</h1>
    <p>Sanem Çiçek tarafından hazırlanmıştır</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    import os
    csv_path = os.path.join('Ödev 2', '50_Startups.csv')
    return pd.read_csv(csv_path)

data = load_data()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Toplam Kayıt", len(data))
with col2:
    st.metric("Toplam Sütun", len(data.columns))
with col3:
    st.metric("Eyalet Sayısı", data['State'].nunique())

st.write(data.head())

st.divider()

st.markdown("""
<div class="task-header">
    <h2>→ GÖREV 1: Ar-Ge Harcaması ve Kâr Arasındaki İlişki</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("**Matplotlib Versiyonu**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x='R&D Spend', y='Profit', s=100, color='blue', ax=ax)
    ax.set_title('Ar-Ge Harcaması vs Kâr', fontsize=14, fontweight='bold')
    ax.set_xlabel('Ar-Ge Harcaması ($)', fontsize=12)
    ax.set_ylabel('Kâr ($)', fontsize=12)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.write("**Plotly Versiyonu (İnteraktif)**")
    fig_plotly = px.scatter(data, x='R&D Spend', y='Profit', 
                            color='State',
                            labels={'R&D Spend': 'Ar-Ge Harcaması ($)', 'Profit': 'Kâr ($)'},
                            hover_data=['State'],
                            title='')
    fig_plotly.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_plotly, use_container_width=True)

st.divider()

st.markdown("""
<div class="task-header">
    <h2>→ GÖREV 2: Yönetim Harcamaları ve Kâr Arasındaki İlişki</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("**Matplotlib Versiyonu**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x='Administration', y='Profit', s=100, color='green', ax=ax)
    ax.set_title('Yönetim Harcaması vs Kâr', fontsize=14, fontweight='bold')
    ax.set_xlabel('Yönetim Harcaması ($)', fontsize=12)
    ax.set_ylabel('Kâr ($)', fontsize=12)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.write("**Plotly Versiyonu (İnteraktif)**")
    fig_plotly = px.scatter(data, x='Administration', y='Profit',
                            color='State',
                            labels={'Administration': 'Yönetim Harcaması ($)', 'Profit': 'Kâr ($)'},
                            hover_data=['State'],
                            title='')
    fig_plotly.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_plotly, use_container_width=True)

st.divider()

st.markdown("""
<div class="task-header">
    <h2>→ GÖREV 3: Eyaletlere Göre Ortalama Kâr</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("**Matplotlib Versiyonu**")
    avg_profit_by_state = data.groupby('State')['Profit'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_profit_by_state.index, y=avg_profit_by_state.values, 
                palette='viridis', ax=ax)
    ax.set_title('Eyaletlere Göre Ortalama Kâr', fontsize=14, fontweight='bold')
    ax.set_xlabel('Eyalet', fontsize=12)
    ax.set_ylabel('Ortalama Kâr ($)', fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.write("**Plotly Versiyonu (İnteraktif)**")
    avg_profit_by_state = data.groupby('State')['Profit'].mean().reset_index()
    fig_plotly = px.bar(avg_profit_by_state, x='State', y='Profit', color='State',
                        labels={'State': 'Eyalet', 'Profit': 'Ortalama Kâr ($)'},
                        title='')
    fig_plotly.update_traces(text='Profit', textposition='outside')
    st.plotly_chart(fig_plotly, use_container_width=True)

st.divider()

st.markdown("""
<div class="task-header">
    <h2>→ GÖREV 4: Harcama Türlerinin Karşılaştırması</h2>
</div>
""", unsafe_allow_html=True)

spend_data = data[['R&D Spend', 'Administration', 'Marketing Spend']].melt(
    var_name='Harcama Türü', value_name='Miktar'
)

col1, col2 = st.columns(2)

with col1:
    st.write("**Matplotlib Versiyonu**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=spend_data, x='Harcama Türü', y='Miktar', 
                palette='Set2', ax=ax)
    ax.set_title('Harcama Türlerinin Dağılımı', fontsize=14, fontweight='bold')
    ax.set_xlabel('Harcama Türü', fontsize=12)
    ax.set_ylabel('Harcama ($)', fontsize=12)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.write("**Plotly Versiyonu (İnteraktif)**")
    fig_plotly = px.box(spend_data, x='Harcama Türü', y='Miktar', color='Harcama Türü',
                        labels={'Harcama Türü': 'Harcama Türü', 'Miktar': 'Miktar ($)'},
                        title='')
    st.plotly_chart(fig_plotly, use_container_width=True)

st.divider()

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <small>Hazırlayan: Sanem Çiçek | Tarih: 11 Aralık 2025</small><br><br>
    <a href='https://github.com/sanemcicek/Bitirme-projesi' target='_blank'>
    <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='30' height='30' style='margin: 0 auto;'>
    </a>
    <br>
    <small><a href='https://github.com/sanemcicek/Bitirme-projesi' target='_blank'>GitHub Repository</a></small>
</div>
""", unsafe_allow_html=True)