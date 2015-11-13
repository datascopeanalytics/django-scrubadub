(function () {
    'use strict';

    angular.module('scrubadub', ['onSelect', 'ngAnimate', 'ui.bootstrap.popover', 'ui.bootstrap.tpls'])
        .controller('ScrubadubController', ScrubadubController);


    function ScrubadubController($scope) {
        var vm = this;
        vm.handleSelection = handleSelection;
        return vm;

        function handleSelection(selection) {
            selection.highlight('<span uib-popover="tktk" popover-is-open="true"></span>');

            console.log(selection.getText());
            // selection.highlight('<b></b>');
            // selection.removeHighlight();
        }

    }

})();
