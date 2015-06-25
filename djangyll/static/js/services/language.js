'use strict';

var LanguageService = function ($resource) {
    function Language() {

        var _this = this;

        var Resource = $resource('/languages/:id', {id: '@id'});

        _this.get = function (id) {
          return Resource.get({id: id}).$promise;
        };

        _this.list = function (ids) {
            return Resource.query({ids: ids}).$promise;
        };

        _this.create = function (name) {
            return Resource.save({name: name}).$promise;
        };

        _this.update = function (id, name) {
            return Resource.update({
                id: id,
                name: name
            }).$promise;
        };

        _this.remove = function (id) {
            return Resource.remove({id: id}).$promise;
        };

        // export public methods
        return {
            get: _this.get,
            list: _this.list,
            create: _this.create,
            update: _this.update,
            remove: _this.remove
        };
    }

    return new Language();
};

LanguageService.$inject = ['$resource'];

locoMocoServices.factory('Language', LanguageService);
