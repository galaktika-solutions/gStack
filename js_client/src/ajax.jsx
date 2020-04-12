/* global $, gettext */
var _ = require("lodash");

var IsEmpty = require("../utils/is_empty.js");
import Cookies from "js-cookie";

var Ajax = function(options) {
  var statusCode;
  // DEFAULT VALUES
  var default500 = function() {
    window.alert(gettext("Internal Server Error!") + "\n" + gettext("Please contact an admin!"));
  };

  var default504 = function() {
    window.alert(gettext("Request Timeout!") + "\n" + gettext("Please contact an admin!"));
  };

  var default400 = function(jqXHR) {
    const response = jqXHR.responseJSON;
    let title = "";
    let message = [];
    _.forEach(response, (value, key) => {
      title = key === "non_field_errors" ? gettext("Error Reasons") : _.startCase(key);
      message.push(title + ": " + value + "\n");
    });
    window.alert(gettext("Warning!") + "\n" + message.join("\n"));
  };

  var default403 = function() {
    window.alert(gettext("Permission denied!"));
  };

  var default404 = function() {
    window.location.hash = "#/notfound/";
  };

  var default401 = function() {
    window.location.href = window.location.origin;
  };

  var default413 = function() {
    window.alert(
      gettext("The file size is too big!") + "\n" + gettext("The maximum file size is 50MB!")
    );
  };

  var default415 = function() {
    window.alert(
      gettext("Unsopported Media Type!") + "\n" + gettext("This format is not supported!")
    );
  };

  var default205 = function() {
    document.location.reload(true);
  };

  var default204 = function() {
    window.alert(gettext("The Item successfully deleted!"));
  };

  var default201 = function() {
    window.alert(gettext("The Item successfully created!"));
  };

  options.type = IsEmpty(options.type) ? "GET" : options.type;

  if (options.success === undefined) {
    statusCode = IsEmpty(options.statusCode) ? {} : options.statusCode;
    options.statusCode = {
      200: IsEmpty(statusCode["200"]) ? function() {} : statusCode["200"],
      201: IsEmpty(statusCode["201"]) ? default201 : statusCode["201"],
      204: IsEmpty(statusCode["204"]) ? default204 : statusCode["204"],
      205: IsEmpty(statusCode["205"]) ? default205 : statusCode["205"],
      400: IsEmpty(statusCode["400"]) ? default400 : statusCode["400"],
      401: IsEmpty(statusCode["401"]) ? default401 : statusCode["401"],
      403: IsEmpty(statusCode["403"]) ? default403 : statusCode["403"],
      404: IsEmpty(statusCode["404"]) ? default404 : statusCode["404"],
      413: IsEmpty(statusCode["413"]) ? default413 : statusCode["413"],
      415: IsEmpty(statusCode["415"]) ? default415 : statusCode["415"],
      500: IsEmpty(statusCode["500"]) ? default500 : statusCode["500"],
      504: IsEmpty(statusCode["504"]) ? default504 : statusCode["504"]
    };
  }
  options.headers = {version: document.body.getAttribute("version")};

  var originalBeforeSend = options.beforeSend;
  options.beforeSend = (xhr, settings) => {
    if (originalBeforeSend !== undefined) {
      originalBeforeSend(xhr, settings);
    }
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !settings.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
    }
  };

  var ajax = $.ajax(options);
  return ajax;
};

module.exports = Ajax;
