$ = jQuery
$ ->
    $("#num-boosters").focus()
    $("#num-boosters").keypress (e) ->
        if e.which == 13
            count = $("#num-boosters").val()
            $.get "http://127.0.0.1:5000/boosters?count=#{count}", (data) ->
                data = data.replace("{","").replace("}","").replace(/"/g,"").split(", ")
                for s in data
                    p = s.split(":")
                    id = p[0]
                    @c = p[1]
                    console.log "out: " + @c
                    add_card = (data) =>
                        console.log "in: " + @c
                        console.log data
                    $.get "http://127.0.0.1:5000/cards/id/#{id}", add_card
                





