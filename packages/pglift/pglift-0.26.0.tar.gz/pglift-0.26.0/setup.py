import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

extras_typing = [
    "mypy >= 0.901",
    "types-PyYAML >= 6.0.11",
    "types-python-dateutil",
    "types-requests",
    "types-setuptools",
]

setup(
    name="pglift",
    description="Life-cycle management of production-ready PostgreSQL instances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dalibo/pglift",
    author="Dalibo SCOP",
    author_email="contact@dalibo.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
        "Topic :: Database",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
    ],
    keywords="postgresql deployment administration",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9, <4",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=[
        "attrs",
        "humanize",
        "pgtoolkit >= 0.22.0",
        "pluggy",
        "psycopg[binary] >= 3.1",
        "pydantic",
        "python-dateutil",
        "requests",
        "tenacity",
        "typing-extensions",
        "PyYAML >= 5.1",
        # CLI requirements
        "click >= 8.0.0, != 8.1.0",
        "rich >= 11.0.0",
    ],
    extras_require={
        "dev": [
            "black >= 22.1.0",
            "check-manifest",
            "flake8",
            "isort",
            "pre-commit",
        ]
        + extras_typing,
        "test": [
            "patroni[etcd]",
            "port-for",
            # psycopg2 required by community.postgresql ansible module
            "psycopg2-binary",
            "pytest",
            "pytest-cov",
            "requests",
            "tenacity >= 8.0.0",
            "ansible",
        ],
        "typing": extras_typing,
        "docs": [
            "furo",
            "sphinx",
        ],
    },
    include_package_data=True,
    package_data={
        "pglift": ["py.typed"],
    },
    entry_points="""
        [console_scripts]
        pglift=pglift.cli:cli
    """,
    project_urls={
        "Documentation": "https://pglift.readthedocs.io/",
        "Source": "https://gitlab.com/dalibo/pglift/",
        "Tracker": "https://gitlab.com/dalibo/pglift/-/issues/",
    },
)
