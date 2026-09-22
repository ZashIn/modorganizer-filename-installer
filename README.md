Mod Organizer plugin (`IPluginInstaller`) to set the mod name (`GuessedString`) to the filename. Actual installation has to be handled by other installers.

## Installation
Either copy `filename_installer.py` into MO's plugins directory or checkout this repo directly into a subfolder of the plugin dir.

## Config
This plugin is deactivated by default. To activate it explicitly for an MO instance, go to `Settings/Plugins/Installer/Filename Installer` and set it to ☑ Enabled.

You can also configure the installer priority (default: 100) and the [GuessQuality](https://github.com/ModOrganizer2/modorganizer-uibase/blob/6d05e42a8a59ec7993bcdfbae6643ac81b73db05/include/uibase/guessedvalue.h#L35) of the filename given to other installers.