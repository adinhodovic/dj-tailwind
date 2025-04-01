# Dj-tailwind

![Lint](https://github.com/adinhodovic/dj-tailwind/workflows/Test/badge.svg)
![Test](https://github.com/adinhodovic/dj-tailwind/workflows/Lint/badge.svg)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/dj-tailwind.svg)](https://pypi.org/project/dj-tailwind/)
[![PyPI Version](https://img.shields.io/pypi/v/dj-tailwind.svg?style=flat)](https://pypi.org/project/dj-tailwind/)

Dj-tailwind is a Django app that allows you to quickly add Tailwind to your project. It's a simple way to get started with Tailwind CSS in Django.

Features:

- Uses [cookiecutter](https://github.com/cookiecutter/cookiecutter) to initialize an empty Tailwind project.
- Adds commands for building, updating and watching and Tailwind.
- Provides template tags for including Tailwind CSS in your templates.
- Provides settings to configure the initial Tailwind build.


## Installation

Install `dj-tailwind` with pip:

```sh
pip install dj-tailwind`
```

Add the app and dependencies to installed Django applications:

```py
INSTALLED_APPS = [
    ...
    "dj-tailwind",
    ...
]
```

Optional: set the Tailwind configuration in your settings file:

```py
DJ_TAILWIND_APP_NAME = "tailwind" # The name of the app that will be created, defaults to `dj_tailwind_output`
DJ_TAILWIND_ENABLE_DAISYUI = True # Enable daisyUI
```

Run the `init` command to create the Tailwind project:

```sh
python manage.py dj_tailwind init
```

The preceding command generates a Django app called `dj_tailwind_output` which contains the Tailwind project. The folder is located in the root of your Django project.

Add the generated app to your installed apps:

```py
INSTALLED_APPS = [
    ...
    "dj_tailwind_output",
    ...
]
```

Add the Tailwind CSS to your base template:

```html
{% load tailwind_tags %}

<head>
{% dj_tailwind_css %}
</head>
```

Run the `start` command to start the Tailwind project in watch mode:

```sh
python manage.py dj_tailwind start
```

### Customization

`Dj-tailwind` uses the default Tailwind configuration file and optionally adds the `daisyUI` plugin. To not introduce complexity and leave customization to end users, you're expected to customize the Tailwind configuration by editing the `tailwind.input.css` file in the `dj_tailwind_output` app. An example configuration file custom fonts and themes:

```css
@import 'tailwindcss' source('../');
@plugin "@tailwindcss/typography";
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/aspect-ratio";

@plugin "daisyui" {
  themes: light --default;
}
@plugin "daisyui/theme" {
  name: light;
  font-family:
    Noto Sans,
    Inter var;
}
```

## Commands

`Dj-tailwind` provides several commands to manage the Tailwind project:

- `./manage.py dj_tailwind init` - Initializes the Tailwind project.
- `./manage.py dj_tailwind build` - Builds the Tailwind project.
- `./manage.py dj_tailwind start` - Starts the Tailwind project in watch mode.
- `./manage.py dj_tailwind update` - Updates the Tailwind project.

## Alternatives

- [https://github.com/timonweb/django-tailwind] - similar project but hasn't been updated in a while. This is just a simplified version of that project.
- [https://github.com/django-commons/django-tailwind-cli] - uses the precompiled Tailwind command-line tool, no dependency on node. However, custom theming seems more complex.
