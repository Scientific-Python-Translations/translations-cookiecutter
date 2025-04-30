import os

# Create the folder structure for content and translations
content_path = "{{ cookiecutter.translations_source_path }}"
print(content_path)
os.makedirs(content_path, exist_ok=True)
