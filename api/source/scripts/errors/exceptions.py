class APIException(Exception):
    status_code: int
    code: str
    msg: str
    detail: str

    def __init__(
            self,
            *,  #키워드 전용 인자, 이후 모든 매개변수는 키워드 인자로 전달되어야 함
            status_code: int = 0,
            code: str = "-1",
            msg: str = None,
            detail: str = None,
            ex: Exception = None,
    ):
        self.status_code = status_code
        self.code = code
        self.msg = msg
        self.detail = detail
        super().__init__(ex)


