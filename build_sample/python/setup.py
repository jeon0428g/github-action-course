from setuptools import setup, find_packages

setup(
    name='humancat',
    version='0.0.5',
    description='GitHub Action Build Test Sample',
    author='jeon0428g',
    author_email='jeon0428g@gmail.com',
    url='https://github.com/jeon0428g/github-action-course',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['sample', 'cat', 'human', 'humancat'],
    python_requires='>=3.8',
    package_data={},
    zip_safe=False
)
