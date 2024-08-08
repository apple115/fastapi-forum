

from fastapi import APIRouter

router=APIRouter()

@router.post("/{topic_id}/post_create")
def post_create(topic_id:int):
    return {"topic_id":topic_id}


@router.get("/{topic_id}/{post_id}")
def post_detail(topic_id:int,post_id:int):
    return {"topic_id":topic_id,"post_id":post_id}
