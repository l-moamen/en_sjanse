import json
from typing import List, Optional
from app.models.venue import Venue
from fastapi import HTTPException
import fcntl


class VenueService:

    def __init__(self, file_path: str = "app/data/venues.json"):
        """
        Initialize the VenueService with a file path.
        :param file_path: Path to the JSON file for storing venues.
        """
        self.file_path = file_path

    def _load_venues(self) -> List[Venue]:
        """
        Load all venues from the JSON file.
        :return: A list of Venue objects.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Venue(**venue) for venue in data]
        except FileNotFoundError:
            return []

    def _save_venues(self, venues: List[Venue]) -> None:
        """
        Save all venues to the JSON file.
        :param venues: A list of Venue objects to save.
        """
        with open(self.file_path, "w") as file:
            # Lock the file before writing (LOCK_EX = exclusive lock)
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            try:
                json.dump([venue.dict() for venue in venues], file, indent=4)
            finally:
                fcntl.flock(file.fileno(), fcntl.LOCK_UN)  # Unlock the file

    def get_venues_by_city(self, city: str):
        """
        Get all venues in a specific city.
        :param city: The city in which to search for venues.
        :return: A list of venues in the specified city.
        """
        venues = self._load_venues()
        filtered_venues = [
            venue for venue in venues if venue.city.lower() == city.lower()
        ]
        return filtered_venues if filtered_venues else None

    def add_venue(self, venue: Venue) -> Venue:
        """
        Add a new venue to the list.

        :param venue: The venue to be added.
        :return: The added venue with its unique ID.
        """
        venues = self._load_venues()

        # Check if the venue already exists
        if self.does_venue_exist(venue.name, venue.city, venue.country):
            raise HTTPException(status_code=400,
                                detail="Venue already exists.")

        # Assign an ID by auto-incrementing the highest ID in the existing venues
        new_id = max([v.id for v in venues], default=0) + 1  # Increment the ID
        venue.id = new_id  # Assign the incremented ID to the new venue
        print(new_id)
        print(type(new_id))

        # Add the new venue to the list
        venues.append(venue)
        self._save_venues(venues)

        return venue

    def does_venue_exist(self, name: str, city: str, country: str) -> bool:
        """
        Check if a venue already exists by its name, city, and country.

        :param name: The name of the venue.
        :param city: The city where the venue is located.
        :param country: The country where the venue is located.
        :return: True if the venue already exists, otherwise False.
        """
        venues = self._load_venues()
        for venue in venues:
            if venue.name == name and venue.city == city and venue.country == country:
                return True
        return False

    def get_all_venues(self) -> List[Venue]:
        """
        Retrieve all venues.
        :return: A list of all Venue objects.
        """
        return self._load_venues()

    def get_venue_by_id(self, venue_id: int) -> Optional[Venue]:
        """
        Retrieve a venue by its ID.
        :param venue_id: The ID of the venue to retrieve.
        :return: The Venue object if found, None otherwise.
        """
        venues = self._load_venues()
        for venue in venues:
            if venue.id == venue_id:
                return venue
        return None

    def update_venue(self, venue_id: int,
                     updated_venue: Venue) -> Optional[Venue]:
        """
        Update the details of an existing venue.
        :param venue_id: The ID of the venue to update.
        :param updated_venue: The updated Venue object.
        :return: The updated Venue object if successful, None otherwise.
        """
        venues = self._load_venues()
        for index, venue in enumerate(venues):
            if venue.id == venue_id:
                # Loop through the fields of the updated venue and update only the provided fields
                for field, value in updated_venue.dict(exclude_unset=True).items():
                    setattr(venue, field, value)

                # Save the updated venue list
                self._save_venues(venues)
                return venue

        return None

    def delete_venue_by_id(self, venue_id: int) -> bool:
        """
        Delete a venue by its ID.
        :param venue_id: The ID of the venue to delete.
        :return: True if the venue was deleted, False otherwise.
        """
        venues = self._load_venues()
        for index, venue in enumerate(venues):
            if venue.id == venue_id:
                del venues[index]
                self._save_venues(venues)
                return True
        return False
