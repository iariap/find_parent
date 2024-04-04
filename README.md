# `find_parent` implementation using Python

We are building a command line tool to navigate the file system. We want to add a command that given two file paths, can find the first parent folder that contains both paths.

So for example: 

```jsx

findParent "a/b/c" "a/b/d"
-> "/a/b"
```

Because filesystems might have aliases, we cannot use the file path to find the parent folder at a glance. (i.e. /var might be pointing to /a/b). We need to find the parent folder by navigating the filesystem.

**Challenge**

Given an input that represents a filesystem, and two files, find the closest folder that contains both file paths.

**Example input**
```
/ (root)
├── a
|   ├── c
|   └── d
└── b
```

```python
assert get_path(root, c) == [root, a, c]

assert get_path(a, b) == []

assert find_parent(root, a, b) == root

assert find_parent(root, c, d) == a

assert find_parent(root, b, c) == root
```