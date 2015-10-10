'use strict';

var PostService = function ($resource, ApiCore) {
    function Post() {

        var self = this;

        var Resource = $resource(ApiCore.getHost('/post/:id'), {
            id: '@id'
        });

        self.get = function (id) {
            return Resource.get({id: id}).$promise;
        };

        self.list = function (ids) {
            return Resource.query({ids: ids}).$promise;
        };

        self.create = function (data) {
            throw new Exception("Not implemented yet.");
        };

        self.update = function (id, data) {
            throw new Exception("Not implemented yet.");
        };

        self.remove = function (id) {
            throw new Exception("Not implemented yet.");
        };

        // export public methods
        return {
            get: self.get,
            list: self.list,
            create: self.create,
            update: self.update,
            remove: self.remove
        };
    }

    return new Post();
};

PostService.$inject = ['$resource', 'ApiCore'];

Services.factory('Post', PostService);
