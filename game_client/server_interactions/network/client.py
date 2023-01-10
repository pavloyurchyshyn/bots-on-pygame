import time
import socket

from abc import abstractmethod
from global_obj.logger import get_logger
from settings.network import NetworkData
from server_stuff.constants.start_and_connect import LoginArgs
from game_client.server_interactions.network.connection_wrapper import SocketConnectionWrapper, ConnectionWrapperAbs


LOGGER = get_logger()


class NetworkAbs:
    connection: ConnectionWrapperAbs
    connected: bool

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError


class SocketConnectionNetwork(NetworkData, NetworkAbs):
    def __init__(self):
        super(SocketConnectionNetwork, self).__init__()
        self.connection: SocketConnectionWrapper = None
        self.connected = False

    def connect(self) -> dict:
        if self.connection:
            self.connection.close()
            self.connection = None
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        LOGGER.info(f'Connecting to {self.anon_host}')
        socket_conn.connect(self.server_addr)
        self.connection = SocketConnectionWrapper(socket_conn)
        LOGGER.info(f'Sending creds: {self.credentials}')
        self.connection.send_json(self.credentials)
        response = self.connection.recv_json()
        LOGGER.info(f"Connection server response: {response}")
        self.token = self.connection.token = response.get(LoginArgs.Token)
        return response

    def disconnect(self):
        try:
            # LOGGER.info(f'Disconnecting')
            self.connection.close()
        except Exception as e:
            LOGGER.error('Failed to disconnect')
            LOGGER.error(e)
        finally:
            self.connected = False
            self.connection = None

    def __del__(self):
        if self.connection:
            self.disconnect()


if __name__ == '__main__':
    connection = SocketConnectionNetwork()
    connection.connect()
    i = 0
    while connection.connection.alive:
        i += 1
        data = {'a': i}
        LOGGER.info(f'DATA: {data}')
        connection.connection.send_json(data)
        time.sleep(0.01)
