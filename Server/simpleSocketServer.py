import asyncore
import socket

handler_list = {}


class EchoHandler(asyncore.dispatcher_with_send):

    def configure_local_address(self, address):
        self.address = address

    def configure_target_address(self, address):
        self.target_address = address

    def handle_read(self):
        data = self.recv(8192)
        if data and self.target_address:
            hd = handler_list.get(self.target_address)
            if hd:
                hd.send(data)
            else:
                self.target_address = None
                self.send("fail to send, target is down")
        else:
            self.send("no target")

    def handle_close(self):
        handler_list[self.address] = None
        self.close()
        print 'connection from %s lost' % repr(self.addr)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)
            handler.configure_local_address(addr)
            handler_list[addr] = handler
            if len(handler_list) > 1:
                it1 = handler_list.values()[0]
                it2 = handler_list.values()[1]
                it1.configure_target_address(it2.address)
                it2.configure_target_address(it1.address)

    def handle_close(self):
        self.close()


server = EchoServer('0.0.0.0', 3344)
asyncore.loop()
