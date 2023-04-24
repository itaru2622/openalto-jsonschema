def_jsons := $(patsubst %.yaml,public/%.json,$(wildcard rfc*.yaml draft-*.yaml))
msg_jsons := $(shell utils/generateTests)

jsmodels        := $(def_jsons) $(msg_jsons)
model_pys       := $(patsubst public/%.json,public/pymodel/%.py,$(jsmodels))
openapi_jsons   := $(patsubst public/%.json,public/openapi/%.json,$(jsmodels))

all: gen_jsonschema gen_pymodel gen_openapi 
gen_jsonschema:: ${jsmodels}
gen_openapi: $(openapi_jsons)
gen_pymodel: $(model_pys)

public/rfc%.json: rfc%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/draft-%.json: draft-%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/message.%.json:
	bash -c "$(shell utils/generateMessageSchema $@)"

# generate pydantic model from JSON Schema
public/pymodel/%.py: public/%.json
	-datamodel-codegen  --input-file-type jsonschema --target-python-version 3.11 --use-union-operator  --input $< --output $@

# generate OpenAPI Schema from JSON Schema
# It requires option '-d' (de-ref remote reference) to avoid remaining 'if-then' clauses in OpenAPI Schema
public/openapi/%.json: public/%.json
	json-schema-to-openapi-schema convert -d $<  > $@

prepare:
	pip install -r requirements.txt
	npm install @openapi-contrib/json-schema-to-openapi-schema

test: $(def_jsons) $(msg_jsons)
	bash -c "$(shell utils/generateTests -t)"

clean:
	rm -f $(jsmodels) $(model_pys) $(openapi_jsons) 
.PHONY: all clean prepare test gen_jsonschema gen_pymodel gen_openapi 
