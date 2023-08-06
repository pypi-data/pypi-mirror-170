# netifaces (2)

## 1. What is this?

The original [netifaces](https://github.com/al45tair/netifaces) was abandonned by it's maintainer,
leaving us without the option to get network addresses of any kind in Python. Unfortunately, the 
original sources are more akin to arcane magic, so picking where it's been left off is a difficult
task.

I decided to rewrite `netifaces`, keeping the **exact same API** but adding the following:

- Support for future python versions
- Type annotations
- Maybe a more "queriable" API in the future

This project aims to be a drop-in replacement for those project who use `netifaces`, but I do not
guarantee anything.



