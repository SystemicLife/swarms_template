# python_project_template

Using cookiecutter to create a python project template.

```
python3 -m pip install --user cookiecutter
```

Following [1]

[1](https://cookiecutter.readthedocs.io/en/stable/installation.html)

To use this, modify the {{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py file to contain the code you want to template. Then modify the cookiecutter.json file to contain the default values you want to change. Then run the following command, from within the directory you want to create a new project in (in this example, /tmp):

```
cookiecutter ~/git/python_project_template
```

The output will look like:

```shell
/tmp$ cookiecutter ~/git/python_project_template
  [1/3] directory_name (Hello): 
  [2/3] file_name (Howdy): 
  [3/3] greeting_recipient (Julie): 
```
which creates a directory called Hello, with a file called Howdy.py, which contains the following code:

```python
print("Hello, Julie!")
```

```

