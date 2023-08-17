from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
import typing as t
from fastapi import Depends, Header, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status
import re

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

def make_response(IsSuccess, data):
    template = {"isSuccess": IsSuccess}
    return dict(list(template.items()) + list(data.items()))

known_tokens = set(["token_floatnarakeiei"])
get_bearer_token = HTTPBearer(auto_error=False)

class UnauthorizedMessage(BaseModel):
    err: str = "Bearer token missing or unknown"

async def get_token(auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),) -> str:
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().err,
        )
    return token

@app.get("/", tags=["Plublic"])
def hello_imc():
    return {"msg": "Frontend API testing of IMC booking system"}

@app.get("booking/availabletime/{date}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def availabletime(date: str ,token: str = Depends(get_token)):
    """time format in YYYY-MM-DD ex. 2023-07-15"""

    date_format = True if re.match("^\d{4}-\d{2}-\d{2}$", date) else False
    
    if date_format:

        return make_response(True, {
            "date": date,
            "availableTime": {
                "07:00-07:30": {"timeIndex": 14},
                "07:30-08:00": {"timeIndex": 15},
                "09:30-10:00": {"timeIndex": 19},
                "10:00-10:30": {"timeIndex": 20},
                "10:30-11:00": {"timeIndex": 21},
                "11:00-11:30": {"timeIndex": 22},
                "11:30-12:00": {"timeIndex": 23},
                "14:30-15:00": {"timeIndex": 29},
                "15:00-15:30": {"timeIndex": 30},
                "15:30-16:00": {"timeIndex": 31},
                "16:00-16:30": {"timeIndex": 32},
                "16:30-17:00": {"timeIndex": 33},
                "17:00-17:30": {"timeIndex": 34},
                "17:30-18:00": {"timeIndex": 35}
            }
        })

    else:
        return make_response(False, {
            "err": "date format is incorrect",
        })

class Booking(BaseModel):
    bookingDate: str
    bookingTimeIndex: List[int]
    event: str
    bandName: str
    telephone: str
    bookerId: str

@app.post("/booking", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
async def booking(book: Booking, token: str = Depends(get_token)):
    """time format in YYYY-MM-DD ex. 2023-07-15"""

    date_format = True if re.match("^\d{4}-\d{2}-\d{2}$", book.booking_date) else False

    if date_format:
        return make_response(True, {
            "bookingId": "imc56786547373882764674",
            "bookingStatus": "pending",
            "bookingIime": book.booking_time_index,
            "date": book.booking_date,
            "event": book.event,
            "bandName": book.band_name,
            "telephone": book.telephone,
            "bookerId": book.booker_id
        })
    else:
        return make_response(False, {
            "err": "date format is incorrect",
        })

@app.get("/user/{id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def get_profile(id:str, token: str = Depends(get_token)):
    return make_response(True,{
        "userId": id,
        "studentId": "6532042321",
        "nickname": "float",
        "name": "chayoot kosiwanich",
        "bookingHistory": [
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
    })

class UpdateProfile(BaseModel):
    nickname: str
    name: str

@app.post("/user/updateprofile", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["User"])
def update_profile(updateprofileprofile: UpdateProfile,token: str = Depends(get_token)):
    return make_response(True, dict(updateprofile))

@app.get("/admin/availabletime/{date}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def admin_availabletime(date: str ,token: str = Depends(get_token)):
    """time format in YYYY-MM-DD ex. 2023-07-15"""
    date_format = True if re.match("^\d{4}-\d{2}-\d{2}$", date) else False
    
    if date_format:

        return make_response(True, {
            "date": date,
            "availableTime": {
                "07:00-07:30": {"timeIndex": 14},
                "07:30-08:00": {"timeIndex": 15},
                "09:30-10:00": {"timeIndex": 19},
                "10:00-10:30": {"timeIndex": 20},
                "10:30-11:00": {"timeIndex": 21},
                "11:00-11:30": {"timeIndex": 22},
                "11:30-12:00": {"timeIndex": 23},
                "14:30-15:00": {"timeIndex": 29},
                "15:00-15:30": {"timeIndex": 30},
                "15:30-16:00": {"timeIndex": 31},
                "16:00-16:30": {"timeIndex": 32},
                "16:30-17:00": {"timeIndex": 33},
                "17:00-17:30": {"timeIndex": 34},
                "17:30-18:00": {"timeIndex": 35}
            }
        })

    else:
        return make_response(False, {
            "err": "date format is incorrect",
        })

class Providing(BaseModel):
    providing_date: str
    providing_time_index: List[int]

@app.post("/admin/providing", status_code=201, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
async def providing(provide: Providing, token: str = Depends(get_token)):

    """time format in YYYY-MM-DD ex. 2023-07-15"""
    date_format = True if re.match("^\d{4}-\d{2}-\d{2}$", provide.providing_date) else False
    
    if date_format:
    
        result_providing = {}

        for time_index, time in time_table_mapper.items():
            if time_index in provide.providing_time_index:
                result_providing[time] = {"status": True, "timeIndex": time_index}
            else:
                result_providing[time] = {"status": False, "timeIndex": time_index}

        return make_response(True, result_providing)
    
    else:
        return make_response(False, {
            "err": "date format is incorrect",
        })

@app.patch("/admin/confirmbooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def confirm_booking(booking_id: str, token: str = Depends(get_token)):
    return make_response(True, {
            "bookingId": booking_id,
            "bookingStatus": "cancel",
            "bookingTime": ["13:00-13:30","13:30-14:00"],
            "date": "2023-12-22",
            "event": "ลานกิจกรรม",
            "bandName": "pluto boy",
            "telephone": "0632156154",
            "bookerId": "user7594094844"
        })

@app.patch("/admin/cancelbooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def cancel_booking(booking_id: str, token: str = Depends(get_token)):
    return make_response(True, {
            "bookingId": booking_id,
            "bookingStatus": "confirm",
            "bookingTime": ["13:00-13:30","13:30-14:00"],
            "date": "2023-12-22",
            "event": "ลานกิจกรรม",
            "bandName": "pluto boy",
            "telephone": "0632156154",
            "bookerId": "user7594094844"
        })

@app.delete("/admin/deletebooking/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def delete_booking(booking_id: str, token: str = Depends(get_token)):
    return make_response(True, {
            "bookingId": booking_id,
            "bookingStatus": "delete",
            "bookingTime": ["13:00-13:30","13:30-14:00"],
            "date": "2023-12-22",
            "event": "ลานกิจกรรม",
            "bandName": "pluto boy",
            "telephone": "0632156154",
            "bookerId": "user7594094844"
        })

@app.get("/admin/getbookinginfo/{booking_id}", status_code=200, responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)}, tags=["Admin"])
def delete_booking(booking_id: str, token: str = Depends(get_token)):
    return make_response(True, {
            "bookingId": booking_id,
            "bookingStatus": "confirm",
            "bookingTime": ["13:00-13:30","13:30-14:00"],
            "date": "2023-12-22",
            "event": "ลานกิจกรรม",
            "bandName": "pluto boy",
            "telephone": "0632156154",
            "bookerId": "user7594094844"
        })




