INDEX := deployment/index.html

define generate_index
	chmod +w $(INDEX)
	./generate_index/main.py > $(INDEX)
	chmod -w $(INDEX)
endef

$(INDEX): generate_index/*.py template.html
	$(call generate_index)

.PHONY: force
force:
	$(call generate_index)
