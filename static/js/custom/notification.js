function notification($scope, type, text) {
    jQuery('#notification').hide();
    $scope.message = {};
    $scope.message.type = type;
    $scope.message.text = text;
    jQuery('#notification').fadeIn();
}
