try:
    # Note the relative import!
    from .action_place_footprints import PlaceFootprints
    # Instantiate and register to Pcbnew
    PlaceFootprints().register()
# if failed, log the error and let the user know
except Exception as e:
    # log the error
    import os
    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(plugin_dir, 'place_footprints_error.log')
    with open(log_file, 'w') as f:
        f.write(repr(e))
    # register dummy plugin, to let the user know of the problems
    import pcbnew
    import wx

    class PlaceFootprints(pcbnew.ActionPlugin):
        """
        Notify user of error when initializing the plugin
        """
        def defaults(self):
            self.name = "Place Footprints"
            self.category = "Place Footprints"
            self.description = "place selected footprints or footprints from multiple sheets " \
                                "in linear, circular or matrix arrangement"
            self.icon_file_name = os.path.join(os.path.dirname(__file__), 'place_footprints_light.png')
            self.dark_icon_file_name = os.path.join(os.path.dirname(__file__), 'place_footprints_dark.png')
            self.show_toolbar_button = True

        def Run(self):
            caption = self.name
            message = "There was an error while loading plugin \n" \
                      "Please take a look in the plugin folder for place_footprints_error.log\n" \
                      "You can raise an issue on GitHub page.\n" \
                      "Please attach the .log file"
            wx.MessageBox(message, caption, wx.OK | wx.ICON_ERROR)

    PlaceFootprints().register()

