def_jsons := $(patsubst %.yaml,public/%.json,$(wildcard rfc*.yaml draft-*.yaml))
msg_jsons := $(shell utils/generateTests)

openapi_inputs  := $(def_jsons) $(msg_jsons)
openapi_jsons   := $(patsubst public/%.json,public/openapi/%.json,$(openapi_inputs))

all: $(def_jsons) $(msg_jsons) gen_openapi
gen_openapi: $(openapi_jsons)

public/rfc%.json: rfc%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/draft-%.json: draft-%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/message.%.json:
	bash -c "$(shell utils/generateMessageSchema $@)"

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
	rm -f $(def_jsons) $(msg_jsons) $(openapi_jsons)
.PHONY: all clean prepare test gen_openapi
