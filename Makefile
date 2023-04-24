def_jsons := $(patsubst %.yaml,public/%.json,$(wildcard rfc*.yaml draft-*.yaml))
msg_jsons := $(shell utils/generateTests)

jsschema        := $(def_jsons) $(msg_jsons)
jsschema_yamls  := $(jsschema:.json=.yaml)
model_pys       := $(patsubst public/%.json,public/pymodel/%.py,$(jsschema))
openapi_jsons   := $(patsubst public/%.json,public/openapi/%.json,$(jsschema))
openapi_yamls   := $(openapi_jsons:.json=.yaml)

oDir            =${PWD}/public
#site           =https://openalto.github.io/alto-jsonschema
#site           =https://raw.githubusercontent.com/openalto/alto-jsonschema/gh-pages
site            =https://raw.githubusercontent.com/itaru2622/openalto-jsonschema/allinone/public

opt_pymodel     =--target-python-version 3.11 --use-union-operator --output-model-type dataclasses.dataclass
opt_pymodel     =

define SITE_CONTENT
# URI prefix for generated JSON schemas
site: "${oDir}"
endef
export SITE_CONTENT

all: gen_all publish
gen_all: config_yaml gen_jsonschema gen_jsonschema_yamls gen_pymodel gen_openapi gen_openapi_yamls
gen_jsonschema:: $(jsschema)
gen_jsonschema_yamls: $(jsschema_yamls)
gen_openapi: $(openapi_jsons)
gen_openapi_yamls: $(openapi_yamls)
gen_pymodel: $(model_pys)

config_yaml:
	echo "$${SITE_CONTENT}" > config.yaml

public/rfc%.json: rfc%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/draft-%.json: draft-%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/message.%.json:
	bash -c "$(shell utils/generateMessageSchema $@)"

public/%.yaml: public/%.json
	cat $< | yq -y > $@
public/openapi/%.yaml: public/openapi/%.json
	cat $< | yq -y > $@

# generate pydantic model from JSON Schema
public/pymodel/%.py: public/%.json
	-datamodel-codegen  --input-file-type jsonschema ${opt_pymodel}  --input $< --output $@

# generate OpenAPI Schema from JSON Schema
# It requires option '-d' (de-ref remote reference) to avoid remaining 'if-then' clauses in OpenAPI Schema
public/openapi/%.json: public/%.json
	json-schema-to-openapi-schema convert -d $< | jq > $@

publish:
	-sed -i "s#${oDir}#${site}#g"                public/*.json public/*.yaml
	-sed -i "s#${oDir}#${site}/pymodel#g"        public/pymodel/*.py
	-sed -i "s#${oDir}#${site}/openapi#g"        public/openapi/*.json public/openapi/*.yaml
	-sed -i "s/.json#/.yaml#/g"                  public/*.yaml public/openapi/*.yaml
	-sed -i 's#id: \(.*\).json#id: \1.yaml#g'    public/*.yaml public/openapi/*.yaml

prepare:
	pip install -r requirements.txt
	npm install @openapi-contrib/json-schema-to-openapi-schema

test: $(jsschema)
	bash -c "$(shell utils/generateTests -t)"

clean:
	rm -f $(jsschema) $(jsschema_yamls) $(model_pys) $(openapi_jsons) $(openapi_yamls)
.PHONY: all clean prepare test gen_all config_yaml gen_jsonschema gen_jsonschema_yamls gen_pymodel gen_openapi gen_openapi_yamls publish
