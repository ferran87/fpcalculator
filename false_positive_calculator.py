import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(
    page_title="False Positive Calculator",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🔬 False Positive Calculator")
st.markdown("""
This calculator helps you understand the relationship between test accuracy, disease prevalence, 
and the probability that a positive test result is truly positive (Positive Predictive Value).
""")

# Sidebar for inputs
st.sidebar.header("Test Parameters")

# Input parameters
sensitivity = st.sidebar.slider(
    "Sensitivity (True Positive Rate)",
    min_value=0.0,
    max_value=100.0,
    value=95.0,
    step=0.1,
    help="Probability that the test correctly identifies someone with the condition"
) / 100

specificity = st.sidebar.slider(
    "Specificity (True Negative Rate)",
    min_value=0.0,
    max_value=100.0,
    value=95.0,
    step=0.1,
    help="Probability that the test correctly identifies someone without the condition"
) / 100

prevalence = st.sidebar.slider(
    "Prevalence (% of population with condition)",
    min_value=0.01,
    max_value=100.0,
    value=1.0,
    step=0.01,
    help="Percentage of the population that actually has the condition"
) / 100

population_size = st.sidebar.number_input(
    "Population Size",
    min_value=100,
    max_value=1000000,
    value=10000,
    step=1000,
    help="Total number of people being tested"
)

# Calculate metrics
def calculate_metrics(sensitivity, specificity, prevalence, population_size):
    # Calculate number of people with and without condition
    people_with_condition = int(population_size * prevalence)
    people_without_condition = population_size - people_with_condition
    
    # Calculate test results
    true_positives = int(people_with_condition * sensitivity)
    false_negatives = people_with_condition - true_positives
    
    true_negatives = int(people_without_condition * specificity)
    false_positives = people_without_condition - true_negatives
    
    # Calculate derived metrics
    total_positives = true_positives + false_positives
    total_negatives = true_negatives + false_negatives
    
    # Positive Predictive Value (PPV)
    ppv = true_positives / total_positives if total_positives > 0 else 0
    
    # Negative Predictive Value (NPV)
    npv = true_negatives / total_negatives if total_negatives > 0 else 0
    
    # False Positive Rate
    false_positive_rate = 1 - specificity
    
    # False Negative Rate
    false_negative_rate = 1 - sensitivity
    
    # False Discovery Rate (FDR)
    fdr = false_positives / total_positives if total_positives > 0 else 0
    
    return {
        'people_with_condition': people_with_condition,
        'people_without_condition': people_without_condition,
        'true_positives': true_positives,
        'false_positives': false_positives,
        'true_negatives': true_negatives,
        'false_negatives': false_negatives,
        'total_positives': total_positives,
        'total_negatives': total_negatives,
        'ppv': ppv,
        'npv': npv,
        'false_positive_rate': false_positive_rate,
        'false_negative_rate': false_negative_rate,
        'fdr': fdr
    }

results = calculate_metrics(sensitivity, specificity, prevalence, population_size)

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Key Metrics")
    
    # Display key metrics in metric cards
    metric_col1, metric_col2 = st.columns(2)
    
    with metric_col1:
        st.metric(
            "Positive Predictive Value (PPV)",
            f"{results['ppv']*100:.2f}%",
            help="Probability that a positive test result is truly positive"
        )
        st.metric(
            "False Discovery Rate (FDR)",
            f"{results['fdr']*100:.2f}%",
            help="Proportion of positive results that are false positives"
        )
    
    with metric_col2:
        st.metric(
            "Negative Predictive Value (NPV)",
            f"{results['npv']*100:.2f}%",
            help="Probability that a negative test result is truly negative"
        )
        st.metric(
            "False Positive Rate",
            f"{results['false_positive_rate']*100:.2f}%",
            help="Proportion of people without condition who test positive"
        )

with col2:
    st.subheader("🎯 Confusion Matrix")
    
    # Create confusion matrix
    confusion_matrix = pd.DataFrame({
        'Condition Present': [results['true_positives'], results['false_negatives']],
        'Condition Absent': [results['false_positives'], results['true_negatives']]
    }, index=['Test Positive', 'Test Negative'])
    
    # Display as heatmap
    fig = px.imshow(
        confusion_matrix.values,
        labels=dict(x="Actual Condition", y="Test Result", color="Count"),
        x=['Condition Present', 'Condition Absent'],
        y=['Test Positive', 'Test Negative'],
        text_auto=True,
        color_continuous_scale='Blues',
        aspect="auto"
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig, width='stretch')

# Detailed breakdown
st.subheader("📈 Detailed Breakdown")

breakdown_col1, breakdown_col2, breakdown_col3, breakdown_col4 = st.columns(4)

with breakdown_col1:
    st.info(f"""
    **True Positives**  
    {results['true_positives']:,}  
    (Correctly identified as positive)
    """)

with breakdown_col2:
    st.error(f"""
    **False Positives**  
    {results['false_positives']:,}  
    (Incorrectly identified as positive)
    """)

with breakdown_col3:
    st.success(f"""
    **True Negatives**  
    {results['true_negatives']:,}  
    (Correctly identified as negative)
    """)

with breakdown_col4:
    st.warning(f"""
    **False Negatives**  
    {results['false_negatives']:,}  
    (Incorrectly identified as negative)
    """)

# Visualization of results
st.subheader("📉 Test Results Distribution")

fig = go.Figure(data=[
    go.Bar(
        name='True Positives',
        x=['Positive Tests'],
        y=[results['true_positives']],
        marker_color='lightgreen'
    ),
    go.Bar(
        name='False Positives',
        x=['Positive Tests'],
        y=[results['false_positives']],
        marker_color='lightcoral'
    ),
    go.Bar(
        name='True Negatives',
        x=['Negative Tests'],
        y=[results['true_negatives']],
        marker_color='lightblue'
    ),
    go.Bar(
        name='False Negatives',
        x=['Negative Tests'],
        y=[results['false_negatives']],
        marker_color='lightyellow'
    )
])

fig.update_layout(
    barmode='stack',
    title='Distribution of Test Results',
    xaxis_title='Test Outcome',
    yaxis_title='Number of People',
    height=400
)

st.plotly_chart(fig, width='stretch')

# Sensitivity analysis
st.subheader("🔍 Sensitivity Analysis: How Prevalence Affects PPV")

prevalence_range = np.logspace(-4, -0.3, 50)  # From 0.01% to 50%
ppv_values = []

for prev in prevalence_range:
    temp_results = calculate_metrics(sensitivity, specificity, prev, 10000)
    ppv_values.append(temp_results['ppv'] * 100)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=prevalence_range * 100,
    y=ppv_values,
    mode='lines',
    line=dict(color='blue', width=3),
    name='PPV'
))

