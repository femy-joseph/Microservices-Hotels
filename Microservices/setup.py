from setuptools import find_packages, setup

setup(name="microservices",
      version = "0.1",
      description = "Microservices using MongoDB and Flask",
      author = "Femimol Joseph",
      platforms = ["any"],
      license = "BSD",
      packages = find_packages(),
      install_requires = ["Flask==2.0.2", "requests==2.22.0","pymongo==3.12.1" ],
      )
