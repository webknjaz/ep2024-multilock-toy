"""Lokiverse API."""

import contextlib
from threading import Thread
from time import sleep

from cheroot.wsgi import Server as WSGIServer


def _produce_hello_world(_environ, start_response):
    http_status = '200 OK'
    http_headers = [('Content-type', 'text/plain')]
    start_response(http_status, http_headers)
    return [b'Hello world!']


@contextlib.contextmanager
def serve_lokiverse_web_app(bind_addr):
    http_server = WSGIServer(
        bind_addr=bind_addr,
        wsgi_app=_produce_hello_world,
    )
    server_thread = Thread(target=http_server.safe_start)
    server_thread.start()
    while not http_server.ready:
        sleep(0.1)

    try:
        yield http_server
    finally:
        http_server.stop()
        server_thread.join()
