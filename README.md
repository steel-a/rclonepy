# rclonepy
Interface to mount a Rclone drive in Python 

Requirements: rclone and fuse packages

Example of use:

```
from rclonepy import RclonePy

with RclonePy('/mnt/configs/rclone.conf', 'myDrive', '/mnt/files'):
    # do your file process inside /mnt/files and it will reflects on myDrive:/
```