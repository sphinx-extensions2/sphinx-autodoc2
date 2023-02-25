# Configuration

(config:global)=
## Global

This section describes the configuration options for `sphinx-autodoc2`, that you can set in the `conf.py` file.

```{autodoc2-config}
```

(config:package)=
## Package analysis

In the `autodoc2_packages` configuration option, an item can be a string, or a dictionary such as:

```python
autodoc2_packages = [
    "../src/autodoc2",
    {
        "path": "../src/other/module",
        "module": "other.module",
    },
]
```

The following are keys allowed in the dictionary:

```{autodoc2-config-package}
```
