import grpc
import cube_pb2
import cube_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cube_pb2_grpc.CubeServiceStub(channel)
    number = 4
    response = stub.GetCube(cube_pb2.CubeRequest(number=number))
    print(f"O cubo de {number} é {response.result}")

if __name__ == "__main__":
    run() 