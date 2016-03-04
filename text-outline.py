#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# This is a GIMP script written in Python for putting an outline around text
#
# This plugin is based on a similar plugin by Pete Nu, available at:
#     http://pete.nu/software/gimp-outliner/
#
# The primary differences between the two are:
#
#     1) His plugin is a little more general-purpose, and will draw outlines
#        around any layer, not just text layers.
#
#     2) This plugin will stroke the outline using your active brush and brush
#        settings, rather than filling a selection.
#
#     3) This plugin will auto-crop the layer to be as small as possible,
#        rather than leaving it as the full image size.
# 
# To use this script, make sure that the selected layer is a text layer you
# want to outline, then choose "Text Outline" from the "Decor" submenu of the
# "Filters" menu
#
# The script will create a new, transparent layer underneath your selected
# layer, and draw the outline into that new layer.

from gimpfu import *

def text_to_path(image, layer):
    """
    Creates a new path based on the passed-in text layer.  Will end
    up throwing a RuntimeException if our layer is not text.  Returns
    the new path.
    """

    path = pdb.gimp_vectors_new_from_text_layer(image, layer)
    pdb.gimp_image_insert_vectors(image, path, None, 0)
    return path

def add_new_layer_beneath(image, layer):
    """
    Adds a new layer beneath the given layer.  Return value is the new
    layer.  Will raise an ValueError if for some reason we can't find
    our own layer.  Note that after adding to the Gimp image, this
    new layer will become the active layer.
    """

    # Get the layer position.
    position = image.layers.index(layer)

    # Add a new layer below the selected one
    new_title = '%s Text Outline' % (layer.name)
    new_layer = gimp.Layer(image, new_title,
        image.width, image.height,
        RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(new_layer, position + 1)    

    # And finally return
    return new_layer

def stroke_path_and_remove(image, layer, path):
    """
    Strokes along the given path, using the current active brush.
    Then removes our temporary path from the list
    """

    pdb.gimp_edit_stroke_vectors(layer, path)
    pdb.gimp_image_remove_vectors(image, path)

def crop_layer(image, layer):
    """
    Autocrops the given layer to be as small as possible.  This actually
    just calls a different plugin which does all the heavy lifting.
    """
    pdb.plug_in_autocrop_layer(image, layer)

def add_text_outline(image, layer) :
    """
    Main function to do our processing.  image and layer are
    passed in by default, we require no other arguments.
    """

    gimp.progress_init("Drawing outline around text")

    # Create a path from the current layer
    path = text_to_path(image, layer)
    gimp.progress_update(25)

    # Add a new layer
    new_layer = add_new_layer_beneath(image, layer)
    gimp.progress_update(50)

    # Stroke along our path and remove it
    stroke_path_and_remove(image, new_layer, path)
    gimp.progress_update(75)

    # Now autocrop the layer so it doesn't take up the
    # whole image size.  Relies on another plugin which
    # I assume must be stock, since I didn't install it
    # manually.
    crop_layer(image, new_layer)
    gimp.progress_update(100)

    # Aaaand exit.
    return

# This is the plugin registration function
register(
    "text_outline",
    "Text Outline",
    "Will draw an outline around text using the active brush.  The outline is drawn to a separate layer underneath the selected layer and cropped to its smallest area.",
    "CJ Kucera",
    "CJ Kucera",
    "Oct 2015",
    "<Image>/Filters/Decor/Text Outline",
    "*",
    [],
    [],
    add_text_outline)

main()
