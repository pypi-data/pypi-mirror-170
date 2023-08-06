PyGObject prebuilt libraries
============================

Introduction
------------

Windows platform only

MSVC version: vs16 - VS2019
PyGObject version: 3.42.2
PyCairo version: 1.21.0


Install
-------

```shell
pip install pygobject-pycairo-prebuilt-libraries-vs2019
```

Usage
-----

```python
try:
    from pygobject_prebuilt_deps import import_pygobject_dll_module
    import_pygobject_dll_module()
except ImportError:
    pass

import gi
gi.require_version("Gtk", "3.0")

```


How it work
-----------


pygobject-pycairo-prebuilt-libraries-vs2019 package will install all prebuilt libraries in site-packages/pygobject_prebuilt_deps
 
```
site-packages
    - pygobject_prebuilt_deps
        - wheels
            - pycairo-xxx.whl
            - pygobject-xxx.whl
        - x86_vs16
            - bin
                - xxx.dll # precompiled Gtk-3 dll ...
            - gi_tylelib
                - gireposisitory-1_0 # gi typelib
        - x64_vs16
            - bin 
                - xxx.dll # precompiled Gtk-3 dll ...
            - gi_tylelib
                - gireposisitory-1_0 # gi typelib
```

When you call `import_pygobject_dll_module`, this function will add the dll bin path to `os.environ['PATH']` and set the corresponding `GI_TYPELIB_PATH` so that you can load the correct prebuilt dll libraries.


