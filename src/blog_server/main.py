from concurrent.futures import ThreadPoolExecutor
import grpc
import grpc_out.blog_pb2_grpc as blog_grpc
from blog_server.service import Blog
from os import environ


def main():

    port = environ.get("PORT")
    if port is None:

        port = 7707

    server = grpc.server(ThreadPoolExecutor(max_workers=4))

    blog_grpc.add_BlogServiceServicer_to_server(Blog(), server)

    server.add_insecure_port(f'[::]:{port}')

    server.start()

    print(f'Server started on port {port}')

    server.wait_for_termination()


if __name__ == '__main__':

    main()
