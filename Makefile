# Where `make install` puts parsley's message_types.py: a sibling ../parsley
# checkout by default, or parsley inside the monorepo with UNIVERSE=<path>.
PARSLEY_DIR ?= $(if $(UNIVERSE),$(UNIVERSE)/areas/sw_libs/parsley,../parsley)

.PHONY: all
all: output/message_types.h output/message_types.py output/message_types.ts output/board-id.rst output/packet-format.rst

output/message_types.h: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f message-types-h $< > $@

output/message_types.py: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f message-types-py $< > $@

output/message_types.ts: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f message-types-ts $< > $@

output/board-id.rst: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f board-id-rst $< > $@

output/packet-format.rst: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f packet-format-rst $< > $@

.PHONY: install
install: output/message_types.h output/message_types.py output/message_types.ts output/board-id.rst output/packet-format.rst
	cp output/message_types.h ../canlib
	cp output/message_types.py $(PARSLEY_DIR)/src/parsley
	cp output/board-id.rst ../docs/avionics/rocketcan
	cp output/packet-format.rst ../docs/avionics/rocketcan
	cp output/message_types.ts ../parsley-ts/src/message_types.ts

.PHONY: clean
clean:
	rm -rf output
