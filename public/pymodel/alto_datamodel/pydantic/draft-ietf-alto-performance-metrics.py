# generated by datamodel-codegen:
#   filename:  draft-ietf-alto-performance-metrics.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field, constr


class Model(BaseModel):
    __root__: Any


class ResponseMeta(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ResponseEntityBase(BaseModel):
    class Config:
        extra = Extra.allow

    meta: Optional[ResponseMeta] = None


class MediaType(BaseModel):
    __root__: constr(
        regex=r'^(application|audio|font|example|image|message|model|multipart|text|video|x-(?:[0-9A-Za-z!#$%&\'*+.^_`|~-]+))\/([0-9A-Za-z!#$%&\'*+.^_`|~-]+)((?:[ \t]*;[ \t]*[0-9A-Za-z!#$%&\'*+.^_`|~-]+=(?:[0-9A-Za-z!#$%&\'*+.^_`|~-]+|"(?:[^"\\]|\.)*"))*)$'
    )


class URI(BaseModel):
    __root__: constr(
        regex=r'^(([^:\/?#]+):)?(\/\/([^\/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?$'
    )


class PIDName(BaseModel):
    __root__: constr(regex=r'^[0-9a-zA-Z-:@_.]{1,64}$')


class ResourceID(BaseModel):
    __root__: PIDName


class VersionTag(BaseModel):
    resource_id: ResourceID = Field(..., alias='resource-id')
    tag: constr(regex=r'^[!-~]+$')


class TypedEndpointAddr(BaseModel):
    __root__: Union[Any]


class AddressType(Enum):
    ipv4 = 'ipv4'
    ipv6 = 'ipv6'


class IPv4EndpointPrefix(BaseModel):
    __root__: constr(
        regex=r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.|(\/(([12]?[0-9])|(3[0-2]))$))){4}'
    )


class IPv6EndpointPrefix(BaseModel):
    __root__: constr(
        regex=r'((((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[a-zA-Z0-9]+)?)|((([^:]+:){6}(([^:]+:[^:]+)|(.*\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?;))\/(([1-5]?[0-9])|(6[0-4]))'
    )


class EndpointAddrGroup(BaseModel):
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


class CostMetric(BaseModel):
    __root__: Union[constr(regex=r'^[0-9a-zA-Z-:_.]{1,32}$'), CostMetricEnum]


class ResourceSpecificEndpointProperty(BaseModel):
    __root__: Any


class GlobalEndpointProperty(BaseModel):
    __root__: constr(regex=r'^[0-9a-zA-Z-:_]{1,32}$')


class EndpointPropertyType(BaseModel):
    __root__: Union[ResourceSpecificEndpointProperty, GlobalEndpointProperty]


class Capabilities(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class IRDResourceEntry(BaseModel):
    uri: URI
    media_type: MediaType = Field(..., alias='media-type')
    accepts: Optional[MediaType] = None
    capabilities: Optional[Capabilities] = None
    uses: Optional[List[ResourceID]] = None


class IRDResourceEntries(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r'^[0-9a-zA-Z-:@_.]{1,64}$'), IRDResourceEntry]


class ServiceResponseMeta(ResponseMeta):
    vtag: Optional[VersionTag] = None
    dependent_vtags: Optional[List[VersionTag]] = Field(None, alias='dependent-vtags')


class NetworkMapData(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r'^[0-9a-zA-Z-:@_.]{1,64}$'), EndpointAddrGroup]


class CostMapCapabilities(BaseModel):
    class Config:
        extra = Extra.allow

    cost_type_names: List[str] = Field(
        ..., alias='cost-type-names', max_items=1, min_items=1
    )