fig.add_vline(
    x=prevalence * 100,
    line_dash="dash",
    line_color="red",
    annotation_text=f"Current: {prevalence*100:.2f}%"
)

fig.update_layout(
    title='Positive Predictive Value vs Prevalence',
    xaxis_title='Prevalence (%)',
    yaxis_title='Positive Predictive Value (%)',
    xaxis_type='log',
    height=400,
    hovermode='x unified'
)

st.plotly_chart(fig, width='stretch')

# Interpretation guide
st.subheader("📚 Interpretation Guide")

with st.expander("What do these metrics mean?"):
    st.markdown("""
    ### Key Concepts:
    
    **Sensitivity (True Positive Rate)**
    - The ability of the test to correctly identify those with the condition
    - Higher is better
    
    **Specificity (True Negative Rate)**
    - The ability of the test to correctly identify those without the condition
    - Higher is better
    
    **Prevalence**
    - The proportion of the population that actually has the condition
    - Critical factor in determining PPV
    
    **Positive Predictive Value (PPV)**
    - If you test positive, this is the probability you actually have the condition
    - **Most important metric for interpreting a positive test result**
    - Heavily influenced by prevalence
    
    **False Discovery Rate (FDR)**
    - The proportion of positive test results that are false positives
    - FDR = 1 - PPV
    
    **Key Insight:**
    Even with high sensitivity and specificity, a low prevalence can result in a surprisingly 
    low PPV, meaning many positive results are false positives!
    """)

with st.expander("Example Scenarios"):
    st.markdown("""
    ### Real-World Examples:
    
    **Rare Disease Screening (1% prevalence)**
    - Even with 95% sensitivity and 95% specificity
    - PPV might only be around 16%
    - This means 84% of positive results are false positives!
    
    **Common Condition (50% prevalence)**
    - With the same test accuracy (95%/95%)
    - PPV would be around 95%
    - Only 5% of positive results are false positives
    
    **Lesson:** Prevalence matters enormously in interpreting test results!
    """)

# Export results
st.subheader("💾 Export Results")

export_data = pd.DataFrame({
    'Metric': [
        'Sensitivity', 'Specificity', 'Prevalence', 'Population Size',
        'True Positives', 'False Positives', 'True Negatives', 'False Negatives',
        'Positive Predictive Value', 'Negative Predictive Value',
        'False Discovery Rate', 'False Positive Rate'
    ],
    'Value': [
        f"{sensitivity*100:.2f}%",
        f"{specificity*100:.2f}%",
        f"{prevalence*100:.2f}%",
        f"{population_size:,}",
        f"{results['true_positives']:,}",
        f"{results['false_positives']:,}",
        f"{results['true_negatives']:,}",
        f"{results['false_negatives']:,}",
        f"{results['ppv']*100:.2f}%",
        f"{results['npv']*100:.2f}%",
        f"{results['fdr']*100:.2f}%",
        f"{results['false_positive_rate']*100:.2f}%"
    ]
})

st.dataframe(export_data, use_container_width=True)

csv = export_data.to_csv(index=False)
st.download_button(
    label="Download Results as CSV",
    data=csv,
    file_name="false_positive_calculator_results.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ using Streamlit | Understanding test accuracy and false positives</p>
</div>
""", unsafe_allow_html=True)

