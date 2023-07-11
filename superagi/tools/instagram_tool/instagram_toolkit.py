from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit
from superagi.tools.instagram_tool.instagram import InstagramTool

class InstagramToolkit(BaseToolkit, ABC):
    name: str = "Instagram Toolkit"
    description: str = "Toolkit containing tools for performing posting photos on Instagram"

    def get_tools(self) -> List[BaseTool]:
        return [InstagramTool()]

    def get_env_keys(self) -> List[str]:
        return [
            "META_USER_ACCESS_TOKEN",
            "INSTAGRAM_BUSINESS_ACCOUNT_ID"
            # Add more config keys specific to your project
        ]