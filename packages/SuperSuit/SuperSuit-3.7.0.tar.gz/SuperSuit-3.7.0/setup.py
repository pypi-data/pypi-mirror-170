import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    path = "supersuit/__init__.py"
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


setuptools.setup(
    name="SuperSuit",
    version=get_version(),
    author="SuperSuit Community",
    author_email="jkterry@farama.org",
    description="Wrappers for Gymnasium and PettingZoo",
    license_files=("LICENSE.txt",),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PettingZoo-Team/SuperSuit",
    keywords=["Reinforcement Learning", "gymnasium"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pettingzoo>=1.22.0",
        "tinyscaler>=1.0.4",
        "gymnasium>=0.26.0",
        "pygame==2.1.2",
        "pymunk==6.2.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras={"dev": ["pettingzoo[butterfly]"]},
    include_package_data=True,
)
