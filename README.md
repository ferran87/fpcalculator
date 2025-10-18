# 📊 AB Testing False Positive Calculator

A focused Streamlit web application for Product Managers running AB tests. Calculate how many of your statistically significant metrics are likely to be **false positives** when testing multiple metrics simultaneously. Understand the multiple testing problem and see the impact of Bonferroni correction.

![False Positive Calculator](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)

## 🌟 Features

### Interactive Parameters
- **Significance Level (α)**: Set your p-value threshold with detailed explanation
- **Type II Error Rate (β)**: Configure statistical power with info popover
- **Number of Metrics**: Track how many metrics you're evaluating
- **Expected Significant Metrics**: Estimate how many real effects you expect

### Key Outputs for PMs
- **Expected False Positives**: How many significant results are likely noise
- **Expected True Positives**: How many significant results are likely real
- **False Discovery Rate**: Percentage of significant results that are false positives
- **Bonferroni Impact**: See the effect of multiple testing correction

### Rich Visualizations
- **Comparison Charts**: With vs without Bonferroni correction
- **Stacked Bar Charts**: Breakdown of true and false positives
- **Sensitivity Analysis**: How false discovery rate changes with number of metrics
- **Real-time Updates**: All calculations update instantly

### PM-Focused Insights
- Clear recommendations and best practices
- Common pitfalls to avoid
- Export functionality to CSV
- Easy-to-understand explanations of statistical concepts

## 🚀 Live Demo

**[Try the app here](https://YOUR_USERNAME-fpcalculator.streamlit.app)** *(Update with your username after deployment)*

Not deployed yet? See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for 5-minute deployment guide!

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/fpcalculator.git
cd fpcalculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run false_positive_calculator.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📊 Use Cases

### AB Testing & Experimentation
- **Product Managers**: Understand how many significant metrics are real vs noise
- **Data Scientists**: Communicate multiple testing problems to stakeholders
- **Experimentation Teams**: Decide when to apply multiple testing corrections
- **Leadership**: Make informed decisions about experiment results

### Common Scenarios
- Testing multiple metrics in a single AB test
- Evaluating significance across many user segments
- Running multiple experiments simultaneously
- Deciding which "wins" to ship to production

### Why This Matters
When you test 20 metrics at α=0.05, you'll see ~1 false positive even if nothing changed. This calculator helps you:
- Quantify the multiple testing problem
- Decide when to use Bonferroni correction
- Set realistic expectations for experiment results
- Avoid shipping changes based on noise

## 🎓 Key Insights

The app demonstrates a critical statistical concept for AB testing: **when you test multiple metrics, some will appear "significant" by random chance, even if your changes had no real effect.**

### Example Scenario
- **Metrics Tested**: 20
- **Significance Level**: α = 0.05
- **Expected Real Effects**: 5 metrics
- **Result Without Bonferroni**: 
  - Expected significant: 5.75 metrics
  - False positives: 0.75 metrics
  - **False Discovery Rate: 13%**

### Why This Matters
- **Multiple Testing Problem**: Testing many metrics inflates your false positive rate
- **P-hacking Risk**: Looking at many metrics and only reporting significant ones
- **Bonferroni Trade-off**: Reduces false positives but also reduces power
- **PM Decision**: Balance between catching real effects and avoiding false positives

This is crucial for:
- Setting realistic expectations for AB tests
- Deciding which "wins" are real vs noise
- Communicating experiment results to stakeholders
- Building a rigorous experimentation culture

## 🛠️ Technology Stack

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[Plotly](https://plotly.com/)**: Interactive visualizations
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation
- **[NumPy](https://numpy.org/)**: Numerical computations

## 📖 Understanding the Metrics

### Alpha (α) - Significance Level
The threshold for declaring a result "statistically significant." With α = 0.05, you accept a 5% chance of a false positive on each metric.

### Beta (β) - Type II Error Rate
The probability of missing a real effect. Power = 1 - β. With β = 0.20, you have 80% power to detect real effects.

### False Positives
Metrics that show statistical significance by random chance, even though there's no real effect. 
```
Expected False Positives = (Number of Null Metrics) × α
```

### True Positives
Real effects that you successfully detect based on your statistical power.
```
Expected True Positives = (Number of Real Effects) × Power
```

### False Discovery Rate (FDR)
The proportion of your significant results that are likely false positives.
```
FDR = False Positives / (False Positives + True Positives)
```

### Bonferroni Correction
Adjusts your significance level to control for multiple testing.
```
Adjusted α = α / Number of Metrics
```

## 🔄 Development Workflow

This project uses a **staging environment** for safe testing before production deployment:

- **Staging**: Test changes before going live → `staging` branch
- **Production**: Live app for users → `main` branch

### Quick Start

1. **Setup staging** (one time):
   ```bash
   # Run the setup script
   create_staging.bat
   
   # Then deploy both staging and production apps on Streamlit Cloud
   ```

2. **Daily workflow**:
   ```bash
   # Switch to staging
   switch_to_staging.bat
   
   # Make changes, test, commit
   git add .
   git commit -m "Your changes"
   git push origin staging
   
   # Test on staging URL, then promote
   promote_to_production.bat
   ```

See [WORKFLOW.md](WORKFLOW.md) for detailed workflow guide.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch from `staging`
3. Make your changes and test thoroughly
4. Push to your fork and submit a Pull Request to `staging`
5. After review and testing, changes will be promoted to `main`

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](#) file for details.

## 🙏 Acknowledgments

- Inspired by the need to better understand medical test interpretation
- Built with the amazing Streamlit framework
- Visualizations powered by Plotly

## 📧 Contact

For questions, suggestions, or feedback, please open an issue on GitHub.

## 🌐 Deploy Your Own

### Streamlit Cloud (Recommended)

1. Fork this repository
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Deploy from your forked repository
5. Share your app with the world!

### Other Deployment Options

- **Heroku**: See [Streamlit Heroku deployment guide](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud)
- **AWS**: Deploy using EC2 or ECS
- **Google Cloud**: Use Cloud Run or App Engine
- **Docker**: Use the included Dockerfile (if added)

## 📈 Roadmap

- [ ] Add more statistical distributions
- [ ] Include ROC curve visualization
- [ ] Add multi-language support
- [ ] Create API endpoint for programmatic access
- [ ] Add comparison mode for multiple tests
- [ ] Include cost-benefit analysis features

---

Made with ❤️ using Streamlit | Understanding test accuracy and false positives

