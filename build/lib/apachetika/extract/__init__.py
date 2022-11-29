from jpype import *
import chardet
import threading
import subprocess
from subprocess import PIPE, Popen

lock = threading.Lock()

#ByteArrayInputStream        = JClass('java.io.ByteArrayInputStream')
#ByteArrayOutputStream       = JClass('java.io.ByteArrayOutputStream')

tika_path = "../data/tika-app.jar"


class Extractor(object):
    extractor = None

    def __init__(self, **kwargs):
        try:
            # make it thread-safe
            #if threading.activeCount() > 1:
            #    if isThreadAttachedToJVM() == False:
            #        attachThreadToJVM()
            lock.acquire()
            self.extractor = subprocess.Popen(["java", "-jar", tika_path, "-x"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        finally:
            lock.release()

    def getHTML(self,data):
        return self.extractor.communicate(input=data)
