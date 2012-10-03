// Functions to highlight the correct tab in the global navigation

// Color for selected
//var highlightcolor='rgb(190,255,154)';
var highlightcolor='rgb(100,163,227)';
//var mouseovercolor='rgb(144,255,83)';
var mouseovercolor='rgb(159,198,237)';
//var mouseoutcolor='rgb(144,255,83)';
var mouseoutcolor='rgb(159,198,237)';
var prevcolor="";

function highlightActive(element)
{
	// Change the 5 tab elements to the selected colors
	for (var i=1; i<=5; i++)
	{
		document.getElementById(element + i).style.backgroundColor=highlightcolor;
	}
}

function mouseoverTab(element)
{
	// Save current color
	prevcolor=document.getElementById(element + "1").style.backgroundColor;
	
	// Change 5 tab elements when mouse enters
	for (var i=1; i<=5; i++)
	{
		document.getElementById(element + i).style.backgroundColor=mouseovercolor;
	}
}

function mouseoutTab(element)
{
	// Change 5 tab elements when mouse exits
	for (var i=1; i<=5; i++)
	{
		document.getElementById(element + i).style.backgroundColor=prevcolor;
	}
}
