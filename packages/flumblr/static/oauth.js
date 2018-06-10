// Clear active session
sessionStorage.removeItem('userSessionId');

// Send user to Tumblr for authorization
sendOauthRequest = function(){
  var httpRequest = new XMLHttpRequest();

  // Send user to Tumblr for authorization
  httpRequest.onreadystatechange = function(){
    console.log(httpRequest.response)

    if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
      tumblrAuthUrl = httpRequest.response.tumblr_auth_url;
      window.location.href = tumblrAuthUrl ;
    }
  }



  // var getJSON = function(url, callback) {
  //     var xhr = new XMLHttpRequest();
  //     xhr.open('GET', url, true);
  //     xhr.responseType = 'json';
  //     xhr.onload = function() {
  //       var status = xhr.status;
  //       if (status === 200) {
  //         callback(null, xhr.response);
  //       } else {
  //         callback(status, xhr.response);
  //       }
  //     };
  //     xhr.send();
  // };


  // Hit backend to initiate oauth session and return Tumblr url for user authorization
  httpRequest.open('GET', 'http://' + window.location.host + '/auth/tumblr');
  httpRequest.responseType = 'json'
  httpRequest.send();



  // Hit backend to initiate oauth session and return Tumblr url for user authorization
  // httpRequest.open('GET', 'http://' + window.location.host + '/oauth/auth_url');
  // httpRequest.send();
}

// Attach event handlers
window.onload = function(){
  document.getElementById('authenticate-button').onclick = sendOauthRequest;
}
