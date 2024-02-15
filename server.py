# server.py

import grpc
from concurrent import futures
import mapreduce_pb2
import mapreduce_pb2_grpc
from collections import Counter

class MapReduceServicer(mapreduce_pb2_grpc.MapReduceServicer):
    def Map(self, request, context):
        mapped_data = [word.upper() for word in request.input_data.split()]
        return mapreduce_pb2.MapResponse(mapped_data=mapped_data)

    def Reduce(self, request, context):
        word_count = Counter(request.mapped_data)
        reduced_data = ""
        for word, count in word_count.items():
            reduced_data += f"'{word}' {count}\n"
        return mapreduce_pb2.ReduceResponse(reduced_data=reduced_data.strip())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mapreduce_pb2_grpc.add_MapReduceServicer_to_server(MapReduceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
