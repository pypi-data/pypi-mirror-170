# New Project templater

This tool can be used to create a new project based on a project template, with the following syntax:

    newproject <template path / Git URL> <project name> [output]

*When the output isn't specified, the project name is used instead.*

## Installing

This tool can be installed with the following command:

    pip install pursuit-newproject

## Project manifest

The template must contain a `project.yml` template with the following sections:

- `template_name`: The name of the project template
- `template_files`: A list of files that will be treated as [Jinja2](https://pypi.org/project/Jinja2/) templates. These files can reference the project name using the `{{ project_name }}` syntax.
- `template_paths`: A list of files or directories that need to be moved to Jinja2-compatible paths

```yaml
---

template_name: Template name
template_files:
  - "templated_file"
template_paths:
  "templated_dir": "{{ project_name }}"
```

## License

This project is licensed under the [GNU GPLv3 license](https://gitlab.com/frPursuit/newproject/-/blob/master/README.md).

