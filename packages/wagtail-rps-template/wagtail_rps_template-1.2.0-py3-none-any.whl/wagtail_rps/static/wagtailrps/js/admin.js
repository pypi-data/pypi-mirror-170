console.log("..:: rps Bandigo CMS ::..");

/*==============================
Nicer Checkbox Label
==============================*/
document.addEventListener("DOMContentLoaded", function(event) {
	const chk_boxes = document.querySelectorAll('input[type=checkbox][id]');
	Array.from(chk_boxes).forEach(function(elem) {
		var label = document.querySelector('label[for='+elem.id+']')
		if (label && label.className == 'w-field__label') {
			label.classList.add("nicer-label")
		}
	})
});