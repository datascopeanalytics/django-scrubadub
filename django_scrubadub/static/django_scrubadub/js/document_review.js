(function () {
    'use strict';

    angular.module('scrubadub', ['onSelect'])
        .controller('ScrubadubController', ScrubadubController);


    function ScrubadubController($scope) {
        var vm = this;
        vm.tktk = tktk;
        return vm;

        function tktk(selection) {
            console.log(selection.getText());
            // selection.highlight('<b></b>');
            // selection.removeHighlight();
        }

    }

})();
