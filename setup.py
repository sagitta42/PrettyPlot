from setuptools import setup, find_packages

setup(
    name='prettyplot',
    version='0.0',
    author='Mariia Redchuk',
    author_email='mariia.redchuk@gmail.com',
    url='https://github.com/sagitta42/prettyplot',
    description='Python class for quick and pretty plotting',
    long_description='',
    packages=find_packages(),
    install_requires=[
        'matplotlib'
#        'numpy',
#        'pandas',
        # 'fcutils @ https://github.com/legend-exp/pyfcutils.git#egg=1.0.0'
    ],
#    cmdclass=dict(build_ext=CMakeBuild, build_py=PygamaBuild, develop=PygamaDev),
    zip_safe=False,
)