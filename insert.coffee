$ = jQuery
$ ->
    cards = []
    id_counter = 0
    $("#cards").focus()

    $("#add-booster").click ()->
        ids = []
        for div in $('[id^=card-]') 
            ids.push parseInt($(div).attr "cid")

        # where the fuck did this NaN come from?
        cards = encodeURIComponent(ids.slice(1).toString())
        console.log cards
        if ids.length > 0
           $.get "http://127.0.0.1:5000/boosters/add?cards=#{cards}", (data)->
               window.location.reload(false)

    $.get 'http://127.0.0.1:5000/boosters/count', (data) ->
        $("#booster-count").html("<h3><span class='label label-default'>boosters recorded: #{data}</span></h3>")
    $.get 'http://127.0.0.1:5000/cards', (data) ->
        cards = JSON.parse data
        $("#cards").autocomplete 
                        source: cards.map (card) -> card[1]
                        minLength: 1
                        autoFocus: true
                   .keypress (e) ->
                       if e.which == 13
                            add_card_by_id = (id) =>
                                $.get 'http://127.0.0.1:5000/cards/id/' + id, (data)=>
                                    card = JSON.parse data
                                    card_id = card[0]
                                    name = card[1]
                                    img = card["2"]
                                    $("#cards").val("")
                                    $("#num-cards").append("<li>#{name}</li>")
                                    div = $("
                                        <div id=card-#{id_counter} style='width: 200px; float: left; margin-right: 6px; display: none;'>
                                        <div class='panel panel-default' style='width: 200px'>
                                            <div class='panel-heading'>#{name}</div>
                                            <div class='panel-body'>
                                                <img width='100%' src='#{img}'>
                                            </div>
                                        </div></div>")

                                    $("#cards-section").append div
                                    div.fadeIn("slow")
                                    $(div).attr "cid", card_id
                                    div.mouseover (e) =>
                                        $(e.currentTarget).find(".panel").addClass("panel-danger")
                                    div.mouseout (e) =>
                                        $(e.currentTarget).find(".panel").removeClass("panel-danger")
                                    div.click (e) =>
                                        $(e.currentTarget).remove()
                                    id_counter++
                            $.get 'http://127.0.0.1:5000/cards/name/' + encodeURIComponent($("#cards").val()), (data)->
                                add_card_by_id data




