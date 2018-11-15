(function resilientCreateIncidentRunScript(){
	var resHelper = new ResilientHelper();
	
	var gdt = new GlideDateTime();
	var now = gdt.getNumericValue();
	
	var roc_fields = {
		"resolution_id": "Resolved",
		"resolution_summary": "We Fixed it!",
		"roc_bool": true,
		"roc_date_picker": now,
		"roc_datetime_picker": now,
		"roc_multiselect": ["select one", "select two"],
		"roc_number": 14,
		"roc_select": "value two",
		"roc_text": "sample text",
		"roc_textarea_plain": "sample text",
		"roc_textarea_rich": "Rich text sample"
	};
	
	resHelper.close(current, roc_fields);

})();