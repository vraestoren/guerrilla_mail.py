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

    def get_email_address(self) -> dict:    
        response = self.session.get(
            f"{self.api}?f=get_email_address&lang={self.language}").json()
        self.sid_token = response["sid_token"]
        return response

    def set_email_user(self, email_user: str) -> dict:  
        response = self.session.get(
            f"{self.api}?f=set_email_user&email_user={email_user}&language={self.language}&sid_token={self.sid_token}").json()
        self.sid_token = response["sid_token"]
        return response

    def check_email(self, seq: int = 0) -> dict:    
        return self.session.get(
            f"{self.api}?f=check_email&seq={seq}&sid_token={self.sid_token}").json()

    def get_email_list(
            self, seq: int = None, offset: int = 0) -> dict: 
        params = {"seq": seq} if seq else {}
        return self.session.get(
            f"{self.api}?f=get_email_list&offset={offset}&sid_token={self.sid_token}",
            params=params).json()

    def fetch_email(self, email_id: int) -> dict:   
        return self.session.get(
            f"{self.api}?f=fetch_email&email_id={email_id}&sid_token={self.sid_token}").json()

    def delete_email(self, email_id: int) -> dict:  
        return self.session.get(
            f"{self.api}?f=del_email&email_ids[]={email_id}&sid_token={self.sid_token}").json()
