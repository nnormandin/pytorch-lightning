#!/usr/bin/env python

from setuptools import setup, find_packages

# https://packaging.python.org/guides/single-sourcing-package-version/

# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="pytorch-lightning",
    version='0.1.dev13',
    description="The Keras for ML researchers using PyTorch",
    author="William Falcon",
    author_email="waf2107@columbia.edu",
    url="https://github.com/williamFalcon/pytorch-lightning",
    download_url="https://github.com/williamFalcon/pytorch-lightning",
    license="MIT",
    keywords=["deep learning", "pytorch", "AI"],
    python_requires=">=3.5",
    install_requires=[
        "torch",
        "tqdm",
        "test-tube",
    ],
    packages=find_packages(),
    long_description=open("README.md", encoding="utf-8").read(),
    include_package_data=True,
    zip_safe=False,
)
