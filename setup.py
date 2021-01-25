import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matthieumarshall-sentiment-analyst",
    version="0.0.1",
    author="Matthieu Marshall",
    description="A package that will analyse the sentiment of some tweets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthieumarshall/sentiment_analyst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
