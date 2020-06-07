import os
import shutil
import sys

from setuptools import setup, find_packages

package_name = 'example-pynq-notebook'

notebook_source_folder = 'notebook/'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']


setup(
    name=package_name,
    version='0.5',
    description='Just an example notebook',
    author='PYNQ Hero',
    url='https://github.com/riklaunim/pynq-example-notebook',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "pynq"
    ],
)


def install_notebook(notebook_name):
    notebook_path = os.path.join(board_notebooks_dir, notebook_name)
    if os.path.isdir(notebook_path):
        shutil.rmtree(notebook_path)
    shutil.copytree(notebook_source_folder, notebook_path)


if 'install' in sys.argv:
    install_notebook(package_name)
