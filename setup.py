from setuptools import setup

setup(
   name='nebari-cli',
   version='1.0',
   description='..',
   author='Asmi',
   author_email='asmijafar.20@gmail.com',
   entry_points={
       'console_scripts':["nebari=cli.main:app"],
   }   
)