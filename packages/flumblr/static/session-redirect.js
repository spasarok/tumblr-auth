// Store user access info in session storage and redirect to safe url
// var userAuthString = window.location.search.substring(1);
var userAuthString = window.location.href
console.log(userAuthString)


// To Do: validate auth string befor redirect

sessionStorage.setItem('userAuthString', userAuthString);
window.location.href = window.location.protocol + '//' + window.location.host + '/user';
