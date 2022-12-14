---
title: "Binding QML with Python: PyViewer 👾"
date: 2021-08-29T12:53:19+02:00
draft: false
toc: true
tags:
  - python
  - qml
  - gui
  - code
---

[PyViewer](https://git.leene.dev/lieuwe/pyviewer) is a example project which
implements a simple image browser / viewer in a scrollable grid array. This main
objective here was using QML to define a graphical layout and bind it to a
python code-base. Note that this code base is compatible with both Pyside2 and
Pyside6. This is because while Pyside6 is preferred it is not readily available
on all platforms. Running Pyside6 instead only recommend the qml library version
requirements to omitted.

Please take a look at the git repository for exact implementation details. A
brief summary of this interaction is presented below.

## Emitting QML Calls

Creating a `QObject` and adding `PySide2.QtCore.Slot` decorators to its methods
will allow a python object to be added to the qml context as a referenceable
object. For example here we add "viewer" to the qml context which is a
"PyViewer" python object.

```Python
pyviewer = PyViewer()
engine.rootContext().setContextProperty("viewer", pyviewer)
```

This way we can call the object's python procedure "update_tag_filter" from
within the QML script as follows:

```QML
viewer.update_tag_filter(false);
```

Further using the `PySide2.QtCore.Property` decorator further allows us to call
states in our python object and manipulate them as it were a qml object.

```QML
viewer.path.split("::")
```

## Emitting Python Calls

Once this context is working we can create a `PySide2.QtCore.Signal` object to
call QML methods from within the python context. A python procedure could then
"emit" this signal and thereby prompt any connected qml methods.

```python
self.path_changed.emit()
```

In the qml contect we can connect the signals from the python "viewer" object
to a qml function call "swipe.update_paths" for example.

```qml
viewer.path_changed.connect(swipe.update_paths)
```

## Example: passing images as bindary data

For reference the code below outlines a simple example that loads an image from
a zip archive and makes the binary data available for QML to source. This
avoids the need for explicit file handles when generating or deflating images
that are needed for the QML front-end.

```python
class Archive(ZipFile):
    """Simple archive handler for loading data."""
    @property
    def binarydata(self) -> bytes:
        """Load file from archive by name."""
        with self.open(self.source_file, "r") as file:
            return file.read()
```

The example class above simply inherits from the zipfile standard library where
we read a image and store it as part of the `PyViewer` class shown below. This
class inherits from `QObject` such that the property is exposed to the qml
interface. In this case the `imageloader` is an `Archive` handler that is
shown above.

```python
class PyViewer(QObject):
    """QObject for binging user interface to python backend."""
    @Property(QByteArray)
    def image(self) -> QByteArray:
        """Return an image at index."""
        return QByteArray(self.imageloader.binarydata).toBase64()
```

This setup allows a relatively clean call to the `viewer.image` property within
the QML context as shown below. Other data types such as `int`, `string`,
`float`, and booleans can be passed as expected without requiring the
QByteArray container.

```qml
Image {
  anchors.fill: parent
  fillMode: Image.PreserveAspectFit
  mipmap: true
  source = "data:image;base64," + viewer.image
}
```

## Downside

Debugging and designing QML in this environment is limited since the pyside
python library does not support all available QML/QT6 functionality. In most
cases you are looking at C++ Qt documentation for how the pyside data-types
and methods are supposed to behave without good hinting. Having developed
native C++/QML projects previously helps a lot. The main advantage here is t
hat QML source code / frame-works can be reused.

## Other Notes:

```python
ImageCms.profileToProfile(img, 'USWebCoatedSWOP.icc',
    'sRGB Color Space Profile.icm', renderingIntent=0, outputMode='RGB')
```
