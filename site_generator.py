import os

from jinja2 import Environment, FileSystemLoader


def load_jinja_templates(dir_path):
    jinja_env = Environment(loader=FileSystemLoader(dir_path),
                            trim_blocks=True,
                            lstrip_blocks=True)
    with os.scandir(dir_path) as dir_iterator:
        return {file.name: jinja_env.get_template(file.name) for file in dir_iterator if file.is_file()}


def render_page(jinja_template, file_name):
    with open(file_name, 'w', encoding='utf-8') as page:
        page.write(jinja_template.render())


if __name__ == '__main__':
    templates_path = 'templates'
    jinja_templates = load_jinja_templates(templates_path)
    render_page(jinja_templates['index.html'], 'index.html')
    render_page(jinja_templates['requests.html'], 'requests.html')

