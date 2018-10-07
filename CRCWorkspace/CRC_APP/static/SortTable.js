function sortTable(column, type="string") {
		var table, rows, switching, i, x, y, shouldSwitch;
		table = document.getElementById("resultsTable");
		switching = true;
		hasSwitchedOnce = false;
	  /*Make a loop that will continue until
	  no switching has been done:*/
		while (switching) {
			//start by saying: no switching is done:
			switching = false;
			rows = table.rows;
			/*Loop through all table rows (except the
			first, which contains table headers):*/
			for (i = 1; i < (rows.length - 1); i++) {
				//start by saying there should be no switching:
				shouldSwitch = false;
				/*Get the two elements you want to compare,
				one from current row and one from the next:*/
				x = rows[i].getElementsByTagName("td")[column];
				x = x.innerHTML.toLowerCase();
				y = rows[i + 1].getElementsByTagName("td")[column];
				y = y.innerHTML.toLowerCase();
				if (type != "string"){
					x = parseFloat(x);
					y = parseFloat(y);
				}
				//check if the two rows should switch place:
				if (x > y) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					hasSwitchedOnce = true;
					break;
				}
			}
			if (shouldSwitch) {
				/*If a switch has been marked, make the switch
				and mark that a switch has been done:*/
				rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
				switching = true;
			}
		}
		if (!hasSwitchedOnce) {
			switching = true;
			while (switching) {
				//start by saying: no switching is done:
				switching = false;
				rows = table.rows;
				/*Loop through all table rows (except the
				first, which contains table headers):*/
				for (i = 1; i < (rows.length - 1); i++) {
					//start by saying there should be no switching:
					shouldSwitch = false;
					/*Get the two elements you want to compare,
					one from current row and one from the next:*/
					x = rows[i].getElementsByTagName("td")[column];
					x = x.innerHTML.toLowerCase();
					y = rows[i + 1].getElementsByTagName("td")[column];
					y = y.innerHTML.toLowerCase();
					if (type != "string"){
						x = parseFloat(x);
						y = parseFloat(y);
					}
					//check if the two rows should switch place:
					if (x < y) {
						//if so, mark as a switch and break the loop:
						shouldSwitch = true;
						hasSwitchedOnce = true;
						break;
					}
				}
				if (shouldSwitch) {
					/*If a switch has been marked, make the switch
					and mark that a switch has been done:*/
					rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
					switching = true;
				}
			}
		}
	}