from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from adapter import Strapi, geo_sort, schemas, database
from adapter.domain import crud,mongo_db

import requests
import json

router = APIRouter(      
    prefix="/api/user",
    responses={ 
        404 : {
            'message': 'Not Found'
        }
    }
)
strapi = Strapi()
mongoDB = mongo_db.MongoDB()

@router.get("/me")
def getuser(request: Request):
    return strapi.getProject(request)

# @router.post("/commit/", response_model=list[schemas.JobBase])
# async def commit_job(data: geo_sort.FeatureCollection, db: Session = Depends(database.get_db)):
#     try:
#         processed_data = geo_sort.Data01(data.dict())
#         if not processed_data:
#             raise HTTPException(status_code=400, detail="No data processed")
#         db_items = []
#         for item in processed_data:
#             try:
#                 list_item = schemas.JobCreate(
#                     project=item['Project'],
#                     hotspot_type=item['hotspot_type'],
#                     max_temp=item['Max Temperature'],
#                     string_tag=item['string_tag'],
#                     priority=item['priority']
#                 )
#                 db_item = crud.job_crud.create_Job(db=db, list=list_item)
#                 db_items.append(db_item)
#             except Exception as e:
#                 print(f"Error processing item: {item}")
#                 print(f"Exception: {e}")
#                 raise HTTPException(status_code=500, detail="Error inserting data into database")
#         return db_items
#     except Exception as e:
#         print(f"Error processing data: {e}")
#         raise HTTPException(status_code=400, detail="Error processing data")

# @router.post("/commit/", response_model=list[schemas.JobBase])
# async def commit_job(data: geo_sort.FeatureCollection,request: Request):
#     try:
#         a = strapi.getProject(request)
#         processed_data = geo_sort.Data01(data.dict())
#         if not processed_data:
#             raise HTTPException(status_code=400, detail="No data processed")
#         db_items = []
#         for item in processed_data:
#             try:
#                 list_item = schemas.JobCreate(
#                     project=item['Project'],
#                     hotspot_type=item['hotspot_type'],
#                     max_temp=item['Max Temperature'],
#                     string_tag=item['string_tag'],
#                     priority=item['priority']
#                 )
#                 db_items.append(list_item)
#             except Exception as e:
#                 print(f"Error processing item: {item}")
#                 print(f"Exception: {e}")
#                 raise HTTPException(status_code=500, detail="Error inserting data into database")
#         return db_items
#     except Exception as e:
#         print(f"Error processing data: {e}")
#         raise HTTPException(status_code=400, detail="Error processing data")


@router.get("/mongo/{token}")
def read_mongo(token: str,request: Request):
    info = strapi.getProject(request)
    result = mongoDB.load_json(token)
    if result is not None:   
        list_cur = list(result) 
    else:
        list_cur = []
    filtered_list = [item for item in list_cur if item.get("roi")]
    # filtered_list =filtered_list[5]
    dataDB = []
    # for item in : filtered_list
    #         try:
    #             list_item = schemas.JobCreate(  
    #                 project=item['Project'],
    #                 hotspot_type=item['hotspot_type'],
    #                 max_temp=item['Max Temperature'],
    #                 string_tag=item['string_tag'],
    #                 priority=item['priority']
    #             )
    #             db_items.append(list_item)
    
    # print(filtered_list['url'])
    return str(filtered_list)
