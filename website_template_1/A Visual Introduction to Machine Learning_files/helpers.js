var makeAttributeFn = function(scaleType) {
  var currentValue = 0;
  var scroll = 0;
  var clamp = true;

  var abstractDomain = [0, 0.3, 1];
  var inputRange = [0,100];
  var inputScale = d3.scale.linear()
    .domain([0,1])
    .range(inputRange);
  var domain = [0, 30, 100];

  var abstractRange = [0, 1, 1];
  var outputRange = [0,1];
  var outputScale = d3.scale.linear()
    .domain([0,1])
    .range(outputRange);
  var range = [0, 1, 1];

  var interpolator;
  var handleResize = function() {};

  var attribute = function() {
    return currentValue;
  }

  attribute._updateInterpolator = function() {
    domain = _.map(abstractDomain, function(d) {
      return inputScale(d);
    });

    range = _.map(abstractRange, function(r) {
      return outputScale(r);
    });

    interpolator = d3.scale.linear()
      .domain(domain)
      .range(range)
      .clamp(clamp);
  }

  // Input Range is the range of possible
  // inputs, in this case, probably the range
  // of scroll positions.
  //
  // This is abstracted out because the range
  // changes whenever the browser window
  // resizes (i.e. the DOM changes)
  attribute.inputRange = function(value) {
    if (!arguments.length) {
      return inputRange
    }
    if (!$.isArray(value) || value.length != 2) {
      throw "Error: input range must be an array of two values.";
    }

    inputRange = value;
    inputScale = d3.scale.linear()
      .domain([0,1])
      .range(inputRange);

    attribute._updateInterpolator()

    return attribute;
  }

  // Output Range is the range of possible
  // outputs for this attribute.
  //
  // This is abstracted out because the range
  // changes whenever the browser window
  // resizes (i.e. the DOM changes)
  attribute.outputRange = function(value) {
    if (!arguments.length) {
      return outputRange
    }
    if (!$.isArray(value) || value.length != 2) {
      throw "Error: output range must be an array of two values.";
    }

    outputRange = value;
    outputScale = d3.scale.linear()
      .domain([0,1])
      .range(outputRange);

    attribute._updateInterpolator();

    return attribute;
  }

  attribute.clamp = function(value) {
    if (!arguments.length) {
      return outputRange
    }
    if (typeof value !== "boolean") {
      throw "Error: clamp must be a boolean value"
    }

    clamp = value;

    attribute._updateInterpolator();

    return attribute;
  }

  attribute.type = function(value) {
    if (!arguments.length) {
      return type
    }
    if (value !== "linear" && value !== "threshold") {
      throw "Error: attribute's scale type must be 'linear' or 'threshold'";
    }

    type = value;

    attribute._updateInterpolator();

    return attribute;
  }

  // Abstract Domain and Abstract Range are
  // specify the abstact (or normalized)
  // relationship between
  // scroll/time progression (input domain) and
  // attribute value (output range).
  //
  // Values should be within 0 to 1.
  attribute.abstractDomain = function(value) {
    if (!arguments.length) {
      return abstractDomain
    }
    if (!$.isArray(value)) {
      throw "Error: attribute domain must be an array.";
    }

    abstractDomain = value;

    attribute._updateInterpolator();

    return attribute
  }

  attribute.abstractRange = function(value) {
    if (!arguments.length) {
      return abstractRange
    }
    if (!$.isArray(value)) {
      throw "Error: attribute range must be an array.";
    }

    abstractRange = value;

    attribute._updateInterpolator();

    return attribute
  }

  attribute.handleScroll = function(value) {
    scroll = value;
    var newValue = Math.round(interpolator(value) * 10)/10;

    if(newValue == currentValue) {
      return false;
    } else {
      currentValue = newValue;
      return true;
    }
  }

  attribute._updateInterpolator();

  return attribute;
}

var makeThresholdFn = function() {
  var currentValue = 0;
  var scroll = 0;

  var abstractDomain = [0, 0.3, 1];
  var inputRange = [0,100];
  var inputScale = d3.scale.linear()
    .domain([0,1])
    .range(inputRange);
  var domain = [0, 30, 100];

  var abstractRange = [0, 1, 1];
  var outputRange = [0,1];
  var outputScale = d3.scale.linear()
    .domain([0,1])
    .range(outputRange);
  var range = [0, 1, 1];

  var interpolator;
  var handleResize = function() {};

  var attribute = function() {
    return currentValue;
  }

  attribute._updateInterpolator = function() {
    domain = _.map(abstractDomain, function(d) {
      return inputScale(d);
    });

    range = _.map(abstractRange, function(r) {
      return outputScale(r);
    });

    interpolator =f
  }

  // Input Range is the range of possible
  // inputs, in this case, probably the range
  // of scroll positions.
  //
  // This is abstracted out because the range
  // changes whenever the browser window
  // resizes (i.e. the DOM changes)
  attribute.inputRange = function(value) {
    if (!arguments.length) {
      return inputRange
    }
    if (!$.isArray(value) || value.length != 2) {
      throw "Error: input range must be an array of two values.";
    }

    inputRange = value;
    inputScale = d3.scale.linear()
      .domain([0,1])
      .range(inputRange);

    attribute._updateInterpolator()

    return attribute;
  }

  // Output Range is the range of possible
  // outputs for this attribute.
  //
  // This is abstracted out because the range
  // changes whenever the browser window
  // resizes (i.e. the DOM changes)
  attribute.outputRange = function(value) {
    if (!arguments.length) {
      return outputRange
    }
    if (!$.isArray(value) || value.length != 2) {
      throw "Error: output range must be an array of two values.";
    }

    outputRange = value;
    outputScale = d3.scale.linear()
      .domain([0,1])
      .range(outputRange);

    attribute._updateInterpolator();

    return attribute;
  }

  attribute.clamp = function(value) {
    if (!arguments.length) {
      return outputRange
    }
    if (typeof value !== "boolean") {
      throw "Error: clamp must be a boolean value"
    }

    clamp = value;

    attribute._updateInterpolator();

    return attribute;
  }

  // Abstract Domain and Abstract Range are
  // specify the abstact (or normalized)
  // relationship between
  // scroll/time progression (input domain) and
  // attribute value (output range).
  //
  // Values should be within 0 to 1.
  attribute.abstractDomain = function(value) {
    if (!arguments.length) {
      return abstractDomain
    }
    if (!$.isArray(value)) {
      throw "Error: attribute domain must be an array.";
    }

    abstractDomain = value;

    attribute._updateInterpolator();

    return attribute
  }

  attribute.abstractRange = function(value) {
    if (!arguments.length) {
      return abstractRange
    }
    if (!$.isArray(value)) {
      throw "Error: attribute range must be an array.";
    }

    abstractRange = value;

    attribute._updateInterpolator();

    return attribute
  }

  attribute.handleScroll = function(value) {
    scroll = value;
    var newValue = Math.round(interpolator(value) * 10)/10;

    if(newValue == currentValue) {
      return false;
    } else {
      currentValue = newValue;
      return true;
    }
  }

  attribute._updateInterpolator();

  return attribute;
}