from setuptools import setup

setup(
    name="calculator-rishin",
    version="0.1.0",
    author="Rishin",
    description="A simple CLI calculator",
    py_modules=["calculator"],
    entry_points={
        "console_scripts": [
            "calculator=calculator:main"
        ]
    }
)
