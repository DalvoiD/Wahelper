import graphene

from apps.core.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
