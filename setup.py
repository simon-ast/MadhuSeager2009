from setuptools import find_packages, setup

setup(
    name="taurex_MadhuSeager2009",
    version="0.0.3",
    author="M. F. Bieger",
    author_email="michellebieger@live.com",
    license="BSD",
    description="A replication of the temperature-pressure profile from "
    "Madhusudhan and Seager 2009, arXiv:0910.147v2",
    packages=find_packages(exclude=("tests", "doc")),
    install_requires=["taurex"],
    entry_points={
        "taurex.plugins": ["taurex_MadhuSeager2009 = taurex_MadhuSeager2009"]
    },
)