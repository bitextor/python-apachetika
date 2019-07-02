import jpype
import chardet
import threading

lock = threading.Lock()

ByteArrayInputStream        = jpype.JClass('java.io.ByteArrayInputStream')

class Extractor(object):
    extractor = None
    data      = None

    def __init__(self, **kwargs):
        if 'pdf' in kwargs:
            self.data = kwargs['pdf']
        else:
            raise Exception('No pdf provided')

        try:
            # make it thread-safe
            if threading.activeCount() > 1:
                if jpype.isThreadAttachedToJVM() == False:
                    jpype.attachThreadToJVM()
            lock.acquire()

            self.extractor = jpype.JClass(
                    "com.java.app.PDFExtract").INSTANCE

        finally:
            lock.release()

        reader = ByteArrayInputStream(self.data)

    def getHTML(self):
        return self.extractor.extract(self.reader)