class DstCosts(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[
        constr(regex=r'^[0-9a-zA-Z-:@_.]{1,64}$'),
        Optional[Union[str, float, List, bool, Dict[str, Any]]],
    ]


class ReqFilteredNetworkMap(BaseModel):
    class Config:
        extra = Extra.allow

    pids: List[PIDName]
    address_types: Optional[List[AddressType]] = Field(None, alias='address-types')


class PIDFilter(BaseModel):
    class Config:
        extra = Extra.allow

    srcs: List[PIDName]
    dsts: List[PIDName]


class FilteredCostMapCapabilities(BaseModel):
    class Config:
        extra = Extra.allow

    cost_type_names: Optional[List[str]] = Field(
        None, alias='cost-type-names', min_items=1
    )
    cost_constraints: Optional[bool] = Field(False, alias='cost-constraints')


class ReqEndpointProp(BaseModel):
    class Config:
        extra = Extra.allow

    properties: List[EndpointPropertyType] = Field(..., min_items=1)
    endpoints: List[TypedEndpointAddr] = Field(..., min_items=1)


class EndpointPropertyCapabilities(BaseModel):
    class Config:
        extra = Extra.allow

    prop_types: List[EndpointPropertyType] = Field(..., alias='prop-types', min_items=1)


class EndpointProps(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[
        constr(regex=r'(^[0-9a-zA-Z-:@_.]{1,64}\.pid$)|(^[0-9a-zA-Z-:_]{1,32}$)'),
        Optional[Union[str, float, List, bool, Dict[str, Any]]],
    ]


class EndpointFilter(BaseModel):
    class Config:
        extra = Extra.allow

    srcs: Optional[List[TypedEndpointAddr]] = None
    dsts: Optional[List[TypedEndpointAddr]] = None


class EndpointDstCosts(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Union[
        Dict[
            constr(
                regex=r'^ipv4:(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.|$)){4}'
            ),
            Optional[Union[str, float, List, bool, Dict[str, Any]]],
        ],
        Dict[
            constr(
                regex=r'^ipv6:((((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[a-zA-Z0-9]+)?)|((([^:]+:){6}(([^:]+:[^:]+)|(.*\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?;))$'
            ),
            Optional[Union[str, float, List, bool, Dict[str, Any]]],
        ],
    ]


class CostSource(Enum):
    nominal = 'nominal'
    sla = 'sla'
    import_ = 'import'
    estimation = 'estimation'


class CostContext(BaseModel):
    cost_source: Optional[CostSource] = Field(None, alias='cost-source')
    parameters: Optional[Union[str, float, List, bool, Dict[str, Any]]] = None


class CostType(BaseModel):
    cost_mode: CostMode = Field(..., alias='cost-mode')
    cost_metric: CostMetric = Field(..., alias='cost-metric')


class IRDMetaCostTypes(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r'^.*$'), CostType]


class Meta(ResponseMeta):
    cost_types: Optional[IRDMetaCostTypes] = Field(None, alias='cost-types')
    default_alto_network_map: Optional[ResourceID] = Field(
        None, alias='default-alto-network-map'
    )


class InfoResourceDirectory(ResponseEntityBase):
    meta: Optional[Meta] = None
    resources: IRDResourceEntries


class InfoResourceNetworkMap(ResponseEntityBase):
    meta: Optional[ServiceResponseMeta] = None
    network_map: NetworkMapData = Field(..., alias='network-map')


class Meta1(ServiceResponseMeta):
    dependent_vtags: Any = Field(..., alias='dependent-vtags')
    cost_type: CostType = Field(..., alias='cost-type')


class CostMapData(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r'^[0-9a-zA-Z-:@_.]{1,64}$'), DstCosts]


class ReqFilteredCostMap(BaseModel):
    class Config:
        extra = Extra.allow

    cost_type: CostType = Field(..., alias='cost-type')
    constraints: Optional[List[str]] = None
    pids: Optional[PIDFilter] = None


class EndpointPropertyMapData(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Union[
        Dict[
            constr(
                regex=r'^ipv4:(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.|$)){4}'
            ),
            EndpointProps,
        ],
        Dict[
            constr(
                regex=r'^ipv6:((((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[a-zA-Z0-9]+)?)|((([^:]+:){6}(([^:]+:[^:]+)|(.*\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?;))$'
            ),
            EndpointProps,
        ],
    ]


class ReqEndpointCostMap(BaseModel):
    class Config:
        extra = Extra.allow

    cost_type: CostType = Field(..., alias='cost-type')
    constraints: Optional[List[str]] = None
    endpoints: EndpointFilter


class Meta2(ServiceResponseMeta):
    cost_type: CostType = Field(..., alias='cost-type')


class EndpointCostMapData(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Union[
        Dict[
            constr(
                regex=r'^ipv4:(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.|$)){4}'
            ),
            EndpointDstCosts,
        ],
        Dict[
            constr(
                regex=r'^ipv6:((((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[a-zA-Z0-9]+)?)|((([^:]+:){6}(([^:]+:[^:]+)|(.*\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?;))$'
            ),
            EndpointDstCosts,
        ],
    ]


class CostType1(CostType):
    cost_metric: Optional[Union[CostMetric, Union[Any]]] = Field(
        None, alias='cost-metric'
    )
    cost_context: Optional[CostContext] = Field(None, alias='cost-context')
    description: Optional[str] = None


class InfoResourceCostMap(ResponseEntityBase):
    meta: Meta1
    cost_map: CostMapData = Field(..., alias='cost-map')


class InfoResourceEndpointProperties(ResponseEntityBase):
    meta: Optional[ServiceResponseMeta] = None
    endpoint_properties: EndpointPropertyMapData = Field(
        ..., alias='endpoint-properties'
    )


class InfoResourceEndpointCostMap(ResponseEntityBase):
    meta: Meta2
    endpoint_cost_map: EndpointCostMapData = Field(..., alias='endpoint-cost-map')
