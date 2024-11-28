from fastapi import APIRouter, HTTPException
from app.models.venue import Venue, VenueUpdate
from app.services.venue import VenueService
from typing import List

# Initialize router and service
router = APIRouter()
venue_service = VenueService()


# Get a list of all venues
@router.get("/", response_model=List[Venue])
def get_venues():
    """
    Retrieve all venues.
    :return: A list of venue objects.
    """
    return venue_service.get_all_venues()


@router.get("/{venue_id}", response_model=Venue)
async def get_venue_by_id(venue_id: str):
    """
    Retrieve a venue by its ID.
    :param venue_id: The unique ID of the venue.
    :return: The venue object corresponding to the given ID.
    """
    try:
        venue_id = int(venue_id)
    except ValueError:
        raise HTTPException(status_code=400,
                            detail="Venue ID must be an integer.")

    try:
        venue = venue_service.get_venue_by_id(venue_id)
        if not venue:
            raise HTTPException(status_code=404, detail="Venue not found.")
        return venue
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid venue ID.")


@router.get("/city/{city}")
async def get_venues_by_city(city: str):
    """
    Get all venues located in a specific city.
    :param city: The city in which to search for venues.
    :return: A list of venues in the specified city.
    """
    venues = venue_service.get_venues_by_city(city)
    if venues is None:
        raise HTTPException(status_code=404,
                            detail="No venues found in the specified city.")
    return venues


# Create a new venue
@router.post("/add", response_model=Venue)
def add_venue(venue: Venue):
    """
    Add a new venue.
    :param venue: The venue object to be added.
    :return: The added venue object.
    """
    added_venue = venue_service.add_venue(venue)
    return added_venue


# Update a venue by ID
@router.put("/{venue_id}", response_model=Venue)
def update_venue(venue_id: int, venue: VenueUpdate):
    """
    Update a venue's details.
    :param venue_id: The unique ID of the venue to update.
    :param venue: The updated venue object.
    :return: The updated venue object.
    """
    updated_venue = venue_service.update_venue(venue_id, venue)
    if not updated_venue:
        raise HTTPException(status_code=404, detail="Venue not found.")
    return updated_venue


# Delete a venue by ID
@router.delete("/{venue_id}")
def delete_venue(venue_id: int):
    """
    Delete a venue by its ID.
    :param venue_id: The unique ID of the venue to delete.
    :return: A success message if the venue is deleted.
    """
    result = venue_service.delete_venue_by_id(venue_id)
    if not result:
        raise HTTPException(status_code=404, detail="Venue not found.")
    return {"message": f"Venue with ID {venue_id} deleted successfully."}
