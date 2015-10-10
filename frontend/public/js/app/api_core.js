'use strict';

//var ApiCoreFactory = function ($modal, $log) {
var ApiCoreFactory = function ($log) {
    var ApiCore = function () {
        var self = this,
            host = 'http://localhost:5000/';

        self.getHost = function (path) {
            var result = /^(\/+)(.*)/gi.exec(path);
            if (3 <= result.length) {
                path = result[2];
            }
            return host + path;
        };

        self.throwApiError = function (error) {
            $log.info('API error: ', error);

            if (403 == error.status) {
                location.href = '/accounts/login/';
                return;
            }

            var size;
            if (angular.isDefined(error.data)) {
                size = 'lg'
            }

            //$modal.open({
            //    windowClass: 'api-error',
            //    templateUrl: 'html/api_error.html',
            //    controller: function ($scope, $modalInstance) {
            //        $scope.error = error;
            //        $scope.close = function () {
            //            $modalInstance.dismiss('close');
            //        };
            //    },
            //    size: size
            //});
        };

        // public members
        return {
            getHost: self.getHost,
            throwApiError: self.throwApiError
        };
    };

    return new ApiCore();
};

//ApiCoreFactory.$inject = ['$modal', '$log'];
ApiCoreFactory.$inject = ['$log'];

Services.factory('ApiCore', ApiCoreFactory);
