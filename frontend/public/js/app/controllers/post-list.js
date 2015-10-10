'use strict';

var PostListController = function ($scope, $rootScope, ApiCore, Post) {
    $scope.loaded = false;

    /**
     * List of all available posts.
     *
     * @type {Array}
     */
    $scope.posts = [];

    /**
     * Get list of all available posts.
     */
    $scope.list = function () {
        $scope.loaded = false;

        Post.list()
            .then(function (data) {
                $scope.posts = data;
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

PostListController.$inject = ['$scope', '$rootScope', 'ApiCore', 'Post'];

Controllers.controller('PostListController', PostListController);
