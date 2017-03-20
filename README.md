# Mkdocs theme for Android Tamer Documentation

[![PyPI](https://img.shields.io/pypi/dm/mkdocs-tamerdocs.svg)](mkdocs-tamer) [![PyPI](https://img.shields.io/pypi/v/mkdocs-tamerdocs.svg)](Version)

Based on default mkdocs theme with multiple customizations.

Customizations include

1. Capability to hide toc per page via ```hide_toc``` page parameter
2. Bare minimum mindmapping capability
    for this to work we need following items
    1. add ```mindmap: true``` in page
    1. page should contain mind map in markdown list format.
3. Last Build date is shown on the bottom of everypage
4. Social icons added (Twitter / Facebook and Linkedin)
```
extra:
  twitter: https://www.twitter.com/anantshri
  facebook: https://www.facebook.com/Anantshri
  linkedin: https://www.linkedin.com/in/anantshri
```
5. Some SEO Stuff added
6. Remove search from the entire site via mkdocs.yml
```
 extra:
   search: false
```
7. Asciinema integration.
    1. Add a tag ```asciinema:true``` to add relevent css and js
    2. page should contain ```<asciinema-player src="/ascii/demo.json"></asciinema-player>``` where src should point to hosted json file
8. As `include_prev_next` is now deprecated hence new variable extra.navigate added to remove navigation options. So to remove navigation entirely.
```
extra:
  navigation: false
```