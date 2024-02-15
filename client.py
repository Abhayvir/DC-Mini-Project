# client.py

import grpc
import mapreduce_pb2
import mapreduce_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = mapreduce_pb2_grpc.MapReduceStub(channel)

    # Map phase
    map_request = mapreduce_pb2.MapRequest(input_data="fuddu Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo Fijo")
    map_response = stub.Map(map_request)
    print("Mapped data:", map_response.mapped_data)

    # Reduce phase
    reduce_request = mapreduce_pb2.ReduceRequest(mapped_data=map_response.mapped_data)
    reduce_response = stub.Reduce(reduce_request)
    print("Reduced data:", reduce_response.reduced_data)

if __name__ == '__main__':
    run()
    