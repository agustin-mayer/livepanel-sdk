from setuptools import setup, find_packages

setup(
    name='Livepanel_SDK',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Agustin Mayer',
    author_email='agustin.mayer@livepanel.co',
    description='SDK para integrar con la API de Livepanel',
    url='https://github.com/agustin-mayer/livepanel-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)