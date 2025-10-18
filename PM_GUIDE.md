# 📊 PM Guide: Understanding False Positives in AB Testing

## 🎯 What Problem Does This Solve?

When you run an AB test and track 20 metrics, some will show "statistical significance" **just by random chance**, even if your change had zero real effect. This calculator helps you understand:

1. **How many of your "wins" are real vs noise**
2. **When to use Bonferroni correction**
3. **How to set realistic expectations**

## 🚀 Quick Start (30 seconds)

1. **Enter your experiment parameters:**
   - Alpha (usually 0.05)
   - Beta (usually 0.20 for 80% power)
   - Number of metrics you're tracking
   - How many metrics you expect to move

2. **Look at the False Discovery Rate:**
   - This tells you what % of your significant results are likely false positives
   - < 10% = Good ✅
   - 10-30% = Be cautious ⚠️
   - > 30% = High risk of false positives ❌

3. **Toggle Bonferroni correction:**
   - See how it reduces false positives
   - But also reduces your power to detect real effects

## 💡 Real-World Example

### Scenario: New Checkout Flow
You're testing a new checkout flow and tracking:
- Conversion rate (primary metric)
- Average order value
- Time to checkout
- Cart abandonment rate
- Return rate
- Customer satisfaction
- Mobile conversion
- Desktop conversion
- ... 20 metrics total

You expect 3-5 metrics to actually improve.

### Without This Tool:
❌ You see 6 metrics hit significance (p < 0.05)
❌ You celebrate and ship the change
❌ But 1-2 of those "wins" were probably just noise
❌ You might be shipping a change that doesn't actually work

### With This Tool:
✅ Input: 20 metrics, expect 5 real effects, α=0.05
✅ Calculator shows: ~1 false positive expected
✅ You see 6 significant metrics
✅ You know ~1 is likely noise
✅ You focus on the strongest signals or run a follow-up test

## 📖 Key Concepts Explained Simply

### Alpha (α) - Your Significance Level
**What it is:** The bar you set for calling something "significant"
**Default:** 0.05 (5%)
**What it means:** "I'm okay with a 5% chance of a false positive on each metric"

**PM Translation:** 
- α = 0.05 → If you test 20 metrics with no real effects, you'll see ~1 false positive
- Lower α (0.01) → Fewer false positives, but might miss real effects
- Higher α (0.10) → Catch more real effects, but more false positives

### Beta (β) - Type II Error Rate
**What it is:** Your chance of missing a real effect
**Default:** 0.20 (which means 80% power)
**What it means:** "If there IS a real effect, I have an 80% chance of catching it"

**PM Translation:**
- β = 0.20 → 80% power → You'll catch 4 out of 5 real effects
- Lower β (0.10) → 90% power → Better, but requires more sample size
- Higher β (0.30) → 70% power → Cheaper/faster, but might miss effects

### False Discovery Rate (FDR)
**What it is:** Of your significant results, what % are false positives
**Target:** < 10% is good, < 5% is great

**PM Translation:**
- FDR = 20% → 1 in 5 of your "wins" is probably noise
- FDR = 50% → Half your "wins" are probably noise
- FDR = 5% → Very confident in your significant results

### Bonferroni Correction
**What it is:** Divides your alpha by the number of metrics
**Example:** α = 0.05, 20 metrics → Bonferroni α = 0.0025

**PM Translation:**
- ✅ Dramatically reduces false positives
- ❌ Also reduces power (might miss real effects)
- 💡 Use when: Testing many metrics and false positives are costly
- 💡 Skip when: Few metrics or need to catch every possible effect

## 🎯 When to Use Bonferroni

### Use Bonferroni When:
✅ Testing 10+ metrics
✅ False positives are expensive (engineering time, user confusion)
✅ You're doing exploratory analysis
✅ Results will be used for major decisions
✅ You can afford to miss some smaller effects

### Skip Bonferroni When:
❌ Testing 1-3 primary metrics
❌ You pre-registered your metrics
❌ You need high power to detect effects
❌ You'll run follow-up tests anyway
❌ Sample size is limited

## 📊 Rule of Thumb Guidelines

### Number of Metrics
- **1-5 metrics:** Low risk, probably don't need Bonferroni
- **5-20 metrics:** Moderate risk, consider Bonferroni for secondary metrics
- **20+ metrics:** High risk, strongly consider Bonferroni or reduce metrics

### Expected Effects
- **Many expected effects (>50% of metrics):** Lower FDR, less need for correction
- **Few expected effects (<25% of metrics):** Higher FDR, more need for correction
- **No expected effects (guardrail metrics):** Very high FDR, definitely use correction

### False Discovery Rate
- **< 10%:** Good! Your significant results are mostly real
- **10-20%:** Okay, but be cautious. Consider follow-up tests
- **20-30%:** Risky. Many "wins" might be noise
- **> 30%:** Very risky. Use Bonferroni or reduce metrics

