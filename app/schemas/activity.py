from pydantic import UUID1, BaseModel, EmailStr


class ActivitySchema(BaseModel):
    """
    Base Activity Schema
    """

    name: str
    config_url: str
    json_params_url: str
    user_url: str
    analytics_url: str
    analytics_list_url: str