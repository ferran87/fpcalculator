# 📖 Complete Guide - AB Testing False Positive Calculator

## 🚀 Quick Start

### Run Locally
```bash
pip install -r requirements.txt
streamlit run false_positive_calculator.py
```

### Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select: `YOUR_USERNAME/fpcalculator`, branch `main`, file `false_positive_calculator.py`
5. Click "Deploy!"

Your app will be live at: `https://YOUR_USERNAME-fpcalculator.streamlit.app`

---

## 🔄 Development Workflow (Staging)

### First Time Setup

**1. Create staging branch** (already done):
```bash
git checkout -b staging
git push -u origin staging
```

**2. Deploy staging app** on Streamlit Cloud:
- Branch: `staging`
- URL: `YOUR_USERNAME-fpcalculator-staging`

### Daily Workflow

**Making Changes:**
```bash
# 1. Switch to staging
git checkout staging

# 2. Make your changes, save files

# 3. Commit and push
git add .
git commit -m "Description of changes"
git push origin staging

# 4. Test on staging URL (auto-deploys in 1-2 min)
```

**Promote to Production:**
```bash
# When staging is tested and ready
git checkout main
git pull origin main
git merge staging
git push origin main
```

Or use: `promote_to_production.bat`

---

## 📊 For Product Managers

### What This Calculator Does

Helps you understand how many of your "statistically significant" metrics in AB tests are likely **false positives** (noise, not real effects).

### Key Inputs

- **Alpha (α)**: Your significance level (usually 0.05 or 0.10)
- **Beta (β)**: Type II error rate (0.20 = 80% power)
- **Number of Metrics**: How many metrics you're tracking
- **Expected Significant**: How many metrics you expect to have real effects

### Key Outputs

- **Expected False Positives**: Metrics showing significance by chance
- **Expected True Positives**: Real effects you'll detect
- **False Discovery Rate**: % of significant results that are false positives

### When to Use Bonferroni Correction

**Use it when:**
- Testing 10+ metrics
- False positives are expensive
- You're doing exploratory analysis

**Skip it when:**
- Testing 1-5 primary metrics
- You need high power
- Sample size is limited

### Best Practices

1. **Pre-register metrics** - Decide what matters before the test
2. **Limit metrics** - Focus on 3-5 key metrics
3. **Separate primary vs secondary** - Different standards
4. **Consider effect sizes** - Not just p-values
5. **Run follow-up tests** - Validate surprising results

### Common Mistakes

❌ Testing 50 metrics and only reporting significant ones  
❌ Adding metrics after seeing results  
❌ Stopping test early when something is significant  
❌ Ignoring multiple testing problem  
❌ Cherry-picking segments  

✅ Pre-register metrics before test  
✅ Report all metrics tested  
✅ Run to pre-defined sample size  
✅ Use this calculator to understand false positive risk  
✅ Validate with follow-up tests  

---

## 🛠️ Technical Details

### How It Calculates

```python
# Metrics with no real effect
null_metrics = total_metrics - expected_significant

# False positives (from null metrics)
false_positives = null_metrics × alpha

# True positives (from real effects, based on power)
true_positives = expected_significant × (1 - beta)

# Total expected significant
total_significant = false_positives + true_positives

# False discovery rate
FDR = false_positives / total_significant
```

### Bonferroni Correction

Adjusts alpha to control family-wise error rate:
```python
adjusted_alpha = alpha / number_of_metrics
```

**Trade-off:**
- ✅ Reduces false positives
- ❌ Reduces statistical power

---

## 🤝 Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch from `staging`
3. Make your changes
4. Test thoroughly
5. Submit a Pull Request to `staging`

### Code Style
- Follow PEP 8
- Use meaningful variable names
- Add comments for complex logic
- Test before submitting

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 📧 Support

- **Issues**: Open an issue on GitHub
- **Questions**: Check this guide first
- **Bugs**: Report with steps to reproduce

---

## 🎓 Learn More

### Resources
- [Multiple Testing Problem (Wikipedia)](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
- [False Discovery Rate](https://en.wikipedia.org/wiki/False_discovery_rate)
- [Evan Miller's AB Testing Tools](https://www.evanmiller.org/ab-testing/)

### Example Scenarios

**Scenario 1: Focused Test (Low Risk)**
```
Metrics: 5
Expected effects: 3
Alpha: 0.05
→ FDR: ~3% ✅
```

**Scenario 2: Dashboard Test (High Risk)**
```
Metrics: 30
Expected effects: 5
Alpha: 0.05
→ FDR: ~24% ⚠️
→ With Bonferroni: ~1% ✅
```

---

**Questions?** Open an issue or check the README!

