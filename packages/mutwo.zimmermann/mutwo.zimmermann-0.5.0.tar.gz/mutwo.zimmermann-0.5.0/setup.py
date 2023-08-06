import setuptools  # type: ignore

version = {}
with open("mutwo/zimmermann_version/__init__.py") as fp:
    exec(fp.read(), version)

VERSION = version["VERSION"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {"testing": ["nose", "coveralls"]}

setuptools.setup(
    name="mutwo.zimmermann",
    version=VERSION,
    license="GPL",
    description="zimmermann extension for event based framework for generative art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Levin Eric Zimmermann",
    author_email="levin.eric.zimmermann@posteo.eu",
    url="https://github.com/mutwo-org/mutwo.zimmermann",
    project_urls={"Documentation": "https://mutwo.readthedocs.io/en/latest/"},
    packages=[
        package
        for package in setuptools.find_namespace_packages(include=["mutwo.*"])
        if package[:5] != "tests"
    ],
    setup_requires=[],
    install_requires=[
        "sympy>=1.10.1, <2.0.0",
        "mutwo.core>=0.62.0, <1.0.0",
        "mutwo.music>=0.18.0, <1.0.0",
        "mutwo.common>=0.9.0, <1.0.0",
    ],
    extras_require=extras_require,
    python_requires=">=3.9, <4",
)
