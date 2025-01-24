from setuptools import setup, find_packages

setup(
    name="json_toolkit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'json',
        'requests',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'pylint',
            'tox',
            'pre-commit',
        ],
    },
    entry_points={
        'console_scripts': [
            'json-toolkit=json_toolkit.cli:main',
        ],
    },
)
