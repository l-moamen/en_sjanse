from fastapi import APIRouter, HTTPException
from app.models.performer import Performer, PerformerUpdate
from app.services.performer import PerformerService
from typing import List

# Initialize router and service
router = APIRouter()
performer_service = PerformerService()


@router.get("/", response_model=List[Performer])
def get_performers():
    """
    Retrieve all performers.
    :return: A list of performer objects.
    """
    return performer_service.get_all_performers()


@router.get("/{performer_id}", response_model=Performer)
async def get_performer_by_id(performer_id: int):
    """
    Retrieve a performer by their ID.
    :param performer_id: The unique ID of the performer.
    :return: The performer object corresponding to the given ID.
    """
    performer = performer_service.get_performer_by_id(performer_id)
    if not performer:
        raise HTTPException(status_code=404, detail="Performer not found.")
    return performer


@router.get("/city/{city}", response_model=List[Performer])
async def get_performers_by_city(city: str):
    """
    Get all performers located in a specific city.
    :param city: The city in which to search for performers.
    :return: A list of performers in the specified city.
    """
    performers = performer_service.get_performers_by_city(city)
    if not performers:
        raise HTTPException(status_code=404, detail="No performers found in the specified city.")
    return performers


@router.post("/add", response_model=Performer)
def add_performer(performer: Performer):
    """
    Add a new performer.
    :param performer: The performer object to be added.
    :return: The added performer object.
    """
    added_performer = performer_service.add_performer(performer)
    return added_performer


@router.put("/{performer_id}", response_model=Performer)
def update_performer(performer_id: int, performer: PerformerUpdate):
    """
    Update a performer's details.
    :param performer_id: The unique ID of the performer to update.
    :param performer: The updated performer object.
    :return: The updated performer object.
    """
    updated_performer = performer_service.update_performer(performer_id, performer)
    if not updated_performer:
        raise HTTPException(status_code=404, detail="Performer not found.")
    return updated_performer


@router.delete("/{performer_id}")
def delete_performer(performer_id: int):
    """
    Delete a performer by their ID.
    :param performer_id: The unique ID of the performer to delete.
    :return: A success message if the performer is deleted.
    """
    result = performer_service.delete_performer_by_id(performer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Performer not found.")
    return {"message": f"Performer with ID {performer_id} deleted successfully."}
