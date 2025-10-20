# 📊 AB Testing False Positive Calculator

Calculate how many of your "statistically significant" metrics in AB tests are likely **false positives** when testing multiple metrics.

[![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

## 🎯 What It Does

When you run an AB test tracking 20 metrics, some will show "statistical significance" just by random chance. This calculator helps you:

- **Quantify false positives**: How many "wins" are likely noise
- **Understand the multiple testing problem**: Why testing many metrics inflates false positives
- **Evaluate Bonferroni correction**: See the trade-off between false positives and statistical power
- **Make better decisions**: Ship changes based on real effects, not noise

## 🚀 Quick Start

### Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/fpcalculator.git
cd fpcalculator
pip install -r requirements.txt
streamlit run false_positive_calculator.py
```

### Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app" → Select this repo → Deploy
4. Your app is live! 🎉

## 📊 Example

**Your AB Test:**
- Testing 20 metrics
- Expecting 5 real effects
- Using α = 0.05, β = 0.20 (80% power)

**Without Bonferroni:**
- Expected significant: 4.75 metrics
- False positives: 0.75 (16% false discovery rate)

**With Bonferroni:**
- Expected significant: 4.04 metrics  
- False positives: 0.04 (1% false discovery rate)

**Insight:** ~1 in 6 of your "wins" is probably noise without correction!

## 🌟 Features

- **Interactive inputs** with explanations for alpha, beta, and power
- **Real-time calculations** of false positives and false discovery rate
- **Bonferroni toggle** to see the impact of multiple testing correction
- **Visualizations** comparing corrected vs uncorrected results
- **Sensitivity analysis** showing how FDR changes with number of metrics
- **PM-friendly** explanations and best practices
- **Export to CSV** for reporting

## 📚 Documentation

- **[GUIDE.md](GUIDE.md)** - Complete guide (deployment, workflow, technical details)
- **[PM_GUIDE.md](PM_GUIDE.md)** - In-depth guide for Product Managers
- **[LICENSE](LICENSE)** - MIT License

## 🔄 Development Workflow

We use a staging/production workflow:

**Make changes:**
```bash
git checkout staging
# make your changes
git add .
git commit -m "Description"
git push origin staging
# test on staging URL
```

**Deploy to production:**
```bash
git checkout main
git merge staging
git push origin main
```

Or use the helper scripts: `push_to_staging.bat` and `promote_to_production.bat`

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch from `staging`
3. Make your changes
4. Submit a PR to `staging`

See [GUIDE.md](GUIDE.md) for details.

## 💡 For Product Managers

### When to Use This Calculator

- Before running AB tests with many metrics
- After getting results to understand false positive risk
- When deciding whether to use Bonferroni correction
- When communicating experiment results to stakeholders

### Key Insights

1. **Multiple testing problem**: Testing 20 metrics at α=0.05 gives you ~1 false positive even if nothing changed
2. **False discovery rate**: The % of your significant results that are false positives
3. **Bonferroni trade-off**: Reduces false positives but also reduces power
4. **Pre-registration helps**: Decide which metrics matter before running the test

### Best Practices

✅ Limit to 3-5 key metrics  
✅ Pre-register metrics before test  
✅ Use primary vs secondary tiers  
✅ Consider Bonferroni for 10+ metrics  
✅ Validate surprising results  

❌ Don't test 50 metrics and cherry-pick  
❌ Don't add metrics after seeing results  
❌ Don't ignore multiple testing  
❌ Don't stop early when significant  

## 📖 Learn More

- [Multiple Testing Problem](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
- [False Discovery Rate](https://en.wikipedia.org/wiki/False_discovery_rate)
- [Evan Miller's AB Testing Guide](https://www.evanmiller.org/ab-testing/)

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

Built for Product Managers and Data Scientists running AB tests. Inspired by the need to better understand and communicate the multiple testing problem.

---

**Made with ❤️ using Streamlit** | Help PMs ship real effects, not noise! 📊
