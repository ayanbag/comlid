import setuptools
import comlid
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comlid",
    version=comlid.__version__,
    author=comlid.__author__,
    author_email="ayanbag9474@gmail.com",
    description="A Command Line based Dictionary cum Translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayanbag/comlid",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_script':[
            'run_comlid = comlid.__main__:main'

        ],
    }
    
)