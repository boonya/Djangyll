'use strict';

var PostController = function ($scope, $routeParams, $rootScope, ApiCore, Post) {
    $scope.loaded = false;

    $scope.id = $routeParams.id;

    $scope.post = {};

    $scope.init = function () {
        $scope.loaded = false;

        Post.get($scope.id)
            .then(function (data) {
                $scope.post.title = data.title;
                $scope.post.body = markdown.toHTML(data.body);
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $scope.loaded = true;
            }
        );
    };

    $scope.$watch('loaded', function (loaded) {
        if (!loaded) {
            $rootScope.$broadcast('globalPreloader:show');
        } else {
            $rootScope.$broadcast('globalPreloader:hide');
        }
    });
};

PostController.$inject = ['$scope', '$routeParams', '$rootScope', 'ApiCore', 'Post'];

Controllers.controller('PostController', PostController);
