import subprocess
import time
import grpc
import cube_pb2
import cube_pb2_grpc

def test_grpc_cube():
    # Inicia o servidor em background
    server = subprocess.Popen(["python", "server.py"])
    time.sleep(1)  # Aguarda o servidor subir

    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = cube_pb2_grpc.CubeServiceStub(channel)
        response = stub.GetCube(cube_pb2.CubeRequest(number=3))
        assert response.result == 27
    finally:
        server.terminate() 