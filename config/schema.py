import graphene
import feed.schema

schema = graphene.Schema(
    query=feed.schema.Query,
    mutation=feed.schema.Mutation
)
