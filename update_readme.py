#!/usr/bin/env python
import pathlib


root = pathlib.Path(__file__).parent.resolve()
til_count = len(list(root.glob("*/*.md")))

def get_path_url(root):
    path_url = []
    for filepath in root.glob("*/*.md"):
        path = str(filepath.relative_to(root))
        url = "https://github.com/dwssef/til/blob/main/{}".format(path)
        path_url.append([path, url])
    return path_url

def readme_demend_data(path_url):
    readme_data = {}
    for path, url in path_url:
        key = path.split("/")[0]
        md_url = f'[{path}]({url})'
        if key in readme_data:
            readme_data[key].append(md_url)
        else:
            readme_data[key] = [md_url]
    return readme_data

def readme_template(rdata):
    template = []
    for topic, md_url in rdata.items():
        template.append(f'## {topic}')
        for i in md_url:
            template.append(i)
    return template

def save_to_readme(template):
    readme = root / "README.md"
    with open(readme, 'w') as f:
        f.write("# Today I Learned\n\n")
        f.write('My Today I Learned snippets. Inspired by [simonw/til](https://github.com/simonw/til).\n\n')
        f.write(f'{til_count} TILs so far.\n\n')
        for i in template:
            f.write(i)
            f.write('\n\n')


path_url = get_path_url(root)
rdata = readme_demend_data(path_url)
template = readme_template(rdata)
save_to_readme(template)
