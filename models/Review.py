from air_bnb.models.base_class import BaseModel

"""
Module for the Review class.
"""


class Review(BaseModel):
    """Represent a review.

        Attributes:
            place_id (str): The Place id.
            user_id (str): The User id.
            text (str): The text of the review.
        """
    place_id = ""
    user_id = ""
    text = ""

