// Clear active session
sessionStorage.removeItem('userSessionId');

// Initiate oauth session and send user to Tumblr for authorization
sendOauthRequest = function(){
  var httpRequest = new XMLHttpRequest();

  // Send user to Tumblr for authorization
  httpRequest.onreadystatechange = function(){
    if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
      var responseLines = httpRequest.responseText.split('\n');
      window.location.href = responseLines[responseLines.length - 1];
    }
  }

  // Hit backend to initiate oauth session and return Tumblr url for user authorization
  httpRequest.open('GET', 'http://' + window.location.host + '/oauth/auth_url');
  httpRequest.send();
}

// Attach event handlers
window.onload = function(){
  document.getElementById('authenticate-button').onclick = sendOauthRequest;
}
