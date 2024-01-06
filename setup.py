from setuptools import setup, find_packages

setup(
    name='toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'transformers==4.36.2',
        'diffusers==0.25.0',
        'torch==1.10.0',
        'ctransformers==0.2.27',
        'accelerate==0.25.0'
    ],
)
