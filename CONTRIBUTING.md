# Contributing to False Positive Calculator

Thank you for your interest in contributing to the False Positive Calculator! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, browser)

### Suggesting Enhancements

We welcome suggestions for new features or improvements! Please create an issue with:
- A clear description of the enhancement
- Why this enhancement would be useful
- Any relevant examples or mockups

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, descriptive commit messages
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description of your changes

### Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular

### Testing

Before submitting a pull request:
- Test the app locally with `streamlit run false_positive_calculator.py`
- Verify all visualizations render correctly
- Test with various parameter combinations
- Ensure no errors in the browser console

### Commit Messages

Use clear and meaningful commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when relevant

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/yourusername/fpcalculator.git
cd fpcalculator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run false_positive_calculator.py
```

## Questions?

Feel free to open an issue for any questions about contributing!

Thank you for helping make this project better! 🙏

