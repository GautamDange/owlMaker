import os
from OpenSSL import crypto

class PKCS12Manager():

    def __init__(self, p12file, passphrase):
        self.p12file = p12file
        self.unlock = passphrase
        self.webservices_dir = ''
        self.keyfile = ''
        self.certfile = ''

        # Get filename without extension
        ext = os.path.splitext(p12file)
        self.filebasename = os.path.basename(ext[0])

        self.createPrivateCertStore()
        self.p12topem()

    def getKey(self):
        return self.keyfile

    def getCert(self):
        return self.certfile

    def createPrivateCertStore(self):
        home = os.path.expanduser('~')
        webservices_dir = os.path.join(home, '.webservices')
        if not os.path.exists(webservices_dir):
            os.mkdir(webservices_dir)
        os.chmod(webservices_dir, 0o700)
        self.webservices_dir = webservices_dir

    def p12topem(self):
        p12 = crypto.load_pkcs12(open(self.p12file, 'rb').read(), bytes(self.unlock, 'utf-8'))

        # PEM formatted private key
        key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())

        self.keyfile = os.path.join(self.webservices_dir, self.filebasename + ".key.pem")
        open(self.keyfile, 'a').close()
        os.chmod(self.keyfile, 0o600)
        with open(self.keyfile, 'wb') as f:
            f.write(key)


        # PEM formatted certificate
        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())

        self.certfile = os.path.join(self.webservices_dir, self.filebasename + ".crt.pem")
        open(self.certfile, 'a').close()
        os.chmod(self.certfile, 0o644)
        with open(self.certfile, 'wb') as f:
            f.write(cert)
