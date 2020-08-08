import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nats_python_client", # Replace with your own username
    version="0.0.1",
    author="jp-vargas",
    author_email="vargasm.jp@gmail.com",
    description="Nats client to use inside Routte python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_namespace_packages(include=["src.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)