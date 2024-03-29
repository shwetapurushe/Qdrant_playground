# starter example from documentation

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from qdrant_client.http.models import UpdateStatus

client = QdrantClient("localhost", port=6333)
# client.recreate_collection(
#     collection_name="test_collection",
#     vectors_config=VectorParams(size=4, # size of vectors in the collection, all must be of same size
#                                 # is the output dimensionality of the encoding
#                                 distance=Distance.DOT)
# )

# operation_info = client.upsert(
#     collection_name="test_collection",
#     wait=True,
#     points=[
#         PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
#         PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": ["Berlin", "London"]}),
#         PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": ["Berlin", "Moscow"]}),
#         PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": ["London", "Moscow"]}),
#         PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"count": [0]}),
#         PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44]),
#     ]
# )

search_result = client.search(
    collection_name="test_collection",
    query_vector=[0.2, 0.1, 0.9, 0.7], 
    limit=3
)

print(search_result[2])