'use strict';

var PostEditController = function ($scope, $routeParams, $rootScope, ApiCore, Post) {
    $scope.loaded = false;

    $scope.id = $routeParams.id;

    $scope.post = {};

    $scope.get = function () {
        $scope.loaded = false;

        Post.get($scope.id)
            .then(function (data) {
                $scope.post.title = data.title;
                $scope.post.body = data.body;
                //$scope.post.additional = data.additional;
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $scope.loaded = true;
            }
        );
    };

    $scope.save = function () {
        $scope.loaded = false;

        Post.update($scope.id, $scope.post)
            .then(function (data) {
                $scope.post.title = data.title;
                $scope.post.body = data.body;
                //$scope.post.additional = data.additional;
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $scope.loaded = true;
            }
        );
        $scope.loaded = true;
    };

    $scope.init = $scope.get;

    $scope.$watch('loaded', function (loaded) {
        if (!loaded) {
            $rootScope.$broadcast('globalPreloader:show');
        } else {
            $rootScope.$broadcast('globalPreloader:hide');
        }
    });
};

PostEditController.$inject = ['$scope', '$routeParams', '$rootScope', 'ApiCore', 'Post'];

Controllers.controller('PostEditController', PostEditController);
