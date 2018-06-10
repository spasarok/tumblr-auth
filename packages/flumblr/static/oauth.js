// Clear active session
sessionStorage.removeItem('userAuthString');

// Send user to Tumblr for authorization
sendOauthRequest = function(){
  var httpRequest = new XMLHttpRequest();

  // Send user to Tumblr for authorization
  httpRequest.onreadystatechange = function(){

    if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
      tumblrAuthUrl = httpRequest.response.tumblr_auth_url;
      window.location.href = tumblrAuthUrl;
    }
  }

  // Hit backend to initiate oauth session and return Tumblr url for user authorization
  httpRequest.open('GET', 'http://' + window.location.host + '/auth/tumblr');
  httpRequest.responseType = 'json'
  httpRequest.send();
}

// Attach event handlers
window.onload = function(){
  document.getElementById('authenticate-button').onclick = sendOauthRequest;
}
