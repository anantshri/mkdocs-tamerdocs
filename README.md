# Mkdocs theme reloaded

Based on default mkdocs theme with some customizations.

Customizations include

1. Capability to hide toc per page via ```hide_toc``` page parameter
1. Bare minimum mindmapping capability
    for this to work we need following items
    1. add ```mindmap: true``` in page
    1. page should contain mind map in markdown list format.
1. Last Build date is shown on the bottom of everypage
1. Remove search from the entire site via mkdocs.yml
```
 extra:
   search: false
``` 