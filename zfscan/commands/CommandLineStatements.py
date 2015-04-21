"""
    Batch of command line statements surrounding zfs
"""
class CommandLineStatements:
    def __init__(self):
        self.check_disks = """
            ls -la /dev/disk/by-id
        """

        self.zpool_status = """
            sudo zpool status {}
        """