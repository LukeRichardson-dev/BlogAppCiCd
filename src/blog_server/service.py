from grpc_out.blog_pb2_grpc import BlogServiceServicer
from grpc_out import blog_pb2


class Blog(BlogServiceServicer):

    def getPosts(self, request, context):
        blog_pb2

        return blog_pb2.GetPostsResponse(name='')

    def getPostCount(self, request, context):
        ...

    def createPost(self, request, context):
        ...
