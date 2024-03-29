"""Public API to a hypothetical simple cone search service."""

from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Response, Query
from fastapi.responses import RedirectResponse

from .models import (
    ConeSearchParameters,
    ErrorModel,
    ExecutionPhase,
    Job,
    JobCreate,
    JobDescription,
    JobStart,
    JobUpdate,
    Verbosity,
)

__all__ = ["router"]

#: FastAPI router for all handlers.
router = APIRouter()

#: Taken from the Simple Cone Search 1.03 specification.
_EXAMPLE_RESPONSE = """
<?xml version="1.0"?>
<!DOCTYPE VOTABLE SYSTEM "http://us-vo.org/xml/VOTable.dtd">
<VOTABLE version="1.0">
  <DEFINITIONS>
    <COOSYS system="eq_FK5" equinox="2000" />
  </DEFINITIONS>
    
  <RESOURCE ID="T9001">
     <DESCRIPTION>
       HEASARC Browse data service
       Please send inquiries to mailto:request@athena.gsfc.nasa.gov
    </DESCRIPTION>
    <PARAM ID="default_search_radius" ucd="OBS_ANG-SIZE" datatype="double" 
           value="0.0516666666666667" />

    <TABLE ID="heasarc_first_9001">
      <DESCRIPTION> Faint Images of the Radio Sky at Twenty cm Source Catalog (FIRST) </DESCRIPTION>
      
      <FIELD name="unique_id" datatype="char" arraysize="*"  ucd="ID_MAIN">
        <DESCRIPTION> Integer key </DESCRIPTION>
      </FIELD>
      
      <FIELD name="name" datatype="char" arraysize="*"  >
        <DESCRIPTION> FIRST Source Designation </DESCRIPTION>
      </FIELD>
      
      <FIELD name="ra" datatype="double" unit="degree" ucd="POS_EQ_RA_MAIN">
        <DESCRIPTION> Right Ascension </DESCRIPTION>
      </FIELD>
      
      <FIELD name="dec" datatype="double" unit="degree" ucd="POS_EQ_DEC_MAIN">
        <DESCRIPTION> Declination </DESCRIPTION>
      </FIELD>
      
      <FIELD name="flux_20_cm" datatype="double" unit="mJy" >
        <DESCRIPTION> Peak 1.4GHz Flux Density (mJy) </DESCRIPTION>
      </FIELD>
      
      <FIELD name="flux_20_cm_error" datatype="double" unit="mJy" >
        <DESCRIPTION> Estimated rms in at Source (mJy) </DESCRIPTION>
      </FIELD>
      
      <FIELD name="int_flux_20_cm" datatype="double" unit="mJy" >

        <DESCRIPTION> Integrated 1.4GHz Flux Density (mJy) </DESCRIPTION>
      </FIELD>
      
      <DATA>
        <TABLEDATA>
<TR>
  <TD>384559</TD><TD>FIRST J120002.6+595708</TD>
  <TD>180.0110042</TD><TD>59.9523889</TD>
  <TD>    1.11</TD><TD> 0.139</TD><TD>    1.14</TD>
</TR>
<TR>
  <TD>385094</TD><TD>FIRST J120025.3+600103</TD>
  <TD>180.1057250</TD><TD>60.0175556</TD>
  <TD>    2.89</TD><TD> 0.142</TD><TD>    2.56</TD>
</TR>
<TR>
  <TD>384928</TD><TD>FIRST J120018.1+600236</TD>
  <TD>180.0755500</TD><TD>60.0434750</TD>
  <TD>   19.38</TD><TD> 0.145</TD><TD>   19.23</TD>
</TR>
<TR>
  <TD>384490</TD><TD>FIRST J115959.4+600403</TD>
  <TD>179.9978875</TD><TD>60.0677083</TD>
  <TD>    1.01</TD><TD> 0.147</TD><TD>    1.20</TD>
</TR>
        </TABLEDATA>
      </DATA>
    </TABLE>

  </RESOURCE>
</VOTABLE>
"""


