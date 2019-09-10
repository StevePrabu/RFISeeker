import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()


setuptools.setup(
        name="RFISeeker",
        version='0.1',        
        scipts=['RFISeeker'],
        author="Steve Prabu",
        description="RFI Source Finding",
        packages=setuptools.find_packages(),
        author_email="",url="https://github.com/StevePrabu/RFISeeker.git",
)



