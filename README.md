
I create my website and blog with [Quarto](https:/quarto.org), having migrated from Hugo. Hugo has the nice shortcut command:

```
hugo new content posts/my-first-post.md
```

which creates an empty file with the date header and draft: True. This is a handy convenience not yet available in the Quarto CLI. This package adds it via Python. Clone the repo and:

```
pip install .
```

Then the `quarto-new-content` command should be available. You can then do something like:

```
quarto-new-content posts/my-first-post.qmd
```

and then open the file in your editor, and start editing with a pre-populated header and the file in the directory you specified.

It will also create new directories, for example:

```
quarto-new-content posts/my-first-post/index.qmd
```

will work.
