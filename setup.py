import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="presidiopy", # Replace with your own username
    version="0.0.1",
    author="David Hernandez",
    author_email="hello@davidhernandez.info",
    description="An API library to interact with Microsoft Presidio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/querylayer/presidiopy",
    project_urls={
        "Bug Tracker": "https://github.com/querylayer/presidiopy/issues",
        "Source Code": "https://github.com/querylayer/presidiopy",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.22.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
