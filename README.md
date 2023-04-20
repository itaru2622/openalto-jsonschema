# ALTO JSON Schema

Try online ALTO message validator: <https://openalto.github.io/alto-jsonschema/>

## Generate JSON Schema

Requirements:

- Python 3.7 or later version
- pip
- [emrichen](https://github.com/con2/emrichen)
- [jsonschema](https://github.com/Julian/jsonschema)

additional requirements to generate OpenAPI Schema from JSON Schema:
- nodejs v10 or later version
- npm
- [json-schema-to-openapi-schema](https://github.com/openapi-contrib/json-schema-to-openapi-schema)

Install python dependencies (emrichen, jsonschema):

~~~
$ make prepare
~~~

Modify `config.yaml`:

~~~
# URI prefix for generated JSON schemas
site: "https://openalto.github.io/alto-jsonschema"
~~~

Build JSON schemas from template:

~~~
$ make
~~~

Run validation tests:

~~~
$ make test
~~~

Go to `public/` directory to find the generated JSON schemas.

You can deploy `public/` directory to your own website directly.

## Included JSON Schemas

### Component Schema:

| IETF Standard | Schema File |
| :------------ | :---------- |
| [RFC7285] | [rfc7285.json] |
| [RFC8189] | [rfc8189.json] |
| [RFC8895] | [rfc8895.json] |
| [RFC8896] | [rfc8896.json] |

[RFC7285]: https://tools.ietf.org/html/rfc7285
[RFC8189]: https://tools.ietf.org/html/rfc8189
[RFC8895]: https://tools.ietf.org/html/rfc8895
[RFC8896]: https://tools.ietf.org/html/rfc8896
[rfc7285.json]: https://openalto.github.io/alto-jsonschema/rfc7285.json
[rfc8189.json]: https://openalto.github.io/alto-jsonschema/rfc8189.json
[rfc8895.json]: https://openalto.github.io/alto-jsonschema/rfc8895.json
[rfc8896.json]: https://openalto.github.io/alto-jsonschema/rfc8896.json

### Message Schema:

| ALTO Message Type | Related Standards | Schema Files |
| :---------------- | :---------------- | :----------- |
| InfoResourceDirectory | [RFC7285], [RFC8189], [RFC8895], [RFC8896] | [.rfc7285][ird.rfc7285], [.rfc8189][ird.rfc8189], [.rfc7285.rfc8895][ird.rfc7285.rfc8895], [.rfc7285.rfc8896][ird.rfc7285.rfc8896], [.rfc8189.rfc8895][ird.rfc8189.rfc8895], [.rfc8189.rfc8896][ird.rfc8189.rfc8896], [.rfc7285.rfc8895.rfc8896][ird.rfc7285.rfc8895.rfc8896], [.rfc8189.rfc8895.rfc8896][ird.rfc8189.rfc8895.rfc8896] |
| InfoResourceNetworkMap | [RFC7285] | [.rfc7285][nm.rfc7285] |
| InfoResourceCostMap | [RFC7285], [RFC8189], [RFC8896] | [.rfc7285][cm.rfc7285], [.rfc8189][cm.rfc8189], [.rfc7285.rfc8896][cm.rfc7285.rfc8896], [.rfc8189.rfc8896][cm.rfc8189.rfc8896] |
| ReqFilteredNetworkMap | [RFC7285] | [.rfc7285][fnm.rfc7285] |
| ReqFilteredCostMap | [RFC7285], [RFC8189], [RFC8896] | [.rfc7285][fcm.rfc7285], [.rfc8189][fcm.rfc8189], [.rfc7285.rfc8896][fcm.rfc7285.rfc8896], [.rfc8189.rfc8896][fcm.rfc8189.rfc8896] |
| ReqEndpointProp | [RFC7285] | [.rfc7285][epsp.rfc7285] |
| InfoResourceEndpointProperties | [RFC7285] | [.rfc7285][eps.rfc7285] |
| ReqEndpointCostMap | [RFC7285], [RFC8189], [RFC8896] | [.rfc7285][ecsp.rfc7285], [.rfc8189][ecsp.rfc8189], [.rfc7285.rfc8896][ecsp.rfc7285.rfc8896], [.rfc8189.rfc8896][ecsp.rfc8189.rfc8896] |
| InfoResourceEndpointCostMap | [RFC7285], [RFC8189], [RFC8896] | [.rfc7285][ecs.rfc7285], [.rfc8189][ecs.rfc8189], [.rfc7285.rfc8896][ecs.rfc7285.rfc8896], [.rfc8189.rfc8896][ecs.rfc8189.rfc8896] |
| UpdateStreamReq | [RFC8895] | [.rfc8895][upsr.rfc8895] |
| UpdateStreamControlEvent | [RFC8895] | [.rfc8895][upsc.rfc8895] |


[ird.rfc7285]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc7285.json
[ird.rfc8189]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc8189.json
[ird.rfc7285.rfc8895]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc7285.rfc8895.json
[ird.rfc7285.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc7285.rfc8896.json
[ird.rfc8189.rfc8895]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc8189.rfc8895.json
[ird.rfc8189.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc8189.rfc8896.json
[ird.rfc7285.rfc8895.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc7285.rfc8895.rfc8896.json
[ird.rfc8189.rfc8895.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceDirectory.rfc8189.rfc8895.rfc8896.json

[nm.rfc7285]: https://openalto.github.io/alto-jsonschema/message.InfoResourceNetworkMap.rfc7285.json

[cm.rfc7285]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc7285.json
[cm.rfc8189]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc8189.json
[cm.rfc7285.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc7285.rfc8896.json
[cm.rfc8189.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc8189.rfc8896.json

[fnm.rfc7285]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredNetworkMap.rfc7285.json

[fcm.rfc7285]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc7285.json
[fcm.rfc8189]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc8189.json
[fcm.rfc7285.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc7285.rfc8896.json
[fcm.rfc8189.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqFilteredCostMap.rfc8189.rfc8896.json

[epsp.rfc7285]: https://openalto.github.io/alto-jsonschema/message.ReqEndpointProp.rfc7285.json

[eps.rfc7285]: https://openalto.github.io/alto-jsonschema/message.InfoResourceEndpointProperties.rfc7285.json

[ecsp.rfc7285]: https://openalto.github.io/alto-jsonschema/message.ReqEndpointCostMap.rfc7285.json
[ecsp.rfc8189]: https://openalto.github.io/alto-jsonschema/message.ReqEndpointCostMap.rfc8189.json
[ecsp.rfc7285.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqEndpointCostMap.rfc7285.rfc8896.json
[ecsp.rfc8189.rfc8896]: https://openalto.github.io/alto-jsonschema/message.ReqEndpointCostMap.rfc8189.rfc8896.json

[ecs.rfc7285]: https://openalto.github.io/alto-jsonschema/message.InfoResourceEndpointCostMap.rfc7285.json
[ecs.rfc8189]: https://openalto.github.io/alto-jsonschema/message.InfoResourceEndpointCostMap..rfc8189.json
[ecs.rfc7285.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceEndpointCostMap.rfc7285.rfc8896.json
[ecs.rfc8189.rfc8896]: https://openalto.github.io/alto-jsonschema/message.InfoResourceEndpointCostMap.rfc8189.rfc8896.json

[upsr.rfc8895]: https://openalto.github.io/alto-jsonschema/message.UpdateStreamReq.rfc8895.json

[upsc.rfc8895]: https://openalto.github.io/alto-jsonschema/message.UpdateStreamControlEvent.rfc8895.json
