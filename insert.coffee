$ = jQuery
$ ->
    cards = []
    $("#cards").focus()
    $.get 'http://127.0.0.1:5000/cards', (data) ->
        cards = JSON.parse data
        $("#cards").autocomplete 
                        source: cards.map (card) -> card[1]
                        minLength: 1
                        autoFocus: true
                   .keypress (e) ->
                       if e.which == 13
                            add_card_by_id = (id) ->
                                $.get 'http://127.0.0.1:5000/cards/id/' + id, (data)->
                                    $("#cards").val("")
                                    console.log data
                            $.get 'http://127.0.0.1:5000/cards/name/' + $("#cards").val(), (data)->
                                add_card_by_id data




