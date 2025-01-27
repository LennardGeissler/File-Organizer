from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="file-organizer",
    version="1.0.0",
    description="A powerful file and folder organizer tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lennard Geißler",
    author_email="lennardgeissler.development@gmail.com",
    url="https://github.com/LennardGeissler/File-Organizer",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "file-organizer=script:main",
        ]
    },
)
