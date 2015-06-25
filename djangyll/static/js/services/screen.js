'use strict';

var ScreenService = function ($resource, $q) {
    function Screen() {

        var _this = this;

        var Resource = $resource('/screens/:id', {id: '@id'});

        _this.get = function (id) {
          return Resource.get({id: id}).$promise;
        };

        _this.list = function (ids) {
            var deferred = $q.defer();
            deferred.resolve([{
                id: 1,
                name: 'Account'
            }, {
                id: 3,
                name: 'Registration'
            }, {
                id: 6,
                name: 'Search'
            }, {
                id: 78,
                name: 'Putin huilo'
            }, {
                id: 55,
                name: 'Login'
            }, {
                id: 2,
                name: 'Landing'
            }]);
            return deferred.promise;
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

    return new Screen();
};

ScreenService.$inject = ['$resource', '$q'];

locoMocoServices.factory('Screen', ScreenService);
