from pathlib import Path, PosixPath
from typing import Dict, List, Optional, Union
from experimaestro.commandline import CommandLineJob
from experimaestro.connectors import Connector
from experimaestro.connectors.local import ProcessBuilder, LocalConnector
from experimaestro.connectors.ssh import SshPath, SshConnector


class ScriptBuilder:
    def write(self, job: CommandLineJob) -> Path:
        raise NotImplementedError()


class Launcher:
    """A launcher"""

    def __init__(self, connector: Connector):
        self.connector = connector
        self.environ: Dict[str, str] = {}
        self.notificationURL: Optional[str] = None

    def setenv(self, key: str, value: str):
        self.environ[key] = value

    def setNotificationURL(self, url: Optional[str]):
        self.notificationURL = url

    def scriptbuilder(self) -> ScriptBuilder:
        """Returns a script builder"""
        raise NotImplementedError()

    def processbuilder(self) -> ProcessBuilder:
        """Returns the process builder for this launcher

        By default, returns the associated connector builder"""
        return self.connector.processbuilder()

    @staticmethod
    def get(path: Path):
        """Get a default launcher for a given path"""
        if isinstance(path, PosixPath):
            from .python import PythonLauncher

            return PythonLauncher(LocalConnector())

        if isinstance(path, SshPath):
            from .python import PythonLauncher

            return PythonLauncher(SshConnector.fromPath(path))
        raise ValueError("Cannot create a default launcher for %s", type(path))
