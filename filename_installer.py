from collections.abc import Sequence
from pathlib import Path
from typing import Any

import mobase


class FilenameInstaller(mobase.IPluginInstallerCustom):
    """
    Installer to set `mobase.GuessedString` to filename only. Does not handle rest of the installation.
    """

    def __init__(self) -> None:
        super().__init__()
        mobase.IPluginInstallerCustom.__init__(self)

    def init(self, organizer: mobase.IOrganizer) -> bool:
        self._organizer = organizer
        return True

    def name(self) -> str:
        return "Filename Installer"

    def description(self) -> str:
        return "Installer to set mod name to file name only."

    def author(self) -> str:
        return "Zash"

    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo("0.1.0", mobase.VersionScheme.REGULAR)

    def enabledByDefault(self):
        return False

    def settings(self) -> Sequence[mobase.PluginSetting]:
        return [
            mobase.PluginSetting("priority", "priority of the installer", 100),
            mobase.PluginSetting(
                "guess_quality",
                f"GuessQuality of the filename: {', '.join(mobase.GuessQuality.__members__)}",
                mobase.GuessQuality.PRESET.name,
            ),
        ]

    def isArchiveSupported(self, obj: Any) -> bool:  # type: ignore
        return True

    def supportedExtensions(self) -> set[str]:
        return {"zip", "rar", "7z", "fomod", "001"}

    def isManualInstaller(self) -> bool:
        return False

    def priority(self) -> int:
        return int(self._organizer.pluginSetting(self.name(), "priority"))  # type: ignore

    def install(
        self,
        mod_name: mobase.GuessedString,
        game_name: str,
        archive_name: str,
        version: str,
        nexus_id: int,
    ) -> mobase.InstallResult:
        print("FILENAME INSTALLER")
        mod_name.update(Path(archive_name).stem, mobase.GuessQuality.PRESET)
        # Return NOT_ATTEMPTED to let other installer, like Simple Installer (InstallerQuick), handle actual installation.
        return mobase.InstallResult.NOT_ATTEMPTED


def createPlugin() -> mobase.IPlugin:
    return FilenameInstaller()
