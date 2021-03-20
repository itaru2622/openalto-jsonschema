def_jsons := $(patsubst %.yaml,public/%.json,$(wildcard rfc*.yaml draft-*.yaml))
msg_jsons := $(shell utils/generateTests)

all: $(def_jsons) $(msg_jsons)

public/rfc%.json: rfc%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/draft-%.json: draft-%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/message.%.json:
	bash -c "$(shell utils/generateMessageSchema $@)"

prepare:
	pip install -r requirements.txt

test: $(def_jsons) $(msg_jsons)
	bash -c "$(shell utils/generateTests -t)"

clean:
	rm $(def_jsons) $(msg_jsons)
.PHONY: all clean prepare test
