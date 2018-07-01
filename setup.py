import setuptools

setuptools.setup(
    name="explorecourses",
    version="1.0.0",
    url="https://github.com/illiteratecoder/Explore-Courses-API",
    author="Jeremy Ephron",
    author_email="jeremye@stanford.edu",
    description="A Python API for Stanford Explore Courses",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)