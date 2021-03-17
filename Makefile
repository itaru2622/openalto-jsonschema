jsons := $(patsubst %.yaml,public/%.json,$(wildcard rfc*.yaml draft-*.yaml))

all: $(jsons)

public/rfc%.json: rfc%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

public/draft-%.json: draft-%.yaml
	emrichen -f config.yaml -f iana.yaml -o $@ --output-format json $<

prepare:
	pip install -r requirements.txt

clean:
	rm $(jsons)
.PHONY: all clean prepare
