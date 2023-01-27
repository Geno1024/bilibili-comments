import json

from typing import List


class ReplyObject:
    class Data:
        class Cursor:
            def __init__(
                    self,
                    is_begin: bool,
                    prev: int,
                    next: int,
                    is_end: bool,
                    all_count: int,
                    mode: int,
                    support_mode: List[int],
                    name: str,
            ):
                self.is_begin = is_begin
                self.prev = prev
                self.next = next
                self.is_end = is_end
                self.all_count = all_count
                self.mode = mode
                self.support_mode = support_mode
                self.name = name

        class Reply:
            class SReply:
                class Member:
                    """
                    This is a bad design.
                    """
                    class LevelInfo:
                        def __init__(
                                self,
                                current_level: int,
                                current_min: int,
                                current_exp: int,
                                next_exp: int
                        ):
                            self.current_level = current_level
                            self.current_min = current_min
                            self.current_exp = current_exp
                            self.next_exp = next_exp

                    def __init__(
                            self,
                            mid: str,
                            uname: str,
                            sex: str,
                            sign: str,
                            avatar: str,
                            rank: str,
                            face_nft_new: int,
                            is_senior_member: int,
                            level_info: LevelInfo,
                            pendant: object,
                            nameplate: object,
                            official_verify: object,
                            vip: object,
                            fans_detail: str,
                            user_sailing: object,
                            is_contractor: bool,
                            contract_desc: str,
                            nft_interaction: str,
                            avatar_item: object,
                    ):
                        self.mid = mid
                        self.uname = uname
                        self.sex = sex
                        self.sign = sign
                        self.avatar = avatar
                        self.rank = rank
                        self.face_nft_new = face_nft_new
                        self.is_senior_member = is_senior_member
                        self.level_info = level_info
                        self.pendant = pendant
                        self.nameplate = nameplate
                        self.official_verify = official_verify
                        self.vip = vip
                        self.fans_detail = fans_detail
                        self.user_sailing = user_sailing
                        self.is_contractor = is_contractor
                        self.contract_desc = contract_desc
                        self.nft_interaction = nft_interaction
                        self.avatar_item = avatar_item

                class Content:
                    def __init__(
                            self,
                            message: str,
                            members: List[object],
                            emote: object,
                            jump_url: object,
                            max_line: int,
                            at_name_to_mid: object,
                            rich_text: object,
                    ):
                        self.message = message
                        self.members = members
                        self.emote = emote
                        self.jump_url = jump_url
                        self.max_line = max_line
                        self.at_name_to_mid = at_name_to_mid
                        self.rich_text = rich_text

                def __init__(
                        self,
                        rpid: int,
                        oid: int,
                        type: int,
                        mid: int,
                        root: int,
                        parent: int,
                        dialog: int,
                        count: int,
                        rcount: int,
                        state: int,
                        fansgrade: int,
                        attr: int,
                        ctime: int,
                        rpid_str: str,
                        root_str: str,
                        parent_str: str,
                        like: int,
                        action: int,
                        member: Member,
                        content: Content,
                        replies: object,
                        assist: int,
                        up_action: object,
                        invisible: bool,
                        card_label: List[object],
                        reply_control: object,
                        folder: object,
                        dynamic_id_str: str = None
                ):
                    self.rpid = rpid
                    self.oid = oid
                    self.type = type
                    self.mid = mid
                    self.root = root
                    self.parent = parent
                    self.dialog = dialog
                    self.count = count
                    self.rcount = rcount
                    self.state = state
                    self.fansgrade = fansgrade
                    self.attr = attr
                    self.ctime = ctime
                    self.rpid_str = rpid_str
                    self.root_str = root_str
                    self.parent_str = parent_str
                    self.like = like
                    self.action = action
                    self.member = member
                    self.content = content
                    self.replies = replies
                    self.assist = assist
                    self.up_action = up_action
                    self.invisible = invisible
                    self.card_label = card_label
                    self.reply_control = reply_control
                    self.folder = folder
                    self.dynamic_id_str = dynamic_id_str

                def __str__(self):
                    return json.dumps({
                        "member": {
                            "id": self.member.mid,
                            "name": self.member.uname,
                            "level": self.member.level_info.current_level
                        },
                        "message": self.content.message
                    }, ensure_ascii=False)

            def __init__(
                    self,
                    rpid: int,
                    oid: int,
                    type: int,
                    mid: int,
                    root: int,
                    parent: int,
                    dialog: int,
                    count: int,
                    rcount: int,
                    state: int,
                    fansgrade: int,
                    attr: int,
                    ctime: int,
                    rpid_str: str,
                    root_str: str,
                    parent_str: str,
                    like: int,
                    action: int,
                    member: SReply.Member,
                    content: SReply.Content,
                    replies: List[SReply],
                    assist: int,
                    up_action: object,
                    invisible: bool,
                    card_label: List[object],
                    reply_control: object,
                    folder: object,
                    dynamic_id_str: str = None
            ):
                self.rpid = rpid
                self.oid = oid
                self.type = type
                self.mid = mid
                self.root = root
                self.parent = parent
                self.dialog = dialog
                self.count = count
                self.rcount = rcount
                self.state = state
                self.fansgrade = fansgrade
                self.attr = attr
                self.ctime = ctime
                self.rpid_str = rpid_str
                self.root_str = root_str
                self.parent_str = parent_str
                self.like = like
                self.action = action
                self.member = member
                self.content = content
                self.replies = replies
                self.assist = assist
                self.up_action = up_action
                self.invisible = invisible
                self.card_label = card_label
                self.reply_control = reply_control
                self.folder = folder
                self.dynamic_id_str = dynamic_id_str

            def __str__(self):
                return json.dumps({
                    "member": {
                        "id": self.member.mid,
                        "name": self.member.uname,
                        "level": self.member.level_info.current_level
                    },
                    "message": self.content.message,
                    "sub_reply": [json.loads(ReplyObject.Data.Reply.SReply(*s).__str__()) for s in self.replies] if self.replies is not None else []
                }, ensure_ascii=False)

        def __init__(
                self,
                cursor: Cursor,
                replies: List[Reply],
                top: object,
                top_replies: str,
                up_selection: object,
                effects: object,
                cm_info: object,
                assist: int,
                blacklist: int,
                vote: int,
                config: object,
                upper: object,
                control: object,
                note: int,
                callbacks: str
        ):
            self.cursor = cursor
            self.replies = replies
            self.top = top
            self.top_replies = top_replies
            self.up_selection = up_selection
            self.effects = effects
            self.cm_info = cm_info
            self.assist = assist
            self.blacklist = blacklist
            self.vote = vote
            self.config = config
            self.upper = upper
            self.control = control
            self.note = note
            self.callbacks = callbacks

    def __init__(
            self,
            code: int,
            message: str,
            ttl: int,
            data: Data
    ):
        self.code = code
        self.message = message
        self.ttl = ttl
        self.data = data