## 🛠️ Practical Workflows

### Workflow 1: Primary + Secondary Metrics
```
Primary Metrics (3-5):
- Don't apply Bonferroni
- These are your key metrics, pre-registered
- Accept standard α = 0.05

Secondary Metrics (10-20):
- Apply Bonferroni
- These are exploratory
- Use adjusted α to control false positives
```

### Workflow 2: Tiered Approach
```
Tier 1 (Must-move metrics): α = 0.05, no correction
Tier 2 (Should-move metrics): α = 0.01, no correction  
Tier 3 (Nice-to-move metrics): α = 0.05, with Bonferroni
```

### Workflow 3: Sequential Testing
```
1. Run test with all metrics
2. See which are significant
3. Use this calculator to estimate false positives
4. Run follow-up test on significant metrics only
5. Only ship if significant in both tests
```

## ⚠️ Common Mistakes PMs Make

### 1. Testing Everything
❌ **Mistake:** Track 50 metrics "just in case"
✅ **Better:** Pick 5-10 key metrics before the test

### 2. P-Hacking
❌ **Mistake:** Test 20 metrics, only report the 3 significant ones
✅ **Better:** Pre-register your metrics, report all results

### 3. Ignoring Multiple Testing
❌ **Mistake:** "We got 5 significant results!" (out of 30 metrics tested)
✅ **Better:** "We tested 30 metrics, expected ~1.5 false positives, got 5 significant"

### 4. Stopping Early
❌ **Mistake:** Check results daily, stop when significant
✅ **Better:** Pre-define sample size, run to completion

### 5. Segment Fishing
❌ **Mistake:** "Not significant overall, but significant for iOS users aged 25-34!"
✅ **Better:** Pre-register segments, or treat as exploratory

### 6. Changing Metrics Mid-Test
❌ **Mistake:** Add new metrics after seeing results
✅ **Better:** Lock metrics before test starts

## 💪 Best Practices

### Before the Test
1. **Pre-register your metrics** - Decide what matters before you see data
2. **Separate primary vs secondary** - Different standards for different tiers
3. **Set sample size** - Don't peek and stop early
4. **Define success criteria** - What would make you ship?

### During the Test
5. **Don't peek** - Or if you do, don't stop early based on significance
6. **Monitor guardrails** - But don't count them in your multiple testing
7. **Document everything** - What you're testing and why

### After the Test
8. **Use this calculator** - Understand your false positive risk
9. **Consider effect sizes** - Not just p-values
10. **Run follow-up tests** - Validate surprising results
11. **Be honest about results** - Report all metrics tested, not just significant ones

## 📈 Example Calculations

### Example 1: Focused Test
```
Metrics: 5
Expected effects: 3
Alpha: 0.05
Beta: 0.20

Result:
- Expected significant: 3.5
- False positives: 0.1
- FDR: 3%

Interpretation: Very low false positive risk ✅
```

### Example 2: Dashboard Test
```
Metrics: 30
Expected effects: 5
Alpha: 0.05
Beta: 0.20

Result:
- Expected significant: 5.25
- False positives: 1.25
- FDR: 24%

Interpretation: ~1 in 4 "wins" is noise ⚠️
Consider Bonferroni!
```

### Example 3: With Bonferroni
```
Same as Example 2, but with Bonferroni:

Result:
- Adjusted alpha: 0.0017
- Expected significant: 4.04
- False positives: 0.04
- FDR: 1%

Interpretation: Much lower false positives ✅
But also detecting fewer real effects (4 vs 5)
```

## 🎓 Learning Resources

### For PMs
- [Evan Miller's AB Testing Tools](https://www.evanmiller.org/ab-testing/)
- [Optimizely's Stats Engine](https://www.optimizely.com/optimization-glossary/statistical-significance/)

### For Data Scientists
- [Multiple Comparisons Problem (Wikipedia)](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
- [False Discovery Rate (Benjamini-Hochberg)](https://en.wikipedia.org/wiki/False_discovery_rate)

## 🤝 Working with Data Scientists

### Questions to Ask Your DS Team
1. "How many metrics are we testing?"
2. "What's our expected false discovery rate?"
3. "Should we use multiple testing correction?"
4. "How many of these significant results are likely real?"
5. "What's our statistical power?"

### Information to Provide
1. Which metrics are primary vs exploratory
2. What effect sizes matter for business
3. Cost of false positives vs false negatives
4. Whether you'll run follow-up tests

## 📞 Need Help?

- Use the calculator to run scenarios
- Consult with your data science team
- When in doubt, be conservative (use Bonferroni)
- Consider follow-up tests for surprising results

---

**Remember:** Statistical significance ≠ Real effect. Always consider:
- Effect size (how big is the change?)
- Business impact (does it matter?)
- Confidence (how many metrics did we test?)
- Replication (can we reproduce it?)

Happy testing! 📊

