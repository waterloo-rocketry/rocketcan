.PHONY: all
all: output/message_types.h output/message_types.py output/board-id.rst output/packet-format.rst 

output/message_types.h: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f message-types-h $< > $@

output/message_types.py: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f message-types-py $< > $@

output/board-id.rst: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f board-id-rst $< > $@

output/packet-format.rst: rocketcan.yaml
	mkdir -p output
	python genre/genre.py -f packet-format-rst $< > $@

.PHONY: install
install: output/message_types.h output/message_types.py output/board-id.rst output/packet-format.rst 
	cp output/message_types.h ../canlib
	cp output/message_types.py ../parsley/src/parsley
	cp output/board-id.rst ../docs/avionics/rocketcan
	cp output/packet-format.rst ../docs/avionics/rocketcan

.PHONY: clean
clean:
	rm -rf output
