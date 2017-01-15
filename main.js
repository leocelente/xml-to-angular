angular.module('app', ['q', 'ngRoute'])
.controller('HomeCtrl',function($scope,$rootScope) {
     function action(x,y) {
    // Body....
   }
     function another_action(args) {
    // Body....
   }
     var page_name = "";
     var userdata = {};
     var age = 0;
     var cars = {};

})
.controller('LoginCtrl',function($scope,$rootScope) {
     function login(username,password) {
    // Body....
   }
     function signup(username,password) {
    // Body....
   }
     var returned_data = {};
     var registered = 0;

})
.factory('DatabaseFact',function($http) {
    var out;
     out.login = function login(username,password) {
    // Body....
   };
     out.signup = function signup(username,password) {
    // Body....
   };
     var returned_data = {};
     var registered = 0;

   return out;
})
.factory('UserFact',function($http) {
    var out;
     out.login = function login(username,password) {
    // Body....
   };
     out.signup = function signup(username,password) {
    // Body....
   };
     var returned_data = {};
     var registered = 0;

   return out;
})
;