# coding: utf-8

"""
    Universal Worker Service (UWS)

    The Universal Worker Service (UWS) pattern defines how to manage asynchronous execution of jobs on a service.

    The version of the OpenAPI document: 1.2
    Contact: grid@ivoa.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uws_server.models.error_summary import ErrorSummary
from uws_server.models.execution_phase import ExecutionPhase
from uws_server.models.parameters import Parameters
from uws_server.models.results import Results
from uws_server.models.uws_version import UWSVersion
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class JobSummary(BaseModel):
    """
    The complete representation of the state of a job 
    """ # noqa: E501
    job_id: StrictStr = Field(description="The identifier for the job ", alias="jobId")
    run_id: Optional[StrictStr] = Field(default=None, description="this is a client supplied identifier - the UWS system does nothing other than to return it as part of the description of the job ", alias="runId")
    owner_id: Optional[StrictStr] = Field(default=None, description="The owner (creator) of the job - this should be expressed as a string that can be parsed in accordance with IVOA security standards. If there was no authenticated job creator then this should be set to NULL. ", alias="ownerId")
    phase: Optional[ExecutionPhase] = None
    quote: Optional[datetime] = Field(default=None, description="A Quote predicts when the job is likely to complete - returned at /{jobs}/{job_id}/quote \"don't know\" is encoded by setting to the XML null value xsi:nil=\"true\" ")
    creation_time: Optional[datetime] = Field(default=None, description="The instant at which the job was created.  Note that the version 1.1 of the specification requires that this element be present. It is optional only in versions 1.x of the schema for backwards compatibility. 2.0+ versions of the schema will make this formally mandatory in an XML sense. ", alias="creationTime")
    start_time: Optional[datetime] = Field(default=None, description="The instant at which the job started execution. ", alias="startTime")
    end_time: Optional[datetime] = Field(default=None, description="The instant at which the job finished execution. ", alias="endTime")
    execution_duration: Optional[StrictInt] = Field(default=None, description="The duration (in seconds) for which the job should be allowed to run - a value of 0 is intended to mean unlimited - returned at /{jobs}/{job_id}/executionduration ", alias="executionDuration")
    destruction: Optional[datetime] = Field(default=None, description="The time at which the whole job + records + results will be destroyed. Returned at /{jobs}/{job_id}/destruction ")
    parameters: Optional[Parameters] = None
    results: Optional[Results] = None
    error_summary: Optional[ErrorSummary] = Field(default=None, alias="errorSummary")
    job_info: Optional[StrictStr] = Field(default=None, description="This is arbitrary information that can be added to the job description by the UWS implementation. ", alias="jobInfo")
    version: Optional[UWSVersion] = None
    __properties: ClassVar[List[str]] = ["jobId", "runId", "ownerId", "phase", "quote", "creationTime", "startTime", "endTime", "executionDuration", "destruction", "parameters", "results", "errorSummary", "jobInfo", "version"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_summary
        if self.error_summary:
            _dict['errorSummary'] = self.error_summary.to_dict()
        # set to None if owner_id (nullable) is None
        # and model_fields_set contains the field
        if self.owner_id is None and "owner_id" in self.model_fields_set:
            _dict['ownerId'] = None

        # set to None if quote (nullable) is None
        # and model_fields_set contains the field
        if self.quote is None and "quote" in self.model_fields_set:
            _dict['quote'] = None

        # set to None if start_time (nullable) is None
        # and model_fields_set contains the field
        if self.start_time is None and "start_time" in self.model_fields_set:
            _dict['startTime'] = None

        # set to None if end_time (nullable) is None
        # and model_fields_set contains the field
        if self.end_time is None and "end_time" in self.model_fields_set:
            _dict['endTime'] = None

        # set to None if destruction (nullable) is None
        # and model_fields_set contains the field
        if self.destruction is None and "destruction" in self.model_fields_set:
            _dict['destruction'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobId": obj.get("jobId"),
            "runId": obj.get("runId"),
            "ownerId": obj.get("ownerId"),
            "phase": obj.get("phase"),
            "quote": obj.get("quote"),
            "creationTime": obj.get("creationTime"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "executionDuration": obj.get("executionDuration"),
            "destruction": obj.get("destruction"),
            "parameters": Parameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "results": Results.from_dict(obj.get("results")) if obj.get("results") is not None else None,
            "errorSummary": ErrorSummary.from_dict(obj.get("errorSummary")) if obj.get("errorSummary") is not None else None,
            "jobInfo": obj.get("jobInfo"),
            "version": obj.get("version")
        })
        return _obj

