import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nats_python_client",
    version="0.0.1",
    author="jp-vargas",
    author_email="vargasm.jp@gmail.com",
    description="Nats client abstraction to use inside python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Routte/nats-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)