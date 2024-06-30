import setuptools

setuptools.setup(
    name='django-simple-editorjs',
    version='0.1.2',
    description='A simple editorjs for django',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Gerardo A. Ballester Jr.',
    author_email='gerardoaballesterjr@gmail.com',
    package_data={'django_simple_editorjs': ['static/*', 'templates/*']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    url='https://github.com/gerardoaballesterjr/django-simple-editorjs',
    python_requires='>=3.4,<4.0',
    keywords='django simple editorjs',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
    ],
)