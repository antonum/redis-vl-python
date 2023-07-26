from setuptools import setup, find_packages

# function to read in requirements.txt to into a python list
def read_requirements():
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
    return requirements

def read_dev_requirements():
    with open("requirements-dev.txt") as f:
        requirements = f.read().splitlines()
    return requirements

extras_require = {
    "all": [
        "openai>=0.26.4",
        "sentence-transformers>=2.2.2"
    ],
    "dev": read_dev_requirements()
}


setup(
    name="redisvl",
    description="Vector loading utility for Redis vector search",
    license="BSD-3-Clause",
    version="0.1.0",
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require=extras_require,
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "rvl = redisvl.cli.__init__:main"
        ]
    }
)