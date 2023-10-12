import graphene

import apps.core.schema
import apps.factions.CSM.schema


class Query(apps.core.schema.Query,
            apps.factions.CSM.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
