class CommandLineStatements:
    """Batch of command line statements surrounding zfs"""

    """Checks the disks in the system"""
    check_disks = "ls -la /dev/disk/by-id"

    """
        zpool command to check status
        {0} = pool
    """
    zpool_status = "sudo zpool status {0}"

    """
        zpool command to turn off drive access
        {0} = pool
        {1} = drive
    """
    zpool_offline = "sudo zpool offline {0} {1}"

    """
        zpool command to turn on drive access
        {0} = pool
        {1} = drive
    """
    zpool_online = "sudo zpool online {0} {1}"

    """
        zpool replace command
        {0} = pool
        {1} = old
        {2} = new
    """
    zpool_replace = "sudo zpool replace {0} {1} {2} -f"

    """zpool import command to show available imports"""
    zpool_import_list = "sudo zpool import"

    """
        zpool import command
        {0} = importable pool
    """
    zpool_import = "sudo zpool import {0}"

    """zfs list command"""
    zfs_list = "sudo zfs list"

    """Disk usage"""
    disk_usage = "df -h"