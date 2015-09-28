from local import Repo

from xpootle.fs.core import Plugin, plugins, FSFile


default_app_config = 'xpootle.fs.local.apps.PootleFSLocalConfig'


class LocalFSFile(FSFile):

    @property
    def latest_commit(self):
        # return mtime
        pass

class LocalFSPlugin(Plugin):
    name = "filesystem"
    file_class = LocalFSFile

    def pull(self):
        pass

    def get_latest_commit(self):
        # return mtime?
        pass

plugins.register(LocalFSPlugin)
