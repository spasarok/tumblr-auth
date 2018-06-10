if(!sessionStorage.getItem('userAuthString')){
  window.location.href = 'http://' + window.location.host + '/unauthorized';
}

serializeJson = function(json) {
  var queryString = [];
  for(var key in json)
    if (json.hasOwnProperty(key)) {
      queryString.push(encodeURIComponent(key) + "=" + encodeURIComponent(json[key]));
    }
  return queryString.join("&");
}

createAndSendXHR = function(serializedData, method, endpoint, callback){
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function(){
    if(xhr.readyState === XMLHttpRequest.DONE) {
      xhr.status === 200 ? console.log(xhr.responseText) : console.log(xhr.status + '\n\nThere was an error');
      if(callback){
        callback(xhr.responseText);
      }
    }
  }
  xhr.open(method, endpoint);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.send(serializedData);
}

getFormData = function(formSelector){
  var inputs = {
    'user_blog_name': document.querySelectorAll(formSelector + ' [name=blog-name]'),
    'title': document.querySelectorAll(formSelector + ' [name=post-title]'),
    'body': document.querySelectorAll(formSelector + ' [name=post-body]')
  }

  var data = {
    'user_auth_string': sessionStorage.getItem('userAuthString'),
  };

  for(var input in inputs){
    if(inputs[input].length > 0){
      data[input] = inputs[input][0].value
    }
  }

  return data;
}

postToTumblrBlog = function(event){
  event.preventDefault();
  var serializedData = serializeJson(getFormData('#post-to-blog-form'));
  var endpoint = window.location.protocol + '//' + window.location.host + '/api/post';
  createAndSendXHR(serializedData, 'POST', endpoint);
}

getTumblrBlogJson = function(event){
  event.preventDefault();
  var serializedData = serializeJson(getFormData('#get-from-blog-form'));
  var endpoint = window.location.protocol + '//' + window.location.host + '/api/get';
  createAndSendXHR(serializedData, 'POST', endpoint, function(response){
    var responseBox = document.getElementById('blog-json-response');
    responseBox.value = response;
    responseBox.classList.remove('hidden');
  });
}

// Attach event handlers
window.onload = function(){
  document.querySelectorAll('#post-to-blog-form .submit-button')[0].onclick = postToTumblrBlog;
  document.querySelectorAll('#get-from-blog-form .submit-button')[0].onclick = getTumblrBlogJson;
}
