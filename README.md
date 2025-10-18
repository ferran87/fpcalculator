# 🔬 False Positive Calculator

A comprehensive Streamlit web application for understanding the relationship between test accuracy, disease prevalence, and false positive rates. This tool helps visualize how even highly accurate tests can produce surprising numbers of false positives when screening for rare conditions.

![False Positive Calculator](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)

## 🌟 Features

### Interactive Parameters
- **Sensitivity**: Adjust the true positive rate (0-100%)
- **Specificity**: Adjust the true negative rate (0-100%)
- **Prevalence**: Set the disease/condition prevalence in the population
- **Population Size**: Define the total number of people being tested

### Comprehensive Metrics
- **Positive Predictive Value (PPV)**: Probability that a positive test is truly positive
- **Negative Predictive Value (NPV)**: Probability that a negative test is truly negative
- **False Discovery Rate (FDR)**: Proportion of positive results that are false positives
- **False Positive Rate**: Proportion of healthy people who test positive

### Rich Visualizations
- **Confusion Matrix Heatmap**: Visual representation of test outcomes
- **Stacked Bar Charts**: Distribution of true/false positives and negatives
- **Sensitivity Analysis**: Interactive chart showing how prevalence affects PPV
- **Real-time Updates**: All visualizations update instantly as you adjust parameters

### Educational Content
- Detailed interpretation guides
- Real-world example scenarios
- Export functionality to CSV
- Mathematical explanations of key concepts

## 🚀 Live Demo

[Try the app here](#) *(Add your deployed URL)*

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

### Medical Testing
- Understanding screening test results
- Evaluating diagnostic test performance
- Making informed decisions about mass screening programs

### Security & Fraud Detection
- Analyzing false alarm rates in security systems
- Optimizing fraud detection thresholds
- Balancing sensitivity vs. specificity in threat detection

### Quality Control
- Manufacturing defect detection
- Product testing and validation
- Statistical process control

### Research & Education
- Teaching Bayesian statistics
- Demonstrating the base rate fallacy
- Understanding conditional probability

## 🎓 Key Insights

The app demonstrates a critical statistical concept: **even with highly accurate tests (e.g., 95% sensitivity and 95% specificity), if the condition being tested is rare (low prevalence), the majority of positive results can be false positives.**

### Example Scenario
- **Test Accuracy**: 95% sensitivity, 95% specificity
- **Prevalence**: 1% (rare condition)
- **Result**: Only ~16% of positive tests are true positives
- **Implication**: 84% of positive results are false positives!

This phenomenon is crucial for understanding:
- Why confirmatory testing is important
- The limitations of mass screening programs
- How to interpret medical test results
- The importance of considering base rates (prevalence)

## 🛠️ Technology Stack

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[Plotly](https://plotly.com/)**: Interactive visualizations
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation
- **[NumPy](https://numpy.org/)**: Numerical computations

## 📖 Understanding the Metrics

### Sensitivity (True Positive Rate)
The probability that the test correctly identifies someone with the condition.
```
Sensitivity = True Positives / (True Positives + False Negatives)
```

### Specificity (True Negative Rate)
The probability that the test correctly identifies someone without the condition.
```
Specificity = True Negatives / (True Negatives + False Positives)
```

### Positive Predictive Value (PPV)
The probability that someone with a positive test actually has the condition.
```
PPV = True Positives / (True Positives + False Positives)
```

### False Discovery Rate (FDR)
The proportion of positive test results that are false positives.
```
FDR = False Positives / (True Positives + False Positives) = 1 - PPV
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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

