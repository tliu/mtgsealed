// Generated by CoffeeScript 1.8.0
(function() {
  var $;

  $ = jQuery;

  $(function() {
    $("#num-boosters").focus();
    return $("#num-boosters").keypress(function(e) {
      var count;
      if (e.which === 13) {
        count = $("#num-boosters").val();
        return $.get("http://127.0.0.1:5000/boosters?count=" + count, function(data) {
          var add_card, c, id, p, s, _i, _len, _results;
          $("#card-block-W .card").remove();
          $("#card-block-U .card").remove();
          $("#card-block-B .card").remove();
          $("#card-block-R .card").remove();
          $("#card-block-G .card").remove();
          $("#card-block-A .card").remove();
          $("#card-block-M .card").remove();
          $("#card-block-L .card").remove();
          data = data.replace("{", "").replace("}", "").replace(/"/g, "").split(", ");
          _results = [];
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            s = data[_i];
            p = s.split(":");
            id = p[0];
            c = p[1];
            console.log("out: " + id + ", " + c);
            add_card = (function(c) {
              return (function(_this) {
                return function(data) {
                  var color;
                  console.log(data);
                  data = data.replace(/^\s+|\s+$/g, "").replace(/]/g, "").replace(/"/g, "").split(",");
                  data[3] = data[3][1];
                  console.log("card-block-" + data[3]);
                  if (data[3] === "W") {
                    color = "#F0F5B8";
                  }
                  if (data[3] === "U") {
                    color = "#2aa9f7";
                  }
                  if (data[3] === "B") {
                    color = "#999999";
                  }
                  if (data[3] === "R") {
                    color = "#fc3f3f";
                  }
                  if (data[3] === "G") {
                    color = "#17bd45";
                  }
                  if (data[3] === "M") {
                    color = "#ffd700";
                  }
                  if (data[3] === "L") {
                    color = "#f4a460";
                  }
                  if (data[3] === "A") {
                    color = "#964B00";
                  }
                  return $("#card-block-" + data[3]).append("<div class=\"card\" style=\"margin-top: 6px;border: 1px solid #555; border-radius: 5px; padding: 4px; background-color: " + color + ";\"> <span style=\"font-size: 18px; margin-right: 6px\">" + c + "</span> <b>" + data[1] + "</b> </div>");
                };
              })(this);
            })(c);
            _results.push($.get("http://127.0.0.1:5000/cards/id/" + id, add_card));
          }
          return _results;
        });
      }
    });
  });

}).call(this);
