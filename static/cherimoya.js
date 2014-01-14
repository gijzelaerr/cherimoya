var cherimoya = angular.module('cherimoya', ['ui.bootstrap'] );

cherimoya.filter('timestamp', function() {
    return function(date) {
        return Math.round(date.getTime() / 1000);
    }
});

cherimoya.controller('RangeCtrl', ['$scope', function($scope) {
  $scope.today = function() {
    $scope.startMoment = new Date();
      $scope.endMoment = new Date();
  };
  $scope.today();

  $scope.showWeeks = true;
  $scope.toggleWeeks = function () {
    $scope.showWeeks = ! $scope.showWeeks;
  };

  $scope.clear = function () {
    $scope.dt = null;
  };

  // Disable weekend selection
  $scope.disabled = function(date, mode) {
    return ( mode === 'day' && ( date.getDay() === 0 || date.getDay() === 6 ) );
  };

  $scope.toggleMin = function() {
    $scope.minDate = ( $scope.minDate ) ? null : new Date();
  };
  $scope.toggleMin();

  $scope.open = function($event) {
    $event.preventDefault();
    $event.stopPropagation();
    $scope.opened = true;
  };

  $scope.toggleMode = function() {
    $scope.ismeridian = ! $scope.ismeridian;
  };

  $scope.update = function() {
    var d = new Date();
    d.setHours( 14 );
    d.setMinutes( 0 );
    $scope.mytime = d;
  };

  $scope.setStartFromTimestamp = function(timestamp) {
      $scope.startMoment = new Date(timestamp * 1000);
  }

  $scope.setEndFromTimestamp = function(timestamp) {
      $scope.endMoment = new Date(timestamp * 1000);
  }

  $scope.changed = function () {
    console.log('Range changed to: ' + $scope.startMoment + ' ' +
    $scope.endMoment);
  };

  $scope.dateOptions = {
    'year-format': "'yy'",
    'starting-day': 1
  };

  $scope.hstep = 1;
  $scope.mstep = 5;
  $scope.ismeridian = true;
  $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'shortDate'];
  $scope.format = $scope.formats[0];


  $scope.width = 992;
  $scope.height = 300;
}]);
