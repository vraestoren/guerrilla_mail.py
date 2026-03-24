from requests import Session

class GuerrillaMail:
    def __init__(self, language: str = "en") -> None:
        self.api = "https://api.guerrillamail.com/ajax.php"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
        self.sid_token = None
        self.language = language

    def _get(self, params: dict) -> dict:
        return self.session.get(self.api, params=params).json()

    def _with_sid(self, params: dict) -> dict:
        return {**params, "sid_token": self.sid_token}

    def get_email_address(self) -> dict:
        params = {
            "f": "get_email_address",
            "lang": self.language
        }
        response = self._get(params)
        self.sid_token = response["sid_token"]
        return response

    def set_email_user(self, email_user: str) -> dict:
        params = self._with_sid({
            "f": "set_email_user",
            "email_user": email_user,
            "language": self.language
        })
        response = self._get(params)
        self.sid_token = response["sid_token"]
        return response

    def check_email(self, seq: int = 0) -> dict:
        params = self._with_sid({
            "f": "check_email",
            "seq": seq
        })
        return self._get(params)

    def get_email_list(
            self, seq: int = None, offset: int = 0) -> dict:
        params = self._with_sid({
            "f": "get_email_list",
            "offset": offset
        })
        if seq:
            params["seq"] = seq
        return self._get(params)

    def fetch_email(self, email_id: int) -> dict:
        params = self._with_sid({
            "f": "fetch_email",
            "email_id": email_id
        })
        return self._get(params)

    def delete_email(self, email_id: int) -> dict:
        params = self._with_sid({
            "f": "del_email",
            "email_ids[]": email_id
        })
        return self._get(params)
