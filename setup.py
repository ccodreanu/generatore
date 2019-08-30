import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generatore",
    version="0.0.1",
    author="Catalin Codreanu",
    author_email="cc.catalincodreanu@gmail.com",
    description="Generatore is a static website generator written in Python based on Markdown and Jinja2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/picofish/generatore",
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=['bin/generatore'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
