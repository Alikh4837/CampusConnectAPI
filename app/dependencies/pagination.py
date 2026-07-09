from fastapi import Query


class PaginationParams():
    def __init__(self,limit:int,offset:int):
        self.limit=limit
        self.offset=offset

def Paginate(
    limit:int=Query(10),
    offset:int=Query(0)
):
    return PaginationParams(
        limit=limit,
        offset=offset
    )