'use strict';

var ApiCoreFactory = function ($resource, $log) {
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
            }
        };

        self.resource = function (url, paramDefaults, actions, options) {
            var extendedActions = angular.extend({}, {update: {method:'PUT'}},
                actions);

            return $resource(self.getHost(url), paramDefaults,
                extendedActions, options);
        };

        return {
            getHost: self.getHost,
            throwApiError: self.throwApiError,
            resource: self.resource
        };
    };

    return new ApiCore();
};

ApiCoreFactory.$inject = ['$resource', '$log'];

Services.factory('ApiCore', ApiCoreFactory);
