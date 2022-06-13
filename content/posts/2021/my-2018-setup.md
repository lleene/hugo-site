---
title: "My 2018 Setup"
date: 2021-08-12T10:24:27+02:00
draft: false
toc: true
tags:
  - website
  - about
---

I mainly use RHEL flavours of linux having both CentOS and Fedora machines. Most
hosted services run on CentOS 8 at the moment albeit they are approaching
end-of-life. Overall the package repository for CentOS 7/8 is just right. I
rarely need to compile anything from source and packages are very stable.
I will eventually migrate to Fedora completely which is where I operate my
development environment.

This is a list of my most used self-hosted services:
 - Gitea: Git server with web interface for repository mirrors and personal repos
 - Plex: multi-media hosting service for streaming movies and tv-shows
 - NextCloud: Cloud storage for synchronizing and sharing files
 - Cockpit: Web base administration portal managing linux boxes
 - RoundCube: Web based email client
 - Postfix/Dovcot: Email stack providing SMTP for my domain
 - NGINX: HTTP server serving as proxy for internal web services
 - Danbooru: Ruby-on-rails based image hosting and tagging service

There are several others that I have tried but these really have been the things
I relied on the most in the past 5 years or so. I think the only thing that is
possibly missing from this list is possibly the equivalent of a centralized LDAP
service but I simply haven't had to manage more than handful of users.

Currently I develop quite a bit of python utilities for scraping, labelling, and
managing media in an automated fashion. In part I am preparing data for one of
my long term projects which is related to image classification based on
structural decomposition rather than textural features. The main idea here is
to analyse and extract structure in an image before performing in-depth analysis
such that said analysis is most specific to its context.
