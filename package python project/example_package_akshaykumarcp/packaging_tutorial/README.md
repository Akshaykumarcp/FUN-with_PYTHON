# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

#### how to create a build?.
- Install dependencies
    ```
    py -m pip install --upgrade build
    py -m pip install --upgrade twine
    ```
- Enter below command from pyproject.toml file path to create build
    ```
    py -m build
    ```
    ```
    * Creating isolated environment: venv+pip...
    * Installing packages in isolated environment:
    - hatchling
    * Getting build dependencies for sdist...
    * Building sdist...
    * Building wheel from sdist
    * Creating isolated environment: venv+pip...
    * Installing packages in isolated environment:
    - hatchling
    * Getting build dependencies for wheel...
    * Building wheel...
    Successfully built example_package_akshaykumarcp-0.0.1.tar.gz and example_package_akshaykumarcp-0.0.1-py3-none-any.whl
    ```
- push build artifacts to pypi
    ```
    py -m twine upload --repository testpypi dist/*
    ```
    ```
    Uploading distributions to https://test.pypi.org/legacy/
    Enter your API token:
    Uploading example_package_akshaykumarcp-0.0.1-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 kB • 00:00 • ?
    Uploading example_package_akshaykumarcp-0.0.1.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 kB • 00:00 • ?

    View at:
    https://test.pypi.org/project/example-package-akshaykumarcp/0.0.1/
    ```
    - package can be located at: https://test.pypi.org/project/example-package-akshaykumarcp/0.0.1/
- Installing your newly uploaded package
    ```
    pip install -i https://test.pypi.org/simple/ example-package-akshaykumarcp==0.0.1
    ```
    ```
    Looking in indexes: https://test.pypi.org/simple/
    Collecting example-package-akshaykumarcp==0.0.1
    Downloading https://test-files.pythonhosted.org/packages/bf/a8/86874d9ce4a2708f26c98a7efe0072b5ac8995172bbd25a74549512dbd61/example_package_akshaykumarcp-0.0.1-py3-none-any.whl.metadata (685 bytes)
    Downloading https://test-files.pythonhosted.org/packages/bf/a8/86874d9ce4a2708f26c98a7efe0072b5ac8995172bbd25a74549512dbd61/example_package_akshaykumarcp-0.0.1-py3-none-any.whl (2.6 kB)
    Installing collected packages: example-package-akshaykumarcp
    Successfully installed example-package-akshaykumarcp-0.0.1
    ```
- Test pypi uploaded package
    ```
    from example_package_akshaykumarcp import example
    example.add_one(2)
    ```

###### Reference:
- [1](https://packaging.python.org/en/latest/tutorials/packaging-projects/), [2](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml)