'use strict';

var ApiCoreFactory = function ($modal, $log) {
    var ApiCore = function () {
        var _this = this;

        _this.throwApiError = function (error) {
            $log.info('API error: ', error);

            if (403 == error.status) {
                location.href = '/accounts/login/';
                return;
            }

            var size;
            if (angular.isDefined(error.data)) {
                size = 'lg'
            }

            $modal.open({
                windowClass: 'api-error',
                templateUrl: 'html/api_error.html',
                controller: function ($scope, $modalInstance) {
                    $scope.error = error;
                    $scope.close = function () {
                        $modalInstance.dismiss('close');
                    };
                },
                size: size
            });
        };

        // public members
        return {
            throwApiError: _this.throwApiError
        };
    };

    return new ApiCore();
};

ApiCoreFactory.$inject = ['$modal', '$log'];

locoMocoServices.factory('ApiCore', ApiCoreFactory);
