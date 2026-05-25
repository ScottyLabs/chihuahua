# Packages

This folder stores helper code for the main app in a package format.

## Creating a new package
Create a new package in this folder following these steps

### 1. Initialize a package
In this folder, run
```shell
uv init <package-name> --package
```

### 2. Add it to the main [`pyproject.toml`](../pyproject.toml)
Add it as a dependency under `project.dependencies`.

```toml
[project]
# other configuration options
dependencies = [
    # other dependencies
    "package-name",
]
```

and mark it as a workspace source under `tool.uv.sources`

```toml
[tool.uv.sources]
# other packages
package-name = { workspace = true }
```

### Use the package

After running `uv sync`, the package should be available to import from the main chihuahua app package
or from other packages.