from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
import typing as t
from fastapi import Depends, Header, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

app = FastAPI()

time_table_mapper = {
    0: "00:00-00:30",
    1: "00:30-01:00",
    2: "01:00-01:30",
    3: "01:30-02:00",
    4: "02:00-02:30",
    5: "02:30-03:00",
    6: "03:00-03:30",
    7: "03:30-04:00",
    8: "04:00-04:30",
    9: "04:30-05:00",
    10: "05:00-05:30",
    11: "05:30-06:00",
    12: "06:00-06:30",
    13: "06:30-07:00",
    14: "07:00-07:30",
    15: "07:30-08:00",
    16: "08:00-08:30",
    17: "08:30-09:00",
    18: "09:00-09:30",
    19: "09:30-10:00",
    20: "10:00-10:30",
    21: "10:30-11:00",
    22: "11:00-11:30",
    23: "11:30-12:00",
    24: "12:00-12:30",
    25: "12:30-13:00",
    26: "13:00-13:30",
    27: "13:30-14:00",
    28: "14:00-14:30",
    29: "14:30-15:00",
    30: "15:00-15:30",
    31: "15:30-16:00",
    32: "16:00-16:30",
    33: "16:30-17:00",
    34: "17:00-17:30",
    35: "17:30-18:00",
    36: "18:00-18:30",
    37: "18:30-19:00",
    38: "19:00-19:30",
    39: "19:30-20:00",
    40: "20:00-20:30",
    41: "20:30-21:00",
    42: "21:00-21:30",
    43: "21:30-22:00",
    44: "22:00-22:30",
    45: "22:30-23:00",
    46: "23:00-23:30",
    47: "23:30-00:00",
}

known_tokens = set(["token_floatnarakeiei"])
get_bearer_token = HTTPBearer(auto_error=False)

class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"

async def get_token(auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),) -> str:
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
        )
    return token

@app.get("/", tags=["Plublic"])
def hello_imc():
    return {"msg": "Frontend API testing of IMC booking system"}

