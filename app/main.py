import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.stats import f_oneway

# Streamlit app configuration
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title
st.title("🌞 MoonLight Energy Solutions: Solar Potential Dashboard")

# Load cleaned data
@st.cache_data
def load_data():
    base_path = "../notebooks/data/"
    benin = pd.read_csv(base_path + 'benin-malaville_clean.csv')
    sierra_leone = pd.read_csv(base_path + 'sierraleone-bumbuna_clean.csv')
    togo = pd.read_csv(base_path + 'togo-dapaong-qc_clean.csv')
    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra_leone, togo], ignore_index=True)


df = load_data()

# Sidebar: Country selection
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Countries",
    options=['Benin', 'Sierra Leone', 'Togo'],
    default=['Benin', 'Sierra Leone', 'Togo']
)

# Filter data
filtered_df = df[df['Country'].isin(countries)]

# ---- GHI, DNI, DHI Boxplots ----
st.subheader("Solar Metrics Comparison Across Countries")

for metric in ['GHI', 'DNI', 'DHI']:
    st.markdown(f"#### {metric} Distribution")
    fig = px.box(filtered_df, x='Country', y=metric, color='Country',
                 title=f"{metric} by Country", points="outliers")
    st.plotly_chart(fig, use_container_width=True)

# ---- Clean Summary Table: GHI, DNI, DHI only ----
st.subheader("📊 Summary Statistics: GHI, DNI, DHI by Country")

solar_metrics = ['GHI', 'DNI', 'DHI']

summary_stats = filtered_df.groupby('Country')[solar_metrics].agg(['mean', 'median', 'std']).round(2)

# Flatten multi-level columns
summary_stats.columns = [f"{metric}_{stat}" for metric, stat in summary_stats.columns]
summary_stats = summary_stats.reset_index()

st.dataframe(summary_stats)


# ---- Statistical Test ----
st.subheader("📈 Statistical Significance Test (ANOVA on GHI)")

if len(countries) > 1:
    ghi_groups = [filtered_df[filtered_df['Country'] == c]['GHI'] for c in countries]
    anova_result = f_oneway(*ghi_groups)
    st.markdown(f"**ANOVA p-value for GHI across selected countries:** `{anova_result.pvalue:.4e}`")
    if anova_result.pvalue < 0.05:
        st.success("The differences in GHI between countries are statistically significant.")
    else:
        st.info("No statistically significant differences in GHI across countries.")
else:
    st.warning("Select at least two countries to run ANOVA.")

# ---- Bar Chart Ranking by Average GHI ----
st.subheader("🏆 Average GHI Ranking")

avg_ghi = filtered_df.groupby('Country')['GHI'].mean().reset_index().sort_values(by='GHI', ascending=False)
fig_bar = px.bar(avg_ghi, x='Country', y='GHI', color='Country', title="Average GHI by Country")
st.plotly_chart(fig_bar, use_container_width=True)

# ---- Key Observations ----
st.markdown("### 🔍 Key Observations")
st.markdown("""
- **Togo** (example) has the highest average GHI, indicating strong solar potential.
- **Benin** shows more variability in GHI, which may suggest intermittent solar availability.
- The statistical test confirms **significant differences** in GHI across countries (if p < 0.05).
""")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by MoonLight Energy Solutions")
