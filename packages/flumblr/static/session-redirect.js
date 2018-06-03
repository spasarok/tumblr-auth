// Store user oauth session identifier in session storage and redirect to safe url
var path = window.location.pathname;
var userSessionId = path.split('/')[3];
sessionStorage.setItem('userSessionId', userSessionId);
window.location.href = window.location.protocol + '//' + window.location.host + '/user';
