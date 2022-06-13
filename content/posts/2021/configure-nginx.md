---
title: "Setting up a NGINX configuration 🧩"
date: 2021-10-31T15:08:33+01:00
draft: true
toc: false
tags:
  - website
  - config
  - nginx
---

This is a test

```bash
nginx
├── conf.d
│   ├── hugo.conf
│   ├── leene.robots
│   ├── leene.ssl
│   └── ...
├── nginx.conf
├── sites-available
│   ├── lieuwe
│   └── ...
├── sites-enabled
│   ├── 0root
│   ├── lieuwe  -> ../sites-available/lieuwe
│   └── ...
├── nginx.conf
└── ...
```
