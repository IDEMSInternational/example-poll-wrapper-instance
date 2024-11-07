from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel
from parenttext_pipeline.models.parenttext_models import *
from typing import List






class PollMetadataModel(DataRowModel):
    poll_type: str = ""
    poll_name: str = ""
	


class PollTypesModel(DataRowModel):
    registration_flow: str = ""
    excluded_user_group: str = ""




