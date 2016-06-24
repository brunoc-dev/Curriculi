var commentModule = angular.module('commentModule',['rest']);

commentModule.directive('commentform', function(){
  return{
    restrict: 'E',
    replace: true,
    templateUrl: '/static/js/angularjs/html/commentform.html',
    controller: function($scope, CommentApi){
      $scope.save = function(){
        $scope.errors = {};
        CommentApi.salvar($scope.comentario).success(function(comentario){
          console.log(comentario);
        }).error(function(errors){
          $scope.errors = errors;
          console.log(errors);
        });
      }
    },
  };
});
