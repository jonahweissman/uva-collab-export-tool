# uva-collab-export-tool

> Trying to get a local copy of everything I have access to on UVA Collab

## Student access

You can mount the Resources section as a local folder using WebDAV. You will need a WebDAV client. I use the one that comes with [Gnome Files](https://wiki.gnome.org/action/show/Apps/Files), found by clicking "Other Locations". The URL is `davs://collab.its.virginia.edu/dav/82793c24-aafa-4608-991d-786ee65b34e4`, replacing the UUID with the UUID of the site you want to download. Put your netbadge ID as your username. You can get a 7 day access token by navigating to Profile Menu (your name in the upper right corner) > Profile > My Resources > Transfer Multiple Files. Use this access token as your password. You should be able to copy the whole folder recursively onto your computer.

TODO: make everything happen automatically and seamlessly

https://pypi.org/project/webdavclient3/

https://collab.its.virginia.edu/direct/site.json (paginated)


## With admin access

https://longsight.screenstepslive.com/s/sakai_help/m/59023/l/556753-how-do-i-export-archive-an-individual-site

## If you own the site

Collab recommends "Want to copy all the resources from another of your UVACollab sites? Use the "Import from Site" option in "Site Settings" instead."

# Contributing

If you know a better way to do this, please let me know. Feel free to ask questions if this is unclear.
