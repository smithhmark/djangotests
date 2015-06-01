(function () {
  'use strict';

  angular
    .module('thinkster.myauth', [
      'thinkster.myauth.controllers',
      'thinkster.myauth.services'
    ]);

  angular
    .module('thinkster.myauth.controllers', []);

  angular
    .module('thinkster.myauth.services', ['ngCookies']);
})();
