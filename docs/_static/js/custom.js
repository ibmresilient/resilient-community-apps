// Add custom "download from app exchange" button to each README file
// uses that README name to determine if the button should be added
if (document.URL.endsWith("README.html")) {
    var headerElem = document.getElementsByTagName("h1")[0];
    var appName = headerElem["innerText"];
    var appXLink = encodeURI(`https://exchange.xforce.ibmcloud.com/hub?q=${appName} soar`);
    var appXButton = `<p><a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="${appXLink}"><span>Download ${appName} on App Exchange</span></a></p>`;
    headerElem.innerHTML += appXButton;
}
