from setuptools import setup, find_packages

setup(
    name='example-pynq-notebook',
    version='0.1',
    description='Just an example notebook',
    author='PYNQ Hero',
    url='https://github.com/riklaunim/pynq-example-notebook',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "pynq"
    ],
)
