import subprocess
class RclonePy:
    """
    -> Class to mount a Rclone Remote into a path.
    """
    process = None

    def __init__(self, pathConfigFile:str, remote:str, pathToMount:str):
        self.pathToMount = pathToMount
        self.process = subprocess.Popen(['rclone','--config',pathConfigFile,'mount',remote+':/',pathToMount],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err = None
        try: err = self.process.communicate(timeout=0.5)
        except: pass

        if err != None and 'transport endpoint is not connected' in str(err[1]):
            self.process.kill()
            subprocess.call('fusermount -u '+self.pathToMount, shell=True)
            self.process = subprocess.Popen(['rclone','--config',pathConfigFile,'mount',remote+':/',pathToMount],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try: err = self.process.communicate(timeout=0.5)
            except: pass
        
        if err != None and err[1]!=b'':
            raise Exception(err[1])

    def __del__(self):
        if self.process is not None:
            try:
                self.process.kill()
                subprocess.call('fusermount -u '+self.pathToMount, shell=True)
            except: pass
            finally: self.process = None

    def __enter__(self):
        return self


    def __exit__(self, type, value, tb):
        if self.process is not None:
            try:
                self.process.kill()
                subprocess.call('fusermount -u '+self.pathToMount, shell=True)
            except: pass
            finally: self.process = None
