---
title: "Setting up a new site."
date: 2021-08-24T10:24:27+02:00
draft: false
toc: false
images:
tags:
  - website
  - setup
  - hugo
---

Previously I tried using grav with the intention to serve a simple website as
it is quite easy to setup and the interface seemed quite nice. However the
editing environment didn't feel good and after googling around a bit hugo
already seemed alot more appealing. It renders from markdown with some html/css
config files and can serve content statically or dynamically without superfluous
features.

So far it looks like I will stick with hugo and in any case a markdown source is
highly portable.

## Building Hugo

Hugo is actually provided by ubuntu and centos repositories but building from
source is equally trivial. I went a head a built hugo from the main repository
using: `go version go1.15.14 linux/amd64` and placed the binary in
`/usr/local/bin`.

```bash
git clone https://github.com/gohugoio/hugo.git
cd hugo
go install
```
I started off with the hermit theme and initialized a repository for this site
and the theme to track changes separately. I will probably adjust the color and
type-setting to some extent. Then eventually adjusting the actual layouts and
templates as we go.

## Git filter

Currently I setup two branches: `master` which is deployed statically on
leene.dev, and `dev` which is just for local development as I try out different
things. I setup a clean-smudge git filter to manage deployment on a site-basis:

```toml
[filter "hostmgmt"]
        smudge = sed 's@\\$HOSTNAME\\$@http://localhost@'
        clean  = sed 's@http://localhost@\\$HOSTNAME\\$@'
```

But looking closer at the hugo documentation, it would be better to prepare a
similar development and production configuration. We'll see if this can evaluate
system environment variables.

## Planned features and content

I usually document most of my system administration work so that will be a large
part of the content here but I am planning to include some technical and
non-technical topics how I see fit.

First I want to setup a clean flow of generating and serving svg content for
well formatted illustrations. Ideally the source code is contained in the
markdown and evaluated by hugo calling some external processing components but
we will see how that works. I will make some milestones as part of the
repository.

Secondly I want to try a few style changes for the hermit template. Most of it
is pretty good but there are a few things that I'd rather customise such as the
main page and the footer.
