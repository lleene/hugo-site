---
title: "Hugo Integration 🧭"
date: 2021-10-30T15:42:22+02:00
draft: true
toc: false
pyscript: true
tags:
  - untagged
---

## This is Work in Progress

The hope here is that we can call a predefined go procedure that parses
some section of markdown source code and instantiates the corresponding svg file
under our static folder that is then referenced.

``` go
{{/* a comment */}}
```

## Using Python Script

Example using standard output from a python script.

{{< pyscript >}}
print("test string")
{{< /pyscript >}}

Example using matplotlib to generate a simple graph.

{{< pyplot >}}
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10)
y = x ** 2
fig, ax = plt.subplots()
ax.plot(x, y)
fig
{{< /pyplot >}}


Example using matplotlib to generate a scatter plot.

{{< pyplot >}}
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(25)
y = np.random.randn(25)
fig, ax = plt.subplots()
ax.scatter(x, y)
fig
{{< /pyplot >}}
