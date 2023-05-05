# generated by datamodel-codegen:
#   filename:  rfc8896.json

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Union

Model = Any


@dataclass
class ResponseMeta:
    pass


@dataclass
class ResponseEntityBase:
    meta: Optional[ResponseMeta] = None


MediaType = str


URI = str


PIDName = str


ResourceID = PIDName


@dataclass
class VersionTag:
    resource_id: ResourceID
    tag: str


TypedEndpointAddr = Any


class AddressType(Enum):
    ipv4 = 'ipv4'
    ipv6 = 'ipv6'


IPv4EndpointPrefix = str


IPv6EndpointPrefix = str


@dataclass
class EndpointAddrGroup:
    ipv4: Optional[List[IPv4EndpointPrefix]] = None
    ipv6: Optional[List[IPv6EndpointPrefix]] = None


class CostMode(Enum):
    numerical = 'numerical'
    ordinal = 'ordinal'


class CostMetricEnum(Enum):
    routingcost = 'routingcost'
    delay_ow = 'delay-ow'
    delay_rt = 'delay-rt'
    delay_variation = 'delay-variation'
    hopcount = 'hopcount'
    lossrate = 'lossrate'
    tput = 'tput'
    bw_residual = 'bw-residual'
    bw_maxres = 'bw-maxres'


CostMetric = Union[str, CostMetricEnum]


@dataclass
class CostType:
    cost_mode: CostMode
    cost_metric: CostMetric


ResourceSpecificEndpointProperty = Any


GlobalEndpointProperty = str


EndpointPropertyType = Union[ResourceSpecificEndpointProperty, GlobalEndpointProperty]


IRDMetaCostTypes = Dict[str, CostType]


@dataclass
class Capabilities:
    pass


@dataclass
class IRDResourceEntry:
    uri: URI
    media_type: MediaType
    accepts: Optional[MediaType] = None
    capabilities: Optional[Capabilities] = None
    uses: Optional[List[ResourceID]] = None


IRDResourceEntries = Dict[str, IRDResourceEntry]


@dataclass
class ServiceResponseMeta(ResponseMeta):
    vtag: Optional[VersionTag] = None
    dependent_vtags: Optional[List[VersionTag]] = None


NetworkMapData = Dict[str, EndpointAddrGroup]


@dataclass
class CostMapCapabilities:
    cost_type_names: List[str]


@dataclass
class Meta1(ServiceResponseMeta):
    dependent_vtags: Any
    cost_type: CostType


DstCosts = Dict[str, Optional[Union[str, float, List, bool, Dict[str, Any]]]]


@dataclass
class ReqFilteredNetworkMap:
    pids: List[PIDName]
    address_types: Optional[List[AddressType]] = None


@dataclass
class PIDFilter:
    srcs: List[PIDName]
    dsts: List[PIDName]


@dataclass
class FilteredCostMapCapabilities:
    cost_type_names: Optional[List[str]] = None
    cost_constraints: Optional[bool] = False


@dataclass
class ReqEndpointProp:
    properties: List[EndpointPropertyType]
    endpoints: List[TypedEndpointAddr]


@dataclass
class EndpointPropertyCapabilities:
    prop_types: List[EndpointPropertyType]


EndpointProps = Dict[str, Optional[Union[str, float, List, bool, Dict[str, Any]]]]


@dataclass
class EndpointFilter:
    srcs: Optional[List[TypedEndpointAddr]] = None
    dsts: Optional[List[TypedEndpointAddr]] = None


@dataclass
class Meta2(ServiceResponseMeta):
    cost_type: CostType


EndpointDstCosts = Dict[str, Optional[Union[str, float, List, bool, Dict[str, Any]]]]


@dataclass
class IRDResourceEntriesModel:
    pass


@dataclass
class IRDResourceEntryModel(IRDResourceEntry):
    pass


@dataclass
class CalendarAttributes:
    cost_type_names: List[str]
    time_interval_size: float
    number_of_intervals: float


@dataclass
class CalendarResponseAttributes:
    calendar_start_time: str
    time_interval_size: float
    number_of_intervals: float
    cost_type_names: Optional[List[str]] = None
    repeated: Optional[float] = None


@dataclass
class ReqFilteredCostMap2:
    calendared: Optional[List[bool]] = None


OrConstraint = List[Any]


@dataclass
class ReqFilteredCostMap:
    cost_type: Optional[CostType] = None
    multi_cost_types: Optional[List[CostType]] = None
    testable_cost_types: Optional[List[CostType]] = None
    constraints: Optional[List[str]] = None
    or_constraints: Optional[List[OrConstraint]] = None
    pids: Optional[PIDFilter] = None


