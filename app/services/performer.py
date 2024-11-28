import json
from typing import List, Optional
from app.models.performer import Performer, PerformerUpdate
from fastapi import HTTPException
import fcntl


def does_performer_exist(performers: List[Performer],
                         display_name: str) -> bool:
    """
    Check if a performer already exists by their display name.
    :param performers:      List of all active performers.
    :param display_name:    The display name of the performer.
    :return: True if the performer already exists, otherwise False.
    """
    for performer in performers:
        if performer.display_name == display_name:
            return True
    return False


class PerformerService:
    def __init__(self, file_path: str = "app/data/performers.json"):
        """
        Initialize the PerformerService with a file path.
        :param file_path: Path to the JSON file for storing performers.
        """
        self.file_path = file_path

    def _load_performers(self) -> List[Performer]:
        """
        Load all performers from the JSON file.
        :return: A list of Performer objects.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Performer(**performer) for performer in data]
        except FileNotFoundError:
            return []

    def _save_performers(self, performers: List[Performer]) -> None:
        """
        Save all performers to the JSON file.
        :param performers: A list of Performer objects to save.
        """
        with open(self.file_path, "w") as file:
            # Lock the file before writing (LOCK_EX = exclusive lock)
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            try:
                json.dump([performer.dict() for performer in performers], file, indent=4)
            finally:
                fcntl.flock(file.fileno(), fcntl.LOCK_UN)  # Unlock the file

    def get_all_performers(self) -> List[Performer]:
        """
        Retrieve all performers.
        :return: A list of all Performer objects.
        """
        return self._load_performers()

    def get_performer_by_id(self, performer_id: int) -> Optional[Performer]:
        """
        Retrieve a performer by their ID.
        :param performer_id: The ID of the performer to retrieve.
        :return: The Performer object if found, None otherwise.
        """
        performers = self._load_performers()
        for performer in performers:
            if performer.id == performer_id:
                return performer
        return None

    def get_performers_by_city(self, city: str) -> List[Performer]:
        """
        Get all performers in a specific city.
        :param city: The city in which to search for performers.
        :return: A list of performers in the specified city.
        """
        performers = self._load_performers()
        filtered_performers = [
            performer for performer in performers if performer.city and performer.city.lower() == city.lower()
        ]
        return filtered_performers if filtered_performers else []

    def add_performer(self, performer: Performer) -> Performer:
        """
        Add a new performer to the list.
        :param performer: The performer to be added.
        :return: The added performer with its unique ID.
        """
        performers = self._load_performers()

        # Check if the display name already exists
        if does_performer_exist(performers, performer.display_name):
            raise HTTPException(status_code=400, detail="Display name already taken.")

        # Assign an ID by auto-incrementing the highest ID in the existing performers
        new_id = max([p.id for p in performers], default=0) + 1  # Increment the ID
        performer.id = new_id  # Assign the incremented ID to the new performer

        # Add the new performer to the list
        performers.append(performer)
        self._save_performers(performers)

        return performer

    def update_performer(self, performer_id: int, updated_performer: PerformerUpdate) -> Optional[Performer]:
        """
        Update the details of an existing performer.
        :param performer_id: The ID of the performer to update.
        :param updated_performer: The updated Performer object.
        :return: The updated Performer object if successful, None otherwise.
        """
        performers = self._load_performers()
        for index, performer in enumerate(performers):
            if performer.id == performer_id:
                # Loop through the fields of the updated performer and update only the provided fields
                for field, value in updated_performer.dict(exclude_unset=True).items():
                    setattr(performer, field, value)

                # Save the updated performers list
                self._save_performers(performers)
                return performer

        return None

    def delete_performer_by_id(self, performer_id: int) -> bool:
        """
        Delete a performer by their ID.
        :param performer_id: The ID of the performer to delete.
        :return: True if the performer was deleted, False otherwise.
        """
        performers = self._load_performers()
        for index, performer in enumerate(performers):
            if performer.id == performer_id:
                del performers[index]
                self._save_performers(performers)
                return True
        return False