@app.get("/availabletime", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def availabletime(token: str = Depends(get_token)):
    return {
        "00:00-00:30": {"status": False, "time_index": 0},
        "00:30-01:00": {"status": False, "time_index": 1},
        "01:00-01:30": {"status": False, "time_index": 2},
        "01:30-02:00": {"status": False, "time_index": 3},
        "02:00-02:30": {"status": False, "time_index": 4},
        "02:30-03:00": {"status": False, "time_index": 5},
        "03:00-03:30": {"status": False, "time_index": 6},
        "03:30-04:00": {"status": False, "time_index": 7},
        "04:00-04:30": {"status": False, "time_index": 8},
        "04:30-05:00": {"status": False, "time_index": 9},
        "05:00-05:30": {"status": False, "time_index": 10},
        "05:30-06:00": {"status": False, "time_index": 11},
        "06:00-06:30": {"status": False, "time_index": 12},
        "06:30-07:00": {"status": False, "time_index": 13},
        "07:00-07:30": {"status": False, "time_index": 14},
        "07:30-08:00": {"status": False, "time_index": 15},
        "08:00-08:30": {"status": True, "time_index": 16, "booking_id": "imc56786547373882764674"},
        "08:30-09:00": {"status": True, "time_index": 17, "booking_id": "imc56786547373882764674"},
        "09:00-09:30": {"status": True, "time_index": 18, "booking_id": "imc56786547373882764674"},
        "09:30-10:00": {"status": False, "time_index": 19},
        "10:00-10:30": {"status": False, "time_index": 20},
        "10:30-11:00": {"status": False, "time_index": 21},
        "11:00-11:30": {"status": False, "time_index": 22},
        "11:30-12:00": {"status": False, "time_index": 23},
        "12:00-12:30": {"status": True, "time_index": 24, "booking_id": "imc56786547373882764674"},
        "12:30-13:00": {"status": True, "time_index": 25, "booking_id": "imc56786547373882764674"},
        "13:00-13:30": {"status": True, "time_index": 26, "booking_id": "imc56786547373882764674"},
        "13:30-14:00": {"status": True, "time_index": 27, "booking_id": "imc56786547373882764674"},
        "14:00-14:30": {"status": True, "time_index": 28, "booking_id": "imc56786547373882764674"},
        "14:30-15:00": {"status": False, "time_index": 29},
        "15:00-15:30": {"status": False, "time_index": 30},
        "15:30-16:00": {"status": False, "time_index": 31},
        "16:00-16:30": {"status": False, "time_index": 32},
        "16:30-17:00": {"status": False, "time_index": 33},
        "17:00-17:30": {"status": False, "time_index": 34},
        "17:30-18:00": {"status": False, "time_index": 35},
        "18:00-18:30": {"status": False, "time_index": 36},
        "18:30-19:00": {"status": False, "time_index": 37},
        "19:00-19:30": {"status": False, "time_index": 38},
        "19:30-20:00": {"status": False, "time_index": 39},
        "20:00-20:30": {"status": False, "time_index": 40},
        "20:30-21:00": {"status": False, "time_index": 41},
        "21:00-21:30": {"status": False, "time_index": 42},
        "21:30-22:00": {"status": False, "time_index": 43},
        "22:00-22:30": {"status": False, "time_index": 44},
        "22:30-23:00": {"status": False, "time_index": 45},
        "23:00-23:30": {"status": False, "time_index": 46},
        "23:30-00:00": {"status": False, "time_index": 47}
    }

class Booking(BaseModel):
    booking_time_index: List[int]
    event: str
    band_name: str
    telephone: str
    booker_id: str

@app.post("/booking", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
async def booking(book: Booking, token: str = Depends(get_token)):
    return {
        "booking_id": "imc56786547373882764674",
        "booking_status": False,
        "booking_time": book.booking_time_index,
        "event": book.event,
        "band_name": book.band_name,
        "telephone": book.telephone,
        "booker_id": book.booker_id
    }

@app.get("/getprofile", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def get_profile(token: str = Depends(get_token)):
    return {
        "student_id": "6532042321",
        "nickname": "float",
        "name": "chayoot kosiwanich",
        "booking_history": [
            {
                "date"  : "12 JUL 2023",
                "time"  : "10:30-12:00",
                "event" : "ลานกิจกรรม",
                "band"  : "pluto boy"
            },
            {
                "date"  : "13 JUL 2023",
                "time"  : "07:30-09:00",
                "event" : "ลานกิจกรรม",
                "band"  : "pluto boy"
            },
            {
                "date"  : "14 JUL 2023",
                "time"  : "08:30-14:00",
                "event" : "ลานกิจกรรม",
                "band"  : "pluto boy"
            }
        ]   
    }

class EditProfile(BaseModel):
    nickname: str
    name: str

@app.post("/editprofile", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def edit_profile(editprofile: EditProfile,token: str = Depends(get_token)):
    return editprofile

@app.get("/admin/availabletime", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def admin_availabletime(token: str = Depends(get_token)):
    return {
        "00:00-00:30": {"status": False, "time_index": 0},
        "00:30-01:00": {"status": False, "time_index": 1},
        "01:00-01:30": {"status": False, "time_index": 2},
        "01:30-02:00": {"status": False, "time_index": 3},
        "02:00-02:30": {"status": False, "time_index": 4},
        "02:30-03:00": {"status": False, "time_index": 5},
        "03:00-03:30": {"status": False, "time_index": 6},
        "03:30-04:00": {"status": False, "time_index": 7},
        "04:00-04:30": {"status": False, "time_index": 8},
        "04:30-05:00": {"status": False, "time_index": 9},
        "05:00-05:30": {"status": False, "time_index": 10},
        "05:30-06:00": {"status": False, "time_index": 11},
        "06:00-06:30": {"status": False, "time_index": 12},
        "06:30-07:00": {"status": False, "time_index": 13},
        "07:00-07:30": {"status": False, "time_index": 14},
        "07:30-08:00": {"status": False, "time_index": 15},
        "08:00-08:30": {"status": True, "time_index": 16, "booking_id": "imc56786547373882764674"},
        "08:30-09:00": {"status": True, "time_index": 17, "booking_id": "imc56786547373882764674"},
        "09:00-09:30": {"status": True, "time_index": 18, "booking_id": "imc56786547373882764674"},
        "09:30-10:00": {"status": False, "time_index": 19},
        "10:00-10:30": {"status": False, "time_index": 20},
        "10:30-11:00": {"status": False, "time_index": 21},
        "11:00-11:30": {"status": False, "time_index": 22},
        "11:30-12:00": {"status": False, "time_index": 23},
        "12:00-12:30": {"status": True, "time_index": 24, "booking_id": "imc56786547373882764674"},
        "12:30-13:00": {"status": True, "time_index": 25, "booking_id": "imc56786547373882764674"},
        "13:00-13:30": {"status": True, "time_index": 26, "booking_id": "imc56786547373882764674"},
        "13:30-14:00": {"status": True, "time_index": 27, "booking_id": "imc56786547373882764674"},
        "14:00-14:30": {"status": True, "time_index": 28, "booking_id": "imc56786547373882764674"},
        "14:30-15:00": {"status": False, "time_index": 29},
        "15:00-15:30": {"status": False, "time_index": 30},
        "15:30-16:00": {"status": False, "time_index": 31},
        "16:00-16:30": {"status": False, "time_index": 32},
        "16:30-17:00": {"status": False, "time_index": 33},
        "17:00-17:30": {"status": False, "time_index": 34},
        "17:30-18:00": {"status": False, "time_index": 35},
        "18:00-18:30": {"status": False, "time_index": 36},
        "18:30-19:00": {"status": False, "time_index": 37},
        "19:00-19:30": {"status": False, "time_index": 38},
        "19:30-20:00": {"status": False, "time_index": 39},
        "20:00-20:30": {"status": False, "time_index": 40},
        "20:30-21:00": {"status": False, "time_index": 41},
        "21:00-21:30": {"status": False, "time_index": 42},
        "21:30-22:00": {"status": False, "time_index": 43},
        "22:00-22:30": {"status": False, "time_index": 44},
        "22:30-23:00": {"status": False, "time_index": 45},
        "23:00-23:30": {"status": False, "time_index": 46},
        "23:30-00:00": {"status": False, "time_index": 47}
    }

class Providing(BaseModel):
    providing_time_index: List[int]

@app.post("/admin/providing", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
async def providing(provide: Providing, token: str = Depends(get_token)):

    result_providing = {}

    for time_index, time in time_table_mapper.items():
        if time_index in provide.providing_time_index:
            result_providing[time] = {"status": True, "time_index": time_index}
        else:
            result_providing[time] = {"status": False, "time_index": time_index}

    return result_providing

@app.patch("/admin/confirmbooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def confirm_booking(booking_id: str, token: str = Depends(get_token)):
    return {
        "booking_id": booking_id,
        "booking_status": True,
        "booking_time": ["13:00-13:30","13:30-14:00"],
        "event": "ลานกิจกรรม",
        "band_name": "pluto boy",
        "telephone": "0632156154",
        "booker_id": "user7594094844"
    }

@app.patch("/admin/cancelbooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def cancel_booking(booking_id: str, token: str = Depends(get_token)):
    return {
        "booking_id": booking_id,
        "booking_status": False,
        "booking_time": ["13:00-13:30","13:30-14:00"],
        "event": "ลานกิจกรรม",
        "band_name": "pluto boy",
        "telephone": "0632156154",
        "booker_id": "user7594094844"
    }

@app.delete("/admin/deletebooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def delete_booking(booking_id: str, token: str = Depends(get_token)):
    return {
        "booking_id": booking_id,
        "booking_status": True,
        "booking_time": ["13:00-13:30","13:30-14:00"],
        "event": "ลานกิจกรรม",
        "band_name": "pluto boy",
        "telephone": "0632156154",
        "booker_id": "user7594094844"
    }

@app.get("/admin/getbookinginfo/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def delete_booking(booking_id: str, token: str = Depends(get_token)):
    return {
        "booking_id": booking_id,
        "booking_status": True,
        "booking_time": ["13:00-13:30","13:30-14:00"],
        "event": "ลานกิจกรรม",
        "band_name": "pluto boy",
        "telephone": "0632156154",
        "booker_id": "user7594094844"
    }




