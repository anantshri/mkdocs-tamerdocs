# Mkdocs theme for Android Tamer Documentation

Based on default mkdocs theme with multiple customizations.

Customizations include

1. Capability to hide toc per page via ```hide_toc``` page parameter
1. Bare minimum mindmapping capability
    for this to work we need following items
    1. add ```mindmap: true``` in page
    1. page should contain mind map in markdown list format.
1. Last Build date is shown on the bottom of everypage
2. Social icons added (Twitter / Facebook and Linkedin)
```
extra:
  twitter: https://www.twitter.com/anantshri
  facebook: https://www.facebook.com/Anantshri
  linkedin: https://www.linkedin.com/in/anantshri
```
3. Some SEO Stuff added
1. Remove search from the entire site via mkdocs.yml
```
 extra:
   search: false
```
1. Asciinema integration.
    1. Add a tag ```asciinema:true``` to add relevent css and js
    2. page should contain ```<asciinema-player src="/ascii/demo.json"></asciinema-player>``` where src should point to hosted json file