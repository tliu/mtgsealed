// Generated by CoffeeScript 1.8.0
(function() {
  var $;

  $ = jQuery;

  $(function() {
    var cards, id_counter;
    cards = [];
    id_counter = 0;
    $("#cards").focus();
    $("#add-booster").click(function() {
      var div, ids, _i, _len, _ref;
      ids = [];
      _ref = $('[id^=card-]');
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        div = _ref[_i];
        ids.push(parseInt($(div).attr("cid")));
      }
      cards = encodeURIComponent(ids.slice(1).toString());
      console.log(cards);
      if (ids.length > 0) {
        return $.get("http://127.0.0.1:5000/boosters/add?cards=" + cards, function(data) {
          return window.location.reload(false);
        });
      }
    });
    $.get('http://127.0.0.1:5000/boosters/count', function(data) {
      return $("#booster-count").html("<h3><span class='label label-default'>boosters recorded: " + data + "</span></h3>");
    });
    return $.get('http://127.0.0.1:5000/cards', function(data) {
      cards = JSON.parse(data);
      return $("#cards").autocomplete({
        source: cards.map(function(card) {
          return card[1];
        }),
        minLength: 1,
        autoFocus: true
      }).keypress(function(e) {
        var add_card_by_id;
        if (e.which === 13) {
          add_card_by_id = (function(_this) {
            return function(id) {
              return $.get('http://127.0.0.1:5000/cards/id/' + id, function(data) {
                var card, card_id, div, img, name;
                card = JSON.parse(data);
                card_id = card[0];
                name = card[1];
                img = card["2"];
                $("#cards").val("");
                $("#num-cards").append("<li>" + name + "</li>");
                div = $("<div id=card-" + id_counter + " style='width: 200px; float: left; margin-right: 6px; display: none;'> <div class='panel panel-default' style='width: 200px'> <div class='panel-heading'>" + name + "</div> <div class='panel-body'> <img width='100%' src='" + img + "'> </div> </div></div>");
                $("#cards-section").append(div);
                div.fadeIn("slow");
                $(div).attr("cid", card_id);
                div.mouseover(function(e) {
                  return $(e.currentTarget).find(".panel").addClass("panel-danger");
                });
                div.mouseout(function(e) {
                  return $(e.currentTarget).find(".panel").removeClass("panel-danger");
                });
                div.click(function(e) {
                  return $(e.currentTarget).remove();
                });
                return id_counter++;
              });
            };
          })(this);
          return $.get('http://127.0.0.1:5000/cards/name/' + encodeURIComponent($("#cards").val()), function(data) {
            return add_card_by_id(data);
          });
        }
      });
    });
  });

}).call(this);
