from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ab-testing-false-positive-calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Streamlit app for Product Managers to understand false positive rates in AB testing with multiple metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fpcalculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Product Managers",
        "Intended Audience :: Data Scientists",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Statistics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "fpcalculator=false_positive_calculator:main",
        ],
    },
)

