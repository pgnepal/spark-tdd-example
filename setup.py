from setuptools import setup, find_packages
    
setup(
    name='clustering',
    version='0.9', 
    url='https://github.com/pgnepal/clustering.git',
    license='Restricted',
    author='Prakash Giri',
    author_email='prakag@gmail.com',
    description ='Spark Clustering Example',
    packages=find_packages(),
    install_requires = ['requests', 'pyspark', 'pandas']
)