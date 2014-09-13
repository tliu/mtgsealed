// Generated by CoffeeScript 1.8.0
(function() {
  var $;

  $ = jQuery;

  $(function() {
    var cards;
    cards = [];
    $("#cards").focus();
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
          add_card_by_id = function(id) {
            return $.get('http://127.0.0.1:5000/cards/id/' + id, function(data) {
              $("#cards").val("");
              return console.log(data);
            });
          };
          return $.get('http://127.0.0.1:5000/cards/name/' + $("#cards").val(), function(data) {
            return add_card_by_id(data);
          });
        }
      });
    });
  });

}).call(this);
