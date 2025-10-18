import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AB Testing False Positive Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("📊 AB Testing False Positive Calculator")
st.markdown("""
Calculate how many of your statistically significant metrics are likely to be **false positives** 
when running AB tests with multiple metrics.
""")

# Sidebar for inputs
st.sidebar.header("Experiment Parameters")

# Alpha input with info
col1, col2 = st.sidebar.columns([3, 1])
with col1:
    alpha = st.number_input(
        "Significance Level (α)",
        min_value=0.001,
        max_value=0.20,
        value=0.05,
        step=0.001,
        format="%.3f"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.popover("ℹ️"):
        st.markdown("""
        **What is Alpha (α)?**
        
        Alpha is your **significance level** - the threshold for declaring a result "statistically significant."
        
        - **α = 0.05** means you accept a 5% chance of a false positive on each individual metric
        - Common values: 0.05, 0.01, 0.10
        - Lower α = more conservative (fewer false positives, but might miss real effects)
        
        **Example:** With α = 0.05, if there's truly no effect, you'll still see a "significant" result 5% of the time by random chance.
        """)

# Beta input with info
col1, col2 = st.sidebar.columns([3, 1])
with col1:
    beta = st.number_input(
        "Type II Error Rate (β)",
        min_value=0.05,
        max_value=0.50,
        value=0.20,
        step=0.01,
        format="%.2f"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.popover("ℹ️"):
        st.markdown("""
        **What is Beta (β)?**
        
        Beta is your **Type II error rate** - the probability of missing a real effect.
        
        - **β = 0.20** means 20% chance of missing a real effect (80% power)
        - **Power = 1 - β** (e.g., β = 0.20 → 80% power)
        - Common values: 0.20 (80% power), 0.10 (90% power)
        
        **Example:** With β = 0.20, if there IS a real effect, you have an 80% chance of detecting it.
        
        **Note:** This affects how many true positives you expect, which influences the false positive rate among your significant results.
        """)

power = 1 - beta
st.sidebar.metric("Statistical Power", f"{power*100:.0f}%")

st.sidebar.markdown("---")

# Number of metrics
num_metrics = st.sidebar.number_input(
    "Number of Metrics Evaluated",
    min_value=1,
    max_value=1000,
    value=20,
    step=1,
    help="Total number of metrics you're tracking in your AB test"
)

# Expected significant metrics
expected_significant = st.sidebar.number_input(
    "Expected Significant Metrics",
    min_value=0,
    max_value=num_metrics,
    value=5,
    step=1,
    help="How many metrics do you expect to show a real effect?"
)

st.sidebar.markdown("---")

# Bonferroni correction toggle
apply_bonferroni = st.sidebar.checkbox(
    "Apply Bonferroni Correction",
    value=False,
    help="Adjusts significance level to account for multiple comparisons"
)

with st.sidebar.expander("ℹ️ What is Bonferroni Correction?"):
    st.markdown("""
    **Bonferroni Correction** is a method to control false positives when testing multiple metrics.
    
    **How it works:**
    - Divides your alpha by the number of metrics
    - Adjusted α = α / number of metrics
    - Makes each individual test more conservative
    
    **Example:**
    - Original α = 0.05, testing 20 metrics
    - Bonferroni α = 0.05 / 20 = 0.0025
    
    **Trade-off:**
    - ✅ Reduces false positives
    - ❌ Reduces power (might miss real effects)
    - ⚠️ Can be too conservative with many metrics
    """)

# Calculate metrics
def calculate_false_positives(alpha, beta, num_metrics, expected_significant, apply_bonferroni):
    """
    Calculate expected false positives in AB testing with multiple metrics.
    
    Logic:
    - Metrics with real effects: expected_significant
    - Metrics with no real effect: num_metrics - expected_significant
    - False positives come from metrics with no real effect that show significance by chance
    - True positives come from metrics with real effects that we detect (based on power)
    """
    
    # Adjust alpha if Bonferroni correction is applied
    if apply_bonferroni and num_metrics > 0:
        adjusted_alpha = alpha / num_metrics
    else:
        adjusted_alpha = alpha
    
    # Metrics with no real effect
    null_metrics = num_metrics - expected_significant
    
    # Expected false positives (from null metrics showing significance by chance)
    expected_false_positives = null_metrics * adjusted_alpha
    
    # Expected true positives (from real effects we detect, based on power)
    power = 1 - beta
    expected_true_positives = expected_significant * power
    
    # Total expected significant results
    total_expected_significant = expected_false_positives + expected_true_positives
    
    # False discovery rate (proportion of significant results that are false positives)
    if total_expected_significant > 0:
        false_discovery_rate = expected_false_positives / total_expected_significant
    else:
        false_discovery_rate = 0
    
    return {
        'adjusted_alpha': adjusted_alpha,
        'null_metrics': null_metrics,
        'expected_false_positives': expected_false_positives,
        'expected_true_positives': expected_true_positives,
        'total_expected_significant': total_expected_significant,
        'false_discovery_rate': false_discovery_rate,
        'power': power
    }

# Calculate for both scenarios
results_without = calculate_false_positives(alpha, beta, num_metrics, expected_significant, False)
results_with = calculate_false_positives(alpha, beta, num_metrics, expected_significant, True)

# Use the selected results
results = results_with if apply_bonferroni else results_without

# Main content
st.markdown("---")

# Key Results - Large and prominent
st.subheader("🎯 Key Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Expected Significant Metrics",
        f"{results['total_expected_significant']:.1f}",
        help="Total metrics expected to show statistical significance"
    )

with col2:
    st.metric(
        "Expected False Positives",
        f"{results['expected_false_positives']:.1f}",
        delta=f"{results['expected_false_positives']/num_metrics*100:.1f}% of all metrics",
        delta_color="inverse",
        help="Metrics showing significance by random chance (no real effect)"
    )

with col3:
    st.metric(
        "Expected True Positives",
        f"{results['expected_true_positives']:.1f}",
        help="Real effects that you'll detect"
    )

with col4:
    st.metric(
        "False Discovery Rate",
        f"{results['false_discovery_rate']*100:.1f}%",
        delta="of significant results",
        delta_color="off",
        help="Proportion of your significant results that are likely false positives"
    )

# Warning if FDR is high
if results['false_discovery_rate'] > 0.3:
    st.error(f"""
    ⚠️ **High False Discovery Rate!** 
    
    {results['false_discovery_rate']*100:.0f}% of your significant metrics are likely to be false positives. 
    Consider applying Bonferroni correction or reducing the number of metrics.
    """)
elif results['false_discovery_rate'] > 0.15:
    st.warning(f"""
    ⚠️ **Moderate False Discovery Rate** 
    
    {results['false_discovery_rate']*100:.0f}% of your significant metrics are likely to be false positives. 
    Be cautious when interpreting results.
    """)
else:
    st.success(f"""
    ✅ **Good False Discovery Rate** 
    
    Only {results['false_discovery_rate']*100:.0f}% of your significant metrics are likely to be false positives.
    """)

st.markdown("---")

# Comparison section
st.subheader("🔄 With vs Without Bonferroni Correction")

comparison_data = pd.DataFrame({
    'Metric': [
        'Adjusted Alpha (α)',
        'Expected False Positives',
        'Expected True Positives',
        'Total Significant Metrics',
        'False Discovery Rate'
    ],
    'Without Bonferroni': [
        f"{results_without['adjusted_alpha']:.4f}",
        f"{results_without['expected_false_positives']:.2f}",
        f"{results_without['expected_true_positives']:.2f}",
        f"{results_without['total_expected_significant']:.2f}",
        f"{results_without['false_discovery_rate']*100:.1f}%"
    ],
    'With Bonferroni': [
        f"{results_with['adjusted_alpha']:.4f}",
        f"{results_with['expected_false_positives']:.2f}",
        f"{results_with['expected_true_positives']:.2f}",
        f"{results_with['total_expected_significant']:.2f}",
        f"{results_with['false_discovery_rate']*100:.1f}%"
    ]
})

st.dataframe(comparison_data, use_container_width=True, hide_index=True)

# Visualization
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Breakdown of Significant Results")
    
    # Create stacked bar chart
    fig = go.Figure()
    
    scenarios = ['Without<br>Bonferroni', 'With<br>Bonferroni']
    false_pos = [results_without['expected_false_positives'], results_with['expected_false_positives']]
    true_pos = [results_without['expected_true_positives'], results_with['expected_true_positives']]
    
    fig.add_trace(go.Bar(
        name='False Positives',
        x=scenarios,
        y=false_pos,
        marker_color='#FF6B6B',
        text=[f"{fp:.1f}" for fp in false_pos],
        textposition='inside'
    ))
    
    fig.add_trace(go.Bar(
        name='True Positives',
        x=scenarios,
        y=true_pos,
        marker_color='#51CF66',
        text=[f"{tp:.1f}" for tp in true_pos],
        textposition='inside'
    ))
    
    fig.update_layout(
        barmode='stack',
        yaxis_title='Expected Significant Metrics',
        showlegend=True,
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📈 False Discovery Rate Comparison")
    
    # Create FDR comparison
    fig2 = go.Figure()
    
    fig2.add_trace(go.Bar(
        x=scenarios,
        y=[results_without['false_discovery_rate']*100, results_with['false_discovery_rate']*100],
        marker_color=['#FF6B6B', '#4DABF7'],
        text=[f"{results_without['false_discovery_rate']*100:.1f}%", 
              f"{results_with['false_discovery_rate']*100:.1f}%"],
        textposition='outside'
    ))
    
    fig2.update_layout(
        yaxis_title='False Discovery Rate (%)',
        showlegend=False,
        height=400,
        yaxis_range=[0, max(results_without['false_discovery_rate']*100, results_with['false_discovery_rate']*100) * 1.2]
    )
    
    st.plotly_chart(fig2, use_container_width=True)

# Detailed breakdown
st.markdown("---")
st.subheader("📋 Detailed Breakdown")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Your Experiment")
    st.markdown(f"""
    - **Total Metrics Tracked:** {num_metrics}
    - **Metrics with Real Effects:** {expected_significant}
    - **Metrics with No Real Effect:** {results['null_metrics']}
    - **Significance Level:** α = {alpha}
    - **Statistical Power:** {results['power']*100:.0f}%
    - **Bonferroni Correction:** {'✅ Applied' if apply_bonferroni else '❌ Not Applied'}
    """)
    
    if apply_bonferroni:
        st.markdown(f"""
        - **Adjusted Alpha:** {results['adjusted_alpha']:.4f} (α / {num_metrics})
        """)

with col2:
    st.markdown("### What This Means")
    st.markdown(f"""
    Out of **{results['total_expected_significant']:.1f}** metrics showing statistical significance:
    
    - **{results['expected_true_positives']:.1f}** are likely **real effects** ✅
    - **{results['expected_false_positives']:.1f}** are likely **false positives** ❌
    
    **Bottom Line:** {results['false_discovery_rate']*100:.0f}% of your "significant" 
    results are probably just noise.
    """)

# Sensitivity Analysis
st.markdown("---")
st.subheader("🔍 Sensitivity Analysis: Impact of Number of Metrics")

# Generate data for different numbers of metrics
metric_range = np.linspace(1, min(200, num_metrics * 3), 50).astype(int)
fdr_without_bonf = []
fdr_with_bonf = []

for n_metrics in metric_range:
    # Scale expected significant proportionally
    scaled_expected = int(expected_significant * n_metrics / num_metrics)
    
    res_without = calculate_false_positives(alpha, beta, n_metrics, scaled_expected, False)
    res_with = calculate_false_positives(alpha, beta, n_metrics, scaled_expected, True)
    
    fdr_without_bonf.append(res_without['false_discovery_rate'] * 100)
    fdr_with_bonf.append(res_with['false_discovery_rate'] * 100)

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=metric_range,
    y=fdr_without_bonf,
    mode='lines',
    name='Without Bonferroni',
    line=dict(color='#FF6B6B', width=3)
))

fig3.add_trace(go.Scatter(
    x=metric_range,
    y=fdr_with_bonf,
    mode='lines',
    name='With Bonferroni',
    line=dict(color='#4DABF7', width=3)
))

# Add current position
fig3.add_vline(
    x=num_metrics,
    line_dash="dash",
    line_color="gray",
    annotation_text=f"Current: {num_metrics} metrics"
)

fig3.update_layout(
    title='How False Discovery Rate Changes with Number of Metrics',
    xaxis_title='Number of Metrics',
    yaxis_title='False Discovery Rate (%)',
    height=400,
    hovermode='x unified',
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

st.plotly_chart(fig3, use_container_width=True)

# Recommendations
st.markdown("---")
st.subheader("💡 Recommendations for PMs")

rec_col1, rec_col2 = st.columns(2)

with rec_col1:
    st.markdown("### ✅ Best Practices")
    st.markdown("""
    1. **Limit your metrics** - Focus on 3-5 key metrics instead of tracking everything
    2. **Pre-register your metrics** - Decide which metrics matter before running the test
    3. **Use primary vs secondary metrics** - Only apply strict significance to primary metrics
    4. **Consider Bonferroni** - Especially when testing many metrics
    5. **Increase sample size** - Higher power reduces false discovery rate
    6. **Replicate findings** - Test significant results in follow-up experiments
    """)

with rec_col2:
    st.markdown("### ⚠️ Common Pitfalls")
    st.markdown("""
    1. **P-hacking** - Testing many metrics and only reporting significant ones
    2. **Ignoring multiple testing** - Not accounting for testing many metrics
    3. **Over-interpreting noise** - Treating all significant results as real
    4. **Stopping tests early** - Peeking at results and stopping when significant
    5. **Cherry-picking segments** - Testing many segments and reporting the significant ones
    6. **Changing metrics mid-test** - Adding metrics after seeing results
    """)

# Export functionality
st.markdown("---")
st.subheader("💾 Export Results")

export_data = pd.DataFrame({
    'Parameter': [
        'Significance Level (α)',
        'Type II Error Rate (β)',
        'Statistical Power',
        'Number of Metrics',
        'Expected Significant Metrics',
        'Bonferroni Correction',
        '',
        'Adjusted Alpha',
        'Expected False Positives',
        'Expected True Positives',
        'Total Expected Significant',
        'False Discovery Rate'
    ],
    'Value': [
        f"{alpha}",
        f"{beta}",
        f"{results['power']*100:.1f}%",
        f"{num_metrics}",
        f"{expected_significant}",
        'Yes' if apply_bonferroni else 'No',
        '',
        f"{results['adjusted_alpha']:.6f}",
        f"{results['expected_false_positives']:.2f}",
        f"{results['expected_true_positives']:.2f}",
        f"{results['total_expected_significant']:.2f}",
        f"{results['false_discovery_rate']*100:.1f}%"
    ]
})

csv = export_data.to_csv(index=False)
st.download_button(
    label="📥 Download Results as CSV",
    data=csv,
    file_name="ab_test_false_positive_analysis.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>AB Testing False Positive Calculator</strong> | Help PMs understand multiple testing problems</p>
    <p>Remember: Not all statistically significant results are real effects! 📊</p>
</div>
""", unsafe_allow_html=True)
