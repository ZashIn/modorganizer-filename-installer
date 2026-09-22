# Only for installation via folder
import mobase

from .filename_installer import FilenameInstaller


def createPlugin() -> mobase.IPlugin:
    return FilenameInstaller()