@dataclass
class FilteredCostMapCapabilities2(FilteredCostMapCapabilities):
    max_cost_types: Optional[float] = None
    testable_cost_type_names: Optional[List[str]] = None


@dataclass
class Meta3(ServiceResponseMeta):
    dependent_vtags: Any
    multi_cost_types: List[CostType]


@dataclass
class ReqEndpointCostMap1:
    cost_type: Optional[CostType] = None
    multi_cost_types: Optional[List[CostType]] = None
    constraints: Optional[List[str]] = None
    testable_cost_types: Optional[List[CostType]] = None
    or_constraints: Optional[List[OrConstraint]] = None
    endpoints: Optional[EndpointFilter] = None


@dataclass
class Meta4(ServiceResponseMeta):
    multi_cost_types: List[CostType]


@dataclass
class InfoResourceCostMap3:
    meta: Optional[Any] = None


@dataclass
class ReqEndpointCostMap3:
    calendared: Optional[List[bool]] = None


@dataclass
class ReqEndpointCostMap5(ReqEndpointCostMap1, ReqEndpointCostMap3):
    pass


@dataclass
class InfoResourceEndpointCostMap3:
    meta: Optional[Any] = None


@dataclass
class Meta(ResponseMeta):
    cost_types: Optional[IRDMetaCostTypes] = None
    default_alto_network_map: Optional[ResourceID] = None


@dataclass
class InfoResourceDirectory(ResponseEntityBase):
    resources: IRDResourceEntries
    meta: Optional[Meta] = None


@dataclass
class InfoResourceNetworkMap(ResponseEntityBase):
    network_map: NetworkMapData
    meta: Optional[ServiceResponseMeta] = None


CostMapData = Dict[str, DstCosts]


@dataclass
class ReqFilteredCostMapModel:
    cost_type: CostType
    constraints: Optional[List[str]] = None
    pids: Optional[PIDFilter] = None


EndpointPropertyMapData = Dict[str, EndpointProps]


@dataclass
class ReqEndpointCostMap:
    cost_type: CostType
    endpoints: EndpointFilter
    constraints: Optional[List[str]] = None


EndpointCostMapData = Dict[str, EndpointDstCosts]


@dataclass
class FilteredCostMapCapabilities1(FilteredCostMapCapabilities):
    calendar_attributes: Optional[CalendarAttributes] = None


@dataclass
class ReqFilteredCostMap3(ReqFilteredCostMapModel, ReqFilteredCostMap2):
    pass


ReqFilteredCostMap1 = ReqFilteredCostMap3


@dataclass
class InfoResourceDirectory2(InfoResourceDirectory):
    resources: Optional[IRDResourceEntriesModel] = None


@dataclass
class InfoResourceCostMap1(ResponseEntityBase):
    meta: Meta3
    cost_map: CostMapData


@dataclass
class InfoResourceEndpointCostMap1(ResponseEntityBase):
    meta: Meta4
    endpoint_cost_map: EndpointCostMapData


@dataclass
class InfoResourceCostMap5(InfoResourceCostMap1, InfoResourceCostMap3):
    pass


@dataclass
class ReqEndpointCostMap4(ReqEndpointCostMap, ReqEndpointCostMap3):
    pass


ReqEndpointCostMap2 = Union[ReqEndpointCostMap4, ReqEndpointCostMap5]


@dataclass
class InfoResourceEndpointCostMap5(
    InfoResourceEndpointCostMap1, InfoResourceEndpointCostMap3
):
    pass


@dataclass
class InfoResourceCostMap(ResponseEntityBase):
    meta: Meta1
    cost_map: CostMapData


@dataclass
class InfoResourceEndpointProperties(ResponseEntityBase):
    endpoint_properties: EndpointPropertyMapData
    meta: Optional[ServiceResponseMeta] = None


@dataclass
class InfoResourceEndpointCostMap(ResponseEntityBase):
    meta: Meta2
    endpoint_cost_map: EndpointCostMapData


@dataclass
class InfoResourceCostMap4(InfoResourceCostMap, InfoResourceCostMap3):
    pass


InfoResourceCostMap2 = Union[InfoResourceCostMap4, InfoResourceCostMap5]


@dataclass
class InfoResourceEndpointCostMap4(
    InfoResourceEndpointCostMap, InfoResourceEndpointCostMap3
):
    pass


InfoResourceEndpointCostMap2 = Union[
    InfoResourceEndpointCostMap4, InfoResourceEndpointCostMap5
]