'use strict';

var PostService = function (ApiCore) {
    function Post() {

        var self = this;

        var Resource = ApiCore.resource('/post/:id', {
            id: '@id'
        });

        self.get = function (id) {
            return Resource.get({id: id}).$promise;
        };

        self.list = function (ids) {
            return Resource.query({ids: ids}).$promise;
        };

        self.create = function (data) {
            return Resource.save(data).$promise;
        };

        self.update = function (id, data) {
            return Resource.update(angular.extend({}, data, {id: id})).$promise;
        };

        self.remove = function (id) {
            return Resource.remove({id: id}).$promise;
        };

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

PostService.$inject = ['ApiCore'];

Services.factory('Post', PostService);
