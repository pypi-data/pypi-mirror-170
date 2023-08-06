# `frequenz-sdk` Release Notes

## Summary

This is the first public open source release based on the internal SDK version v0.10.0. There are no breaking changes in this release, only changes to the project structure, metadata, and automation. Packages are also now uploaded to PyPI as [`frequenz-sdk`](https://pypi.org/project/frequenz-sdk/), so this project now can be installed normally via `pip`:

```sh
python -m pip install frequenz-sdk
```

The GitHub issues were also improved, adding templates for [reporting issues](https://github.com/frequenz-floss/frequenz-sdk-python/issues/new?assignees=&labels=priority%3A%E2%9D%93%2C+type%3Abug&template=bug.yml) and [requesting features](https://github.com/frequenz-floss/frequenz-sdk-python/issues/new?assignees=&labels=part%3A%E2%9D%93%2C+priority%3A%E2%9D%93%2C+type%3Aenhancement&template=feature.yml). Users are also pointed to the [Discussion forums](https://github.com/frequenz-floss/frequenz-sdk-python/issues/new/choose) when trying to open an issue if they have questions instead. Also many labels are assigned automatically on issue and pull request creation.

## Upgrading

Even if there are no breaking changes, you might see this error in your local
environment when upgrading:

    ERROR: Project file:///home/luca/devel/frequenz-sdk-python has
    a 'pyproject.toml' and its build backend is missing the 'build_editable'
    hook. Since it does not have a 'setup.py' nor a 'setup.cfg', it cannot be
    installed in editable mode. Consider using a build backend that supports PEP
    660.

If so, you should probably update the dependencies in you virtual environment
(for example `python -m pip install -U -e .`)
