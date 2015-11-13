(function () {
    'use strict';

    angular.module('scrubadub', ['onSelect', 'ngAnimate', 'ui.bootstrap.popover', 'ui.bootstrap.tpls'])
        .controller('ScrubadubController', ScrubadubController);


    function ScrubadubController(RangeService, $scope) {
        var vm = this;
        vm.handleSelection = handleSelection;
        vm.templateUrl = '/static/django_scrubadub/templates/popover.html';
        vm.onFilthSelected = onFilthSelected;
        vm.currentSelection = undefined;
        vm.popoverShown = [];

        return vm;

        function handleSelection(selection) {
            // TODO: Make Clark fix this
            if (RangeService.disabled) {
                return;
            }

            vm.popoverShown.push(true);
            var isOpen = "vm.popoverShown["+(vm.popoverShown.length-1)+"]";

            RangeService.disabled = true;
            vm.currentSelection = selection;
            selection.highlight('<span class="filth" uib-popover-template="vm.templateUrl" popover-is-open="'+isOpen+'"></span>');

            // selection.highlight('<b></b>');
            // selection.removeHighlight();
        }

        function onFilthSelected() {
            console.log(vm.currentSelection)
            console.log('we have determined that', vm.currentSelection.getText());
            console.log('   is a filthy little ', vm.filthType);

            vm.popoverShown[vm.popoverShown.length-1] = false;
            RangeService.disabled = false;
            // vm.currentSelection.removeHighlight();
        }

    }

})();
