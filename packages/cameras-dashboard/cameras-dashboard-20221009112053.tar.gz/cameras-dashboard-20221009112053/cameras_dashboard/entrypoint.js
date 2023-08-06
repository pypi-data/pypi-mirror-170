
try {
  new Function("import('/hacsfiles/frontend/main-d07cb663.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-d07cb663.js';
  el.type = 'module';
  document.body.appendChild(el);
}
  