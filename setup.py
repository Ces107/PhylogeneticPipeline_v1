from setuptools import setup, find_packages

setup(
    name='PipelineAnálisis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    'biopython==1.83',  # Especifica la versión 1.83 de Biopython
    'numpy==1.26.4',    # Especifica la versión 1.26.4 de Numpy
    ]

)
