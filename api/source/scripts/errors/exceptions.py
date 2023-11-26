class APIException(Exception):
    status_code: int #200외 응답인 경우 서버 에러
    code: str #0이면 정상 응답, 그 외 커스텀 에러 코드로 전달되면 api 에러
    msg: str  #기본 메세지
    detail: str #상세 메세지

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

class UploadException(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
                status_code=200,
                code="100000",
                msg="파일 업로드 실패",
                ex=ex
        )

class InvalidImageException(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
                status_code=200,
                code="1000001",
                msg="유효하지 않은 이미지",
                ex=ex
        )
