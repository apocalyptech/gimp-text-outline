# Gimp Text Outline

This is a GIMP script written in Python for putting an outline around text.

This plugin is based on a similar plugin by Pete Nu, available at:
http://pete.nu/software/gimp-outliner/

The primary differences between the two are:

1. His plugin is a little more general-purpose, and will draw outlines around
   any layer, not just text layers.
2. This plugin will stroke the outline using your active brush and brush
   settings, rather than filling a selection.
3. This plugin will auto-crop the layer to be as small as possible, rather than
   leaving it as the full image size.

To use this script, make sure that the selected layer is a text layer you want
to outline, then choose "Text Outline" from the "Decor" submenu of the
"Filters" menu.

The script will create a new, transparent layer underneath your selected layer,
and draw the outline into that new layer.

# Installation

* Save text-outline.py to your Gimp plugin directory.
** On Linux, this will be ~/.gimp-2.8/plug-ins/
** On Windows, apparently it might be something like `C:\Users\[username]\.gimp-2.8\plug-ins`
* Restart GIMP

# Usage

* Make sure that the selected layer is the one containing the text you want to outline.
* Choose "Text Outliner" from the "Decor" submenu of the "Filters" menu

That's it!
