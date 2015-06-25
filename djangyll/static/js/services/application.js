'use strict';

var ApplicationService = function ($resource) {
    function Application() {

        var _this = this;

        var Resource = $resource('/apps/:app_id/:property/:pid', {
            app_id: '@app_id',
            property: '@property',
            pid: '@pid'
        });

        _this.get = function (app_id) {
            return Resource.get({app_id: app_id}).$promise;
        };

        _this.list = function (ids) {
            return Resource.query({ids: ids}).$promise;
        };

        _this.languages = function (app_id, languages) {
            return Resource.query({
                app_id: app_id,
                property: 'languages',
                ids: languages
            }).$promise;
        };

        _this.participants = function (app_id, participants) {
            return Resource.query({
                app_id: app_id,
                property: 'participants',
                ids: participants
            }).$promise;
        };

        _this.create = function (name, languages) {
            return Resource.save({
                name: name,
                languages: languages
            }).$promise;
        };

        _this.update = function (app_id, input) {
            var data = {app_id: app_id};
            if (input['name']) data['name'] = input['name'];
            if (input['languages']) data['languages'] = input['languages'];
            if (input['participants']) data['participants'] = input['participants'];
            return Resource.update(data).$promise;
        };

        _this.remove = function (app_id) {
            return Resource.remove({app_id: app_id}).$promise;
        };

        // export public methods
        return {
            get: _this.get,
            list: _this.list,
            create: _this.create,
            update: _this.update,
            remove: _this.remove,
            languages: _this.languages,
            participants: _this.participants
        };
    }

    return new Application();
};

ApplicationService.$inject = ['$resource'];

locoMocoServices.factory('Application', ApplicationService);
