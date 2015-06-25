'use strict';

var TextService = function ($resource) {
    function Text() {

        var _this = this;

        var Resource = $resource('/texts/');

        _this.get = function (id) {
            return Resource.get({id: id}).$promise;
        };

        /**
         * @param application_id {Number}
         * @param language_id {Number|null}
         */
        _this.list = function (application_id, language_id) {
            return Resource.query({
                application_id: application_id,
                language_id: language_id
            }).$promise;
        };

        /**
         * @param application_id {Number}
         * @param entries {Array}
         */
        _this.create = function (application_id, entries) {
            return Resource.save({application_id: application_id, items: entries}).$promise;
        };

        /**
         * @param application_id {Number}
         * @param entries {Array}
         */
        _this.update = function (application_id, entries) {
            return Resource.update({application_id: application_id, items: entries}).$promise;
        };

        /**
         * @param entries {Array}
         */
        _this.remove = function (entries) {
            return Resource.remove({items: entries.join(',')}).$promise;
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

    return new Text();
};

TextService.$inject = ['$resource'];

locoMocoServices.factory('Text', TextService);
