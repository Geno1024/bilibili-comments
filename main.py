import json
import re
from collections import namedtuple
from typing import List

import requests

from replyobject import ReplyObject


def get_comment(aid: int, page: int) -> ReplyObject:
    print(f"Getting page {page}")
    return json.loads(requests.get(f"https://api.bilibili.com/x/v2/reply/main?mode=3&next={page}&oid={aid}&plat=1&type=1").text, object_hook=lambda ds: namedtuple('X', [re.sub(r"^\d", "N", re.sub(r"\[|\]|/|\?|:|=|&|-|\.| ", "", r)) for r in ds.keys()])(*ds.values()))


def get_comments(aid: int) -> List[ReplyObject.Data.Reply]:
    page = 1
    reply_object = get_comment(aid, page)
    replies = reply_object.data.replies
    while not reply_object.data.cursor.is_end:
        page += 1
        reply_object = get_comment(aid, page)
        replies += reply_object.data.replies
    typecast = [ReplyObject.Data.Reply(*r) for r in replies]
    return typecast


if __name__ == '__main__':
    get_comments(948058403)
    get_comments(777785654)

