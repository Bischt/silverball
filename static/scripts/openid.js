/* OpenID authentication scripts.  Used for simplifying the provider interface */

// Google
function openidYahoo() {
	var providerURL="https://me.yahoo.com";
	document.getElementById("openidprovider").value=providerURL;
}

// Yahoo
function openidGoogle() {
	var providerURL="https://www.google.com/accounts/o8/id";
	document.getElementById("openidprovider").value=providerURL;
}

