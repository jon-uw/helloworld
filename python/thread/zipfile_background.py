'''
     copy from python2.7 tutorial 11.4. Multi-threading
'''

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'finisehd background zip of: ', self.infile

background = AsyncZip('zipfile_background.py', 'tmp.zip')
background.start()

print 'The main program is still running'
background.join()
print 'backgroud zip job is done..'