@router.get(
    "",
    description="Perform a simple cone search",
    response_class=Response,
    responses={
        200: {
            "content": {
                "text/xml;content=x-votable": {"example": _EXAMPLE_RESPONSE},
            }
        },
        400: {"description": "Search Out of Range", "model": ErrorModel},
        422: {"description": "Invalid Parameters", "model": ErrorModel},
    },
    summary="Cone search",
)
async def search_sync(
    ra: Annotated[
        float,
        Query(
            title="Right-ascension",
            description=(
                "A right-ascension in the ICRS coordinate system for the"
                " positon of the center of the cone to search, given in"
                " decimal degrees"
            ),
            examples=[179.5],
        )
    ],
    dec: Annotated[
        float,
        Query(
            title="Declination",
            description=(
                "A declination in the ICRS coordinate system for the positon"
                " of the center of the cone to search, given in decimal"
                " degrees"
            ),
            examples=[59.98],
        )
    ],
    sr: Annotated[
        float,
        Query(
            title="Search radius",
            description=(
                "The radius of the cone to search, given in decimal degrees"
            ),
            examples=[0.5],
        )
    ],
    verb: Annotated[
        Verbosity,
        Query(
            title="Verbosity",
            description=(
                "Choose from `minimum` (minimum columns required to describe"
                " the object), `all` (all available columns), or `default`"
                " (a useful intermediate number of columns)"
            ),
            examples=[Verbosity.ALL],
        )
    ] = Verbosity.DEFAULT,
) -> Response:
    ...


@router.post(
    "",
    description="Perform a simple cone search",
    response_class=Response,
    responses={
        200: {
            "content": {
                "text/xml;content=x-votable": {"example": _EXAMPLE_RESPONSE},
            }
        },
        400: {"description": "Search Out of Range", "model": ErrorModel},
        422: {"description": "Invalid Parameters", "model": ErrorModel},
    },
    summary="Cone search",
)
async def search_sync(params: ConeSearchParameters) -> Response:
    ...


@router.get(
    "/jobs",
    description=(
        "List all existing jobs for the current user. Jobs will be sorted"
        " by creation date, with the most recently created listed first."
    ),
    response_model=list[JobDescription],
    response_model_exclude_none=True,
    summary="Cone search job list",
)
async def get_job_list(
    phase: Annotated[
        list[ExecutionPhase] | None,
        Query(
            title="Execution phase",
            description="Limit results to the provided execution phases",
        )
    ] = None,
    after: Annotated[
        datetime | None,
        Query(
            title="Creation date",
            description="Limit results to jobs created after this date",
        ),
    ] = None,
    last: Annotated[
        int | None,
        Query(
            title="Number of jobs",
            description="Return at most the given number of jobs",
        ),
    ] = None,
) -> list[JobDescription]:
    ...


@router.post(
    "/jobs",
    response_class=RedirectResponse,
    status_code=303,
    summary="Create async cone search job",
)
async def create_job(create: JobCreate[ConeSearchParameters]) -> str:
    ...


@router.get(
    "/jobs/{job_id}",
    response_model=Job[ConeSearchParameters],
    response_model_exclude_none=True,
    summary="Cone search job details",
)
async def get_job(
    job_id: str,
    wait: Annotated[
        int,
        Query(
            title="Wait for status changes",
            description=(
                "Maximum number of seconds to wait or -1 to wait for as long"
                " as the server permits"
            ),
            examples=[-1, 60]
        ),
    ],
    phase: Annotated[
        ExecutionPhase,
        Query(
            title="Initial phase for waiting",
            description=(
                "When waiting for status changes, consider this to be the"
                " initial execution phase. If the phase has already changed,"
                " return immediately. This parameter should always be provided"
                " when wait is used."
            ),
            examples=[ExecutionPhase.EXECUTING],
        ),
    ]
) -> Job[ConeSearchParameters]:
    ...


@router.delete(
    "/jobs/{job_id}",
    status_code=204,
    summary="Delete a cone search job",
)
async def delete_job(job_id: str) -> None:
    ...


@router.patch(
    "/jobs/{job_id}",
    status_code=200,
    response_model=Job[ConeSearchParameters],
    response_model_exclude_none=True,
    summary="Update a cone search job",
)
async def patch_job(job_id: str, update: JobUpdate) -> Job:
    ...


@router.post(
    "/jobs/{job_id}/start",
    response_class=RedirectResponse,
    status_code=303,
    summary="Start a cone search job",
)
async def job_start(job_id: str, start: JobStart) -> str:
    ...
