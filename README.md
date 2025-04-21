# translations-cookiecutter

**A Cookiecutter template for creating translation repositories within the Scientific Python ecosystem.**

This template helps maintainers set up dedicated translation repositories that are ready to integrate with [Crowdin](https://crowdin.com/) and the [Scientific Python Translations](https://scientific-python-translations.github.io/) infrastructure.

---

## What is this?

The `translations-cookiecutter` provides a standardized structure for Scientific Python project translation repositories. It includes boilerplate files, GitHub Actions workflows, and configuration that allow projects to integrate multilingual content into their websites efficiently.

## 🚀 Getting Started

### Prerequisites

- Python ≥ 3.7
- [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Install Cookiecutter:

```bash
pip install cookiecutter
```

### Example: Creating a Translation Repo for NumPy

Let’s say you're setting up translations for the [NumPy website](https://numpy.org/).

You should first ask the Scientific Python Translations Team to create a new project on the [Scientific Python Crowdin](https://scientific-python.crowdin.com/u). For this example the project name is `NumPy.Org`. Letter casing must match exactly.

Run the following command:

```bash
cookiecutter gh:Scientific-Python-Translations/translations-cookiecutter
```

You’ll see prompts like this:

```bash
  [1/11] project_name (): NumPy.Org
  [2/11] source_org (): numpy
  [3/11] source_repo_name (): numpy.org
  [4/11] base_source_folder (content):
  [5/11] source_ref (main):
  [6/11] translations_repo (Scientific-Python-Translations/numpy.org-translations):
  [7/11] translations_folder (numpy.org-translations/content/en/):
  [8/11] translations_ref (main):
  [9/11] translation_percentage (90):
  [10/11] approval_percentage (0):
  [11/11] Select use_precommit
    1 - false
    2 - true
    Choose from [1/2] (1): 2
```

Notice that the project name must match the Crowdin project name. As the prompt keeps asking for
the project details, you will get default suggestions in parentheses which correspond to the used
defaults for the projects already added to the organization.

After answering, a new folder `numpy.org-translations/` will be created with:

- Crowdin configuration files
- GitHub Actions workflows
- Folder structure for localized content

Next steps:

1. Push it to GitHub:

   ```bash
   cd numpy.org-translations
   git init
   git remote add origin git@github.com:Scientific-Python-Translations/numpy.org-translations.git
   git add .
   git commit -m "Initial commit from translations-cookiecutter for NumPy.Org website"
   git push -u origin main
   ```

2. Request a Crowdin project via the [Scientific Python Discord](https://scientific-python.org/community/), if one hasn't been created already.

3. Update the language switcher and localization configuration on [`numpy.org`](https://github.com/numpy/numpy.org) to begin serving translated content.

4. Update the `crowdin.yml` file contents. The template will create a default Crowind configuration file
   but the contents for the `files` setion will change from project to project so this needs to be updated
   in order to have the correct integration. You can read more about the configuration file on the [Crowdin support docs](https://support.crowdin.com/developer/configuration-file/).

```yaml
# https://support.crowdin.com/developer/configuration-file/
project_identifier: PROJECT_IDENTIFIER_CROWDIN
api_key: API_KEY_CROWDIN
base_path: ./
preserve_hierarchy: true
files:
  # Update this to the correct extensions of your project
  - source: /content/en/*.md
    translation: /content/%two_letters_code%/%original_file_name%
    update_option: update_as_unapproved
    # ignore:
    #  - /content/en/*.mdx
```

## 🙌 Community & Support

- Join the [Scientific Python Discord](https://scientific-python.org/community/) and visit the `#translation` channel
- Browse the [Scientific Python Translations documentation](https://scientific-python-translations.github.io/docs/)
- Visit the [content-sync](https://github.com/Scientific-Python-Translations/content-sync) and [translations-sync](https://github.com/Scientific-Python-Translations/translations-sync) Github actions.

## 🤝 Contributing

Want to improve this template? Found a bug? [Open an issue](https://github.com/Scientific-Python-Translations/translations-cookiecutter/issues) or pull request!

## 📄 License

This project is licensed under the [MIT License](LICENSE).
